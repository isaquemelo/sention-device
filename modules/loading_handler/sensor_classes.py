from modules.loading_handler.AnalogicSensor import AnalogicSensor
from modules.loading_handler.BMP280Sensor import BMP280Sensor
from modules.loading_handler.DigitalSensor import DigitalSensor


sensor_classes = {
    "BMP280": BMP280Sensor,
    "ANALOGIC": AnalogicSensor,
    "DIGITAL": DigitalSensor
}