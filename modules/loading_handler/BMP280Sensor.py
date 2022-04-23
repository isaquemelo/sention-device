from modules.loading_handler.ISensor import ISensor

from machine import Pin, I2C
from libs.BMP280 import BMP280

class BMP280Class(ISensor):
    def __init__(self, port):
        #remember to change "SLK and SDL" to "slc and sda"
        bmp_bus = I2C(0, scl = Pin(port["SLK"]), sda = Pin(port["SLD"]))
        self.bmp = BMP280(bmp_bus)
        

    def get_data(self):
        data = {}
        data["temp"] = self.bmp.getTemp()
        data["press"] = self.bmp.getPress()
        data["alti"] = self.bmp.getAltitude()

        return data

    