from modules.loading_handler.ISensor import ISensor

from machine import Pin

class DigitalSensor(ISensor):
    def __init__(self, port):
        self.port = Pin(port, Pin.IN)

    def get_data(self):
        return {"value": self.port.value()}