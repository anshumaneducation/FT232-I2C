from pyftdi.i2c import I2cController
import time

i2c = I2cController()

try:
    while True: 
        i2c.configure('ftdi://ftdi:232h/1')

        # Specify the I2C address of the PCF8591
        pcf_address = 0x48

        # Command to select the DAC output register
        dac_cmd = 0x40

        # Value to set the DAC to maximum voltage (2.5V)
        dac_max_voltage = 0xFF

        # Write maximum voltage (2.5V) to the DAC
        i2c.write(pcf_address, [dac_cmd, dac_max_voltage])
        print("Setting DAC output to maximum voltage (2.5V)")

        # Wait for 3 seconds
        time.sleep(3)

        # Value to set the DAC to half voltage (1.25V)
        dac_half_voltage = 0x7F

        # Write half voltage (1.25V) to the DAC
        i2c.write(pcf_address, [dac_cmd, dac_half_voltage])
        print("Setting DAC output to half voltage (1.25V)")

        # Wait for 3 seconds
        time.sleep(3)

except Exception as e:
    print("Error:", e)

finally:
    # Release the I2C bus
    i2c.terminate()
