from pyftdi.i2c import I2cController
import time

# Initialize the I2C controller
i2c = I2cController()
i2c.configure('ftdi://ftdi:232h/1')

# Specify the I2C address of the PCF8591 ADC
adc_address = 0x48

# Commands to start reading from channels 0 to 3
channel_cmds = [ 0x41, 0x42, 0x43,0x44]

# Define reference voltage (in volts)
reference_voltage = 3.3

# Maximum value for 8-bit ADC
adc_value_max = 255

try:
    while True:
        for channel, cmd in enumerate(channel_cmds):
            # Write command to select the channel
            i2c.write(adc_address, bytes([cmd]))

            # Add a small delay to allow the ADC to stabilize after switching channels
            time.sleep(0.1)  # 10 ms delay

            # Read one byte of data from the ADC
            data = i2c.read(adc_address, 1)

            # Convert the received byte to an integer (0-255)
            analog_value = data[0]

            # Calculate voltage using the formula: voltage = (analog_value / adc_value_max) * reference_voltage
            voltage = (analog_value / adc_value_max) * reference_voltage

            print(f"Voltage (V) - Channel {channel}:", voltage)

        time.sleep(0.2)

except Exception as e:
    print("Error:", e)

finally:
    # Release the I2C bus
    i2c.terminate()

