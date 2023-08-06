# charge-power

A small utility to track power consumed or provided to the device battery.

## Installation

One can install the module via __pipx__:
- `pipx install charge-power`
- `pipx install git+https://github.com/kanootoko/charge-power.git`

## Work principals

By default, searches for battery directory in __/sys/class/power_supply__. Uses __charge_now__ and __charge_full__
  files to get current and max chagre level.

Then the measurements are taken from __charge_now__ file by timer by given delay time. Difference between
  is the amount of energy consumed/provided to the battery, and it is displayed to the console (and log file if it
  is set).
