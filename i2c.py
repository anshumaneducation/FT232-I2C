import time
from pyftdi.i2c import I2cController, I2cNackError

# Define MMA8451 I2C address
MMA8451_ADDRESS = 0x1d

# Register addresses
REG_OUT_X_MSB = 0x01
REG_OUT_Y_MSB = 0x03
REG_OUT_Z_MSB = 0x05
REG_CTRL_REG1 = 0x2A
REG_WHOAMI = 0x0D

# Function to convert raw data to g-forces (assuming 14-bit data)
def convert_to_g(data):
    value = data >> 2  # Convert to 14-bit value
    if value & (1 << 13):  # Check if negative number
        value -= (1 << 14)
    g_force_value = value / (1 << 11)  # Assuming 1g = 2^11 counts
    return g_force_value

# Function to initialize the MMA8451
def initialize_mma8451(slave):
    # Check WHOAMI register
    whoami = slave.exchange([REG_WHOAMI], 1)[0]
    if whoami != 0x1A:
        raise RuntimeError(f"Unexpected WHOAMI value: {whoami}")

    # Set the device to active mode (bit 0 of CTRL_REG1 to 1)
    ctrl_reg1 = slave.exchange([REG_CTRL_REG1], 1)[0]
    slave.write([REG_CTRL_REG1, ctrl_reg1 | 0x01])
    # Give the device time to power up
    time.sleep(0.1)

# Initialize FTDI I2C controller
i2c = I2cController()
i2c.configure("ftdi://ftdi:232h/1")

# Get the I2C port for the MMA8451
slave = i2c.get_port(MMA8451_ADDRESS)

# Initialize the MMA8451
initialize_mma8451(slave)

try:
    while True:
        # Read data from registers
        data_x = slave.exchange([REG_OUT_X_MSB], 2)
        data_y = slave.exchange([REG_OUT_Y_MSB], 2)
        data_z = slave.exchange([REG_OUT_Z_MSB], 2)

        # Combine high and low bytes and convert to g-forces
        x_raw = (data_x[0] << 8) | data_x[1]
        y_raw = (data_y[0] << 8) | data_y[1]
        z_raw = (data_z[0] << 8) | data_z[1]

        x_g = convert_to_g(x_raw)
        y_g = convert_to_g(y_raw)
        z_g = convert_to_g(z_raw)

        # Print the data
        print(f"X-axis acceleration: {x_g:.2f}g")
        print(f"Y-axis acceleration: {y_g:.2f}g")
        print(f"Z-axis acceleration: {z_g:.2f}g")

        # Add a delay
        time.sleep(2)  # Read every 0.1 seconds (adjust as needed)
except KeyboardInterrupt:
    pass
except I2cNackError as e:
    print(f"I2C communication error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
