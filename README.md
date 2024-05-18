# FT232-I2C
All required things to work ft232 for i2c


# Using FT232H to Control I2C

## Checking FTDI Device Compatibility

To ensure compatibility with the `pylibftdi` library for Python, follow these steps:

1. Open **Device Manager** on your computer.
2. Locate **libusbK USB Devices** in the list.
3. Verify that your FT232 device is listed under **libusbK USB Devices**.

## Converting Driver with Zadig

If your FT232 device is not listed under **libusbK USB Devices**, you will need to convert its driver using Zadig software:

1. Download and open Zadig from [here](https://zadig.akeo.ie/).
2. In Zadig, select your FT232 device from the dropdown menu.
3. Choose the `libusbK` driver from the list of available drivers.
4. Click the `Install Driver` button to convert the current driver to `libusbK`.

## Installing pyftdi

To use the FT232H for I2C and SPI communication, you need to install the `pyftdi` library. Run the following command in your terminal:

```sh
pip3 install pyftdi
## Table of Experiments

| Exp No | Name of Experiment            | Libraries  | Program File Name            |
|--------|-------------------------------|------------|------------------------------|
| 1      | Ledblink                      | pylibftdi  | Ledblink.py                  |
| 2      | I2C Scan                      | pylibftdi  | I2cScan.py                   |
| 3      | Accelerometer (MMA8451)       | pylibftdi  | i2c.py                       |
| 4      | Read ADC Single Channel       | pylibftdi  | pcf8591_1channel.py          |
| 5      | Read ADC 4 Channel            | pylibftdi  | pcf8591_4channel.py          |
| 6      | Write to DAC                  | pylibftdi  | Dac.py                       |

