<p align="center">
    <img src="https://img.shields.io/badge/language-Python3-%23f34b7d.svg?style=for-the-badge" alt="Python3">
    <img src="https://img.shields.io/badge/tool type-HDL debugging support-red?style=for-the-badge" alt="tool">
    <img src="https://img.shields.io/badge/Licence-GPL--3.0-0078d7.svg?style=for-the-badge" alt="GPL-3.0">
</p>

# VCDcompare

As part of the development of a module replacing another module in a complete system designed to run on an FPGA (Field Programmable Gate Array) board , we are checking functional behavior using the Verilator HDL simulator.

The new module does not respect the same timing constraint as the previous one, and in order to help with debugging, we have made this tool to compare two vcd traces without taking timings into account. The script compares hard-coded signals with value changes. All differences are then logged in an output file.

## Dev Setup

- Ubuntu 22.04
- python 3.10.12
- pip 22.0.2
- input uses vcd files generated with Verilator 5.002

## Getting Started
Install dependencies:
```bash
pip3 install -r requirements.txt    
```
Fill input files and signals to be checked:

| type            | variable in python file |
|-----------------|-------------------------|
| vcd file 1      | ```vcdF1```             |
| vcd file 2      | ```vcdF2```             |
| list of signals | ```signals```           |

Run the app:
```bash
python3 VCDcompare.py
```

It writes on a message.log file all the difference between changes of aimed signals from two vcd files

# in construction...
  

