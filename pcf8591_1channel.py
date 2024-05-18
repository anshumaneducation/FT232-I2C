
from pyftdi.i2c import I2cController
import time
i2c = I2cController()

try:
    while True: 
        i2c.configure('ftdi://ftdi:232h/1')

        # Specify the I2C address of the PCF8591 ADC
        adc_address = 0x48
        channel_0_cmd = 0x44
        i2c.write(adc_address, [channel_0_cmd])
        data = i2c.read(adc_address,4)
        print(len(data))
        analog_value1 = data[0]
        analog_value2 = data[1]
        analog_value3 = data[2]
        analog_value4 = data[3]
        reference_voltage = 3.3 
        ## put out value max  to be 256-1 8 bit adc
        adc_value_take=(2<<7 )-1
 
        voltage = analog_value1 /(adc_value_take) * reference_voltage
        print("Voltage (V):", voltage)
        voltage = analog_value2 /(adc_value_take) * reference_voltage
        print("Voltage (V):", voltage)
        voltage = analog_value3 /(adc_value_take) * reference_voltage
        print("Voltage (V):", voltage)
        voltage = analog_value4 /(adc_value_take) * reference_voltage
        print("Voltage (V):", voltage)
        time.sleep(2)

except Exception as e:
    print("Error:", e)

finally:
    # Release the I2C bus
    i2c.terminate()
