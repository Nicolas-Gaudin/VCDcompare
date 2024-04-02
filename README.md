# VCDcompare

## my setup

- Ubuntu 22.04
- python 3.10.12
- pip 22.0.2

## Getting Started
Install dependencies:
```bash
pip3 install -r requirements.txt    
```
Run the app:
```bash
python3 VCDcompare.py
```
Tap your memory address in hexadecimal format.

Example :
If your address is ```0x0054 3210``` , tap ```543210``` in the field.

## Considered cache configuration

| Parameter                     | #  |
|-------------------------------|----|
| Address width                 | 22 |
| Number of set                 | 16 |
| Number of word per cache line | 4  |

## Next upgrades 

- Ask user his cache config and address width
  

