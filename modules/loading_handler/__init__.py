from constants import GET_DEVICE_URL
import libs.request as request
import libs.ulogging as logging
import libs.picoweb as picoweb
from modules.loading_handler.DigitalActuator import DigitalActuator

from modules.network import connect_to_wifi
from modules.auth import generate_token

from modules.storage import get_kvs

def get_user_preferences(deviceId):

    connect_to_wifi("ERICK_PIMENTEL", "6B896DBDE2")

    #kvs = get_kvs()
    #auth_token = kvs.get("AUTH_TOKEN")
    auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImJlYjA0YjlhLTk0ZTAtNDU5NC05MDUzLTdlZDllMzliN2ZhZCIsImlhdCI6MTY1MDY2ODg1OCwiZXhwIjoxNjUxOTY0ODU4fQ.jBVb4PKiO-jrjTZ8DOCCn34u_1GEHGx-fWFqLtAiqXE"
    
    response = request.get(GET_DEVICE_URL + deviceId, headers={'Authorization': auth_token})
    print(response.json())
    return response.json()

def setup_pins_and_imports(user_preferences):

    sensors = user_preferences["sensors"]
    actuators = user_preferences["actuators"]

    
    for actuator in actuators:
        port = actuator["port"]
        triggers = actuator["triggers"]
        actuator_instance = DigitalActuator(port, triggers)
        actuator_instance.execute_triggers(100)
    

    return False