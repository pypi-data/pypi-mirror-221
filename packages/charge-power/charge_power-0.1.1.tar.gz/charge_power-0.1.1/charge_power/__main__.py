"""Print current wattage of charge/discharge"""
from __future__ import annotations

import itertools
import os
import sys
from pathlib import Path

import click
from rich.console import Console

from charge_power import __version__ as version
from charge_power.charge import print_battery_charge


_CHARGE_COEFF = 0.00001139850942569049  # coefficient to multiply current_charge value to get Watts


@click.command("print_wattage")
@click.version_option(version)
@click.option("--delay", "-d", type=int, default=30, help="Delay between measurements in seconds", show_default=True)
@click.option(
    "--number", "-n", type=int, default=None, help="Number of measurements before stop", show_default="(unlimited)"
)
@click.option("--log-file", "-l", type=click.Path(dir_okay=False), default=None, help="Path to a file to log output")
@click.argument(
    "battery_path", type=click.Path(exists=True, file_okay=False), default=None, metavar="BATTERY_PATH", required=False
)
def main(delay: int, number: int | None, log_file: str | None, battery_path: str | None):
    """
    Show power usage of the given battery.

    Single argument may be used to set exact battery directory. If not given, will try to find it automatically.
    """
    console = Console(highlight=False, emoji=False)
    if battery_path is None:
        options = list(Path("/sys/class/power_supply").glob("BAT*"))
        if len(options) == 0:
            console.print("[red]No batteries found at [b]/sys/class/power_supply[/b], exiting[/red]")
            sys.exit(1)
        elif len(options) > 1:
            console.print(f"[yellow]More than one battery found, using [b]{options[0]}[/yellow b]")
        battery_path = options[0]

    battery_dir = Path(battery_path)
    if not battery_path.exists() or not battery_path.is_dir():
        console.print(f"[red]Battery path [b]{battery_dir}[/b] does not exist or not a directory, exiting[/red]")
        sys.exit(1)

    rng = itertools.cycle((True,)) if number is None else range(number)
    full_wattage = int((battery_dir / "charge_full").read_text()) * _CHARGE_COEFF

    def get_charge() -> int:
        """Get current battery charge status in Watts"""
        return int((battery_dir / "charge_now").read_text()) * _CHARGE_COEFF

    logfile = None
    current_charge = get_charge()
    if log_file is not None:
        try:
            logfile = open(log_file, "a", encoding="utf-8")  # pylint: disable=consider-using-with
            print(
                f"Starting to print charge change (delay={delay}, number={number})."
                f" Current charge is {current_charge:.2f}Wh",
                file=logfile,
            )
        except Exception as exc:  # pylint: disable=broad-except
            console.print(f"[red]Could not open file [i]{log_file}[/i] to log data[/red]: {exc!r}")
            sys.exit(1)

    console.print(
        f"Starting to print charge change [dim](delay={delay}, number={number})[/dim]."
        f" Current charge is [green]{current_charge:.2f}[/green]Wh"
    )
    try:
        print_battery_charge(get_charge, full_wattage, delay, rng, console, logfile)
    except KeyboardInterrupt:
        print("Finishing by Ctrl+C hit")
    finally:
        if logfile is not None:
            try:
                logfile.close()
            except Exception as exc:  # pylint: disable=broad-except
                console.print(f"[red]Could not close log file [i]{log_file}[/red]: {exc!r}")


if __name__ == "__main__":
    if os.name != "posix":
        print("This utility works only with linux systems")
        sys.exit(1)
    main()  # pylint: disable=no-value-for-parameter
