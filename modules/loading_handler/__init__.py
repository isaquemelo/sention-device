from constants import GET_DEVICE_URL
import libs.request as request
import libs.ulogging as logging
import libs.picoweb as picoweb
from modules.loading_handler.DigitalActuator import DigitalActuator
from modules.loading_handler.BMP280Sensor import BMP280Class

from modules.network import connect_to_wifi
from modules.auth import generate_token
from machine import Pin

from time import sleep

from modules.storage import get_kvs

def loading_module():
    user_preferences = get_user_preferences("285cc101-e76e-4a5e-b69f-e8fe9e5da73f")
    setup_pins_and_imports(user_preferences)

def get_user_preferences(device_id):

    connect_to_wifi("ERICK_PIMENTEL", "6B896DBDE2")

    #kvs = get_kvs()
    #auth_token = kvs.get("AUTH_TOKEN")
    auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImJlYjA0YjlhLTk0ZTAtNDU5NC05MDUzLTdlZDllMzliN2ZhZCIsImlhdCI6MTY1MDY2ODg1OCwiZXhwIjoxNjUxOTY0ODU4fQ.jBVb4PKiO-jrjTZ8DOCCn34u_1GEHGx-fWFqLtAiqXE"
    
    response = request.get(GET_DEVICE_URL + device_id, headers={'Authorization': auth_token})
    #print(response.json())
    return response.json()

def setup_pins_and_imports(user_preferences):

    sensors = user_preferences["sensors"]
    actuators = user_preferences["actuators"]

    sensors_instance = {}
    for sensor in sensors:
        sensor_id = sensor["id"]
        sensor_type = sensor["type"]
        sensor_port = sensor["port"]

        sensor_instance = BMP280Class(sensor_port)

        sensors_instance[sensor_id] = sensor_instance


    for key, value in sensors_instance.items(): print(key, '->', value.get_data())



    actuators_instance = {}
    for actuator in actuators:
        actuator_id = actuator["id"]
        actuator_port = actuator["port"]
        actuator_triggers = actuator["triggers"]
        actuator_instance = DigitalActuator(actuator_port, actuator_triggers)
        
        actuators_instance[actuator_id] = actuator_instance

    #for key, value in actuators_instance.items(): print(key, '->', value.port, value.triggers)
        

    

    return False