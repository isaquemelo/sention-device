from modules.loading_handler.ISensor import ISensor

from machine import Pin, ADC


class AnalogicSensor(ISensor):
    def __init__(self, port):
        adc = ADC(Pin(port))
        adc.atten(ADC.ATTN_11DB)
        self.port = adc

    def get_data(self):
        return {"value": self.port.read()}
