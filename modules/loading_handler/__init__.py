from constants import GET_DEVICE_URL
import libs.request as request
import libs.ulogging as logging
import libs.picoweb as picoweb

from modules.network import connect_to_wifi
from modules.auth import generate_token
from machine import Pin

from modules.loading_handler.DigitalActuator import DigitalActuator
from modules.loading_handler.sensor_classes import sensor_classes

from time import sleep
import _thread

from modules.storage import get_kvs


def loading_module():
    kvs = get_kvs()
    device_id = kvs.get("DEVICE_ID")

    user_preferences = get_user_preferences(device_id)
    return setup_pins_and_imports(user_preferences)


def get_user_preferences(device_id):
    kvs = get_kvs()
    auth_token = kvs.get("AUTH_TOKEN")

    response = request.get(GET_DEVICE_URL + device_id,
                           headers={'Authorization': auth_token})

    try:
        preferences = response.json()
    except Exception:
        preferences = False

    return preferences


def display_sensor_readings(sensors_instance):
    while True:
        for key, value in sensors_instance.items():
            print(key, '->', value.get_data())
        sleep(2)


def setup_pins_and_imports(user_preferences):
    sensors = user_preferences["sensors"]
    actuators = user_preferences["actuators"]

    sensors_instance = {}
    for sensor in sensors:
        sensor_id = sensor["id"]
        sensor_type = sensor["type"]
        sensor_port = sensor["port"]

        sensor_instance = sensor_classes[sensor_type](sensor_port)
        sensors_instance[sensor_id] = sensor_instance

    actuators_instance = {}
    for actuator in actuators:
        actuator_id = actuator["id"]
        actuator_port = actuator["port"]
        actuator_triggers = actuator["triggers"]

        actuator_instance = DigitalActuator(actuator_port, actuator_triggers)
        actuators_instance[actuator_id] = actuator_instance

    #for key, value in actuators_instance.items(): print(key, '->', value.port, value.triggers)

    return sensors_instance, actuators_instance
