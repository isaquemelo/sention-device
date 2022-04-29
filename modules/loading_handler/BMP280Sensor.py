from modules.loading_handler.ISensor import ISensor

from machine import Pin, I2C
from libs.BMP280 import BMP280


class BMP280Sensor(ISensor):
    def __init__(self, ports):
        # remember to change "SLK and SDL" to "slc and sda"
        bmp_bus = I2C(0, scl=Pin(ports["SLC"]), sda=Pin(ports["SDA"]))
        self.bmp = BMP280(bmp_bus)

    def get_data(self, dataSource=False):
        data = {}

        try:
            data["TEMPERATURE"] = self.bmp.getTemp()
            data["PRESSURE"] = self.bmp.getPress()
            data["ALTITUDE"] = self.bmp.getAltitude()
        except:
            data = {
                "TEMPERATURE": 0,
                "PRESSURE": 0,
                "ALTITUDE": 0,
            }

        return data[dataSource] if dataSource else data
