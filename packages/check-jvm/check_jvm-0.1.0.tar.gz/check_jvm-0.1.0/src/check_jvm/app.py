# -*- coding: utf-8 -*-

"""Check-JVM CLI application."""

# MIT License (see LICENSE)
# Author: Dániel Hagyárossy <d.hagyarossy@sapstar.eu>

import logging
import os
import platform
import json
import re
import timeit
from typing import Dict, List, Optional
from typing_extensions import Annotated
import typer
import subprocess

from sys import __stdin__ as stdin, stdout
from enum import Enum

from rich import box
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from rich.align import Align
from rich.status import Status

from check_jvm.java_version import JavaExecutable


class ResultType(str, Enum):
    csv = "csv"


log = logging.getLogger(__name__)
exec_name = "java"
app = typer.Typer()
scan_status = None


def get_java_files(exec_name: str = "java") -> List[Optional[str]]:
    files = []
    tl_dir = ""
    for dirpath, _, filenames in os.walk("/"):
        os_path = dirpath.split(os.sep)
        if tl_dir != f"{os_path[0]}{os.sep}{os_path[1]}":
            tl_dir = f"{os_path[0]}{os.sep}{os_path[1]}"
            log.info(f"Processing '{tl_dir}'")
            if scan_status:
                scan_status.update(
                    f"Scanning [green]'{tl_dir}'[/] for JAVA files. "
                    "This could take a while, please wait...",
                )

        for file in filenames:
            if file == exec_name:
                pathname = os.path.join(dirpath, file)
                if os.access(pathname, os.X_OK) and not os.path.islink(
                    pathname
                ):
                    log.info("Found: '%s'", pathname)
                    files.append(os.path.join(dirpath, file))
    log.debug(f"'get_java_files' result: {files}")
    return files


def check_version(file: Optional[str] = ""):
    log.info(f"Checking '{file}'")
    try:
        java_out = subprocess.run(
            [file, "-XshowSettings:properties", "-version"],
            capture_output=True,
        )
    except FileNotFoundError as e:
        if log:
            log.warning("Unable to execute '%s' (File not found)", e.filename)
        return

    java = JavaExecutable(java_out.stderr)
    return java


def process_versions() -> Dict[str, JavaExecutable]:
    jvm_details = {}
    for file in get_java_files(exec_name):
        java = check_version(file)
        jvm_details.update({file: java})
    return jvm_details


def interactive(
    verbose: bool, debug: bool, show_all: bool, result: ResultType
):
    global scan_status
    console = Console()
    log_level = "WARNING"
    if verbose:
        log_level = "INFO"
    if debug:
        log_level = "DEBUG"

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console)],
    )
    console.clear()

    table = Table(box=box.ROUNDED, expand=True, show_lines=True)

    table.add_column(
        "Status", justify="center", vertical="middle", no_wrap=True
    )
    table.add_column(
        "Version", justify="center", vertical="middle", no_wrap=True
    )
    table.add_column(
        "Vendor", justify="center", vertical="middle", no_wrap=True
    )
    table.add_column("Location", justify="left", vertical="middle")
    if verbose:
        table.add_column("Version Output", justify="left", vertical="middle")

    log.info("OS: '%s'", platform.system())
    scan_status = Status(
        "Scanning the filesystem for all available JAVA files. "
        "This could take a while, please wait...",
        console=console,
    )
    with scan_status:
        java_versions = process_versions()
        for file, jvm in java_versions.items():
            log.info(
                f"JVM details of '{file}':\n  "
                f"Status: {jvm.status}\n  "
                f"Vendor: {jvm.vendor}\n  "
                f"Version: {jvm.version}"
            )
            if result and result.value == "csv":
                console.log(f"{jvm.status};{jvm.version};{jvm.vendor};{file}")
                continue

            status = "[bold yellow]??[/]"
            if jvm.status == "KO":
                status = "[bold red]KO[/]"
            if jvm.status == "OK":
                status = "[bold green]OK[/][green]:heavy_check_mark:[/]"
            if jvm.status == "KO" or show_all:
                if verbose:
                    table.add_row(
                        status,
                        jvm.version,
                        jvm.vendor,
                        file,
                        jvm.raw_version,
                    )
                else:
                    table.add_row(
                        status,
                        jvm.version,
                        jvm.vendor,
                        file,
                    )

    if not result:
        console.print(table)


def non_interactive(show_all: bool):
    java_versions = process_versions()
    for file, jvm in java_versions.items():
        if jvm.status == "KO" or show_all:
            print(f"{jvm.status};{jvm.version};{jvm.vendor};{file}")


@app.command()
def main(
    show_all: Annotated[
        bool, typer.Option("--all", help="Show all JAVA versions.")
    ] = False,
    result: Annotated[
        ResultType,
        typer.Option("--result", "-r", help="Set the output to CSV."),
    ] = None,
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Verbose output.")
    ] = False,
    debug: Annotated[
        bool, typer.Option("--debug", "-d", help="Enable debug output.")
    ] = False,
):
    global exec_name
    global stdin
    global stdout

    if platform.system() == "Windows":
        exec_name = "java.exe"

    start = timeit.default_timer()
    print("The start time is :", start)

    # https://stackoverflow.com/questions/44780476/windows-cmd-piping-python-3-5-py-file-results-works-but-pyinstaller-exes-leads
    if stdout.isatty():
        stdout = open(stdout.fileno(), "w", encoding="utf-8", closefd=False)
        interactive(verbose, debug, show_all, result)
    else:
        non_interactive(show_all=show_all)
    print("The difference of time is :", timeit.default_timer() - start)
