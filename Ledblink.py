import time
from pylibftdi import BitBangDevice

with BitBangDevice() as bb:
    print("BitBangDevice initialized")
    while True:
        bb.port = 128
        print("LED ON")
        time.sleep(2)
        bb.port = 0
        print("LED OFF")
        time.sleep(1)
