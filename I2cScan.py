from pyftdi.i2c import I2cController, I2cNackError

# Replace with the actual I2C slave device address from its datasheet

def detect_i2c_device( ):

    try:
        # Create an I2C controller instance
        i2c = I2cController()
        start_address=0
        end_address=127
        # Configure the I2C interface (replace with your specific FT232 info)
        i2c.configure(f"ftdi://ftdi:232h/1")  # Adjust bus number
        for address in range(128):
            try:
                # Write a single byte (e.g., 0x00) to the current address
                i2c.write(address,"Hello".encode('utf-8'))

                # Read a single byte from the current address
                data = i2c.read(address, 1)

                # Check if data was read successfully (length should be 1)
                if len(data) == 1:
                    print(f"I2C device detected at address: {hex(address)}")
                      # Exit the loop if a device is found

            except I2cNackError as e:
                # No device acknowledged at this address, continue scanning
                pass


        for address in range(start_address, end_address + 1):
            try:
                # Attempt to read a byte from the address
                i2c.get_port(address).read()
                # If no error is raised, a device acknowledged and likely exists
                print(f"I2C device detected at address: {hex(address)}")
                return True
            except I2cNackError as e:
                pass  # No device at this address

        # No device found in the specified range
        return False

    except Exception as e:
        print(f"Error during I2C detection: {e}")
        return False

# Example usage (replace 0 with the appropriate I2C bus number)
if detect_i2c_device():
    print("I2C device detected!")
else:
    print("No I2C device found.")



