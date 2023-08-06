import time
import struct
from adafruit_bus_device import i2c_device
from micropython import const

try:
    from typing import Tuple
    from busio import I2C
except ImportError:
    pass

_SM8436_DEFAULT_ADDR = const(0x6d)  # SM8436 I2C Address

class SM8436:

    def __init__(self, i2c_bus: I2C, address: int = _SM8436_DEFAULT_ADDR) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)
        self._buffer = bytearray(9)
        
    @property
    def differential_pressure(self) -> float:
        """The current differential pressure in ..."""
        return self.measurements[1]

    @property
    def temperature(self) -> float:
        """The current temperature in degrees Celsius"""
        return self.measurements[0]
        
    @property
    def measurements(self) -> Tuple[float, float]:
        """both `temperature` and `relative_humidity`, read simultaneously"""

        pressure = None
        command = 0x2E

        with self.i2c_device as i2c:
            self._buffer[0] = command
            i2c.write(self._buffer, end=1)
            time.sleep(0.01)
            i2c.readinto(self._buffer)

        # separate the read data
        temp_data = self._buffer[0:2]
        press_data = self._buffer[2:4]
        stat = self._buffer[4:6]
        stat_sync = self._buffer[6:8]
        crc = self._buffer[4]
        
        # decode data into human values:
        # convert bytes into 16-bit signed integer
        # convert the LSB value to a human value according to the datasheet
        p_min = -20
        p_max = 500
        digital_min = -26215
        digital_max = 26214
        p = struct.unpack_from("<h", press_data)[0]
        pressure = p_min+((p-digital_min)/(digital_max-digital_min))*(p_max-p_min)
        
        t = struct.unpack_from("<h", temp_data)[0]
        b_0 = -16881
        b_1 = 397.2
        temperature = (t-b_0)/b_1

        return (temperature, pressure)
