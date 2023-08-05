import os
import subprocess
from pathlib import Path
from atro_rsync.helpers import wrap_in_double_quotes
import logging

def rsync(source: Path, destination: Path, options: list[str] = [], exclusions: list[str] = [], cwd=os.getcwd()):
    log_msg = f"Running rsync from {source.as_posix()} to {destination.as_posix()}"
    if len(options) == 1:
        log_msg += f" with option {options[0]}"
    elif len(options) > 1:
        log_msg += f" with options {', '.join(options)}"
    exclusion_command = []
    if len(exclusions) > 0:
        if len(exclusions) == 1:
            log_msg += f" excluding {exclusions[0]}"
        else:
            log_msg += f" excluding {', '.join(exclusions)}"

        exclusion_command = [f'--exclude="{exclusion}"' for exclusion in exclusions]

    logging.info(log_msg)
    command_list = [
        "rsync",
        *options,
        wrap_in_double_quotes(str(source) + "/"),
        wrap_in_double_quotes(str(destination) + "/"),
        *exclusion_command,
    ]
    command = " ".join(command_list)
    logging.info("Command ran: '" + command + "'")
    output = subprocess.run(command, cwd=cwd, shell=True, capture_output=True)
    logging.debug("Rsync output: " + output.stdout.decode())
    if output.stderr:
        logging.error("Rsync error: " + output.stderr.decode())
    if output.returncode != 0:
        raise Exception("Rsync failed")
