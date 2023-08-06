# -*- coding: utf-8 -*-
"""
The 'config' module of the CLI
"""

import getpass
import logging
import os
import stat
import sys
from pathlib import PosixPath, Path
from typing import Any, Dict

import typer
import yaml

from cli import __app_name__, get_default_config_file_path, get_default_stocks_api_url
from cli.config import get_config
from stocks import AssayStructureError
from stocks.assaysniffer import AssaySniffer
from stocks.assaysniffer.registry import registry
from stocks.models import User, Assay, InstrumentRun, Study
from stocksapi.client import StocksClient
from stocksapi.exceptions import MultipleObjectMatchedError
from stocksapi.manager import StocksManager
from requests.exceptions import ConnectionError

logger = logging.getLogger(__name__)

# name of this module (as appearing on the command line) is the last part of the __name__ e.g. cli.config -> config
_MODULE_NAME = __name__.rsplit(".", 1)[-1]
# list of command names offered in this module
_CMD_VALIDATE_ASSAY = "assay"

# create the CLI app
app = typer.Typer()


@app.command(_CMD_VALIDATE_ASSAY,
             short_help="Validate an assay in the 'initialized' state.",
             help=
             """
             Longer help
             """
             )
def validate_assay(
        run_dir: Path = typer.Option(
            ...,
            "--run-dir",
            "-r",
            help="Path to the assay run directory to validate."
        ),
        sniffer_name: str = typer.Option(
            ...,
            "--name",
            "-n",
            help="Name of the sniffer to use to extract the dataset and sample information."
        ),
        study_id: str = typer.Option(
            ...,
            "--study",
            "-s",
            help="The UUID of the study to which all the datasets will be associated "
        ),
        conf_file_path: str = typer.Option(
            get_default_config_file_path(),
            "--config-path",
            help="Config file absolute path")
) -> None:
    """
    Register one or more assay and associated raw data to STOCKS. All assays must be of the same type i.e. same
    technology (e.g. 'sequencing') and platform (e.g. Illumina or Nanopore) and produced by a unique instrument run.
    The assay(s) are parsed from a run directory obeying a structure recognized by a 'sniffer'.
    """
    _config = get_config(Path(conf_file_path))
    client: StocksClient = StocksClient(_config)
    stocks_manager: StocksManager = StocksManager(client)

    # Check given id is really a study
    study: Study = stocks_manager.fetch_study(study_id, load_ownership=False)
    if not study:
        raise typer.BadParameter(f"Wrong value provided for --study, no study returned for UUID {study_id}")

    # snif the run-dir
    registry.load_custom_plugins_from_plugin_base_dir(
        Path("./plugins/assaysniffers").resolve()
    )
    sniffer: AssaySniffer = registry.get_sniffer_instance(sniffer_name)
    if not sniffer:
        raise typer.BadParameter(f"Unknown sniffer name: {sniffer_name}. "
                                 f"Registered sniffers: {registry.get_registered_sniffer_names()}")

    sniffer.set_stocks_manager(stocks_manager=stocks_manager)
    # looks good, snif the dir_path
    try:
        runs = sniffer.sniff_instrument_run_assays(
            dir_path=run_dir, group=stocks_manager.logged_in_user.get_primary_group().name)
    except AssayStructureError as err:
        logger.error(str(err))
        print(f"The data in {str(run_dir)} does not comply to the sniffer {sniffer_name} expectations!")
        sys.exit(1)
    except MultipleObjectMatchedError as e:
        raise typer.BadParameter(f"{len(e.results)} assays returned for --run-dir {run_dir}")

    if not runs or len(runs) == 0:
        raise typer.BadParameter(f"Sniffer '{sniffer_name}' could not detect any assay i.e. data in {str(run_dir)} "
                                 f"is not recognized by this sniffer.")
    if len(runs) > 1:
        raise typer.BadParameter(f"Sniffer '{sniffer_name}' detected {len(runs)} instrument runs in the directory"
                                 f" {str(run_dir)}. Loading mutliple runs at once is not supported; please call"
                                 f" the {_CMD_VALIDATE_ASSAY} command on a folder containing results for a unique run")

    the_run: InstrumentRun = runs[0]
    if len(the_run.assays) != 1:
        raise typer.BadParameter(f"The sniffer '{sniffer_name}' detected {len(the_run.assays)} assay(s) while a unique"
                                 f" one is expected in the {_CMD_VALIDATE_ASSAY} command.")
    the_assay: Assay = the_run.assays[0]

    print(stocks_manager.validate_assay(the_assay, study_id=study.id))
