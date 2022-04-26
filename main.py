from constants import CREATE_NEW_DEVICE_URL
import libs.request as request
from modules.loading_handler import get_user_preferences, loading_module, setup_pins_and_imports
from modules.network import connect_to_wifi, start_wifi_network, stop_wifi_network, test_internet_connection
from time import sleep
from modules.contact_cloud import save_sensor_data_to_cloud

from modules.server import start_api, stop_api
from modules.storage import get_kvs
import _thread


# start_wifi_network()
#connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")

connected = connect_to_wifi("ERICK_PIMENTEL", "6B896DBDE2")

# kvs = get_kvs()
# kvs.wipe()
# print(kvs.get_store())

#(sensors, actuators) = loading_module()

list_sensors_data = [
		{
			"id": "302c0573-149c-492a-8711-9d1a18438f85",
			"data": -123
		}, 
		{
			"id": "48e86d3a-53e5-48e2-ae64-15f9f9a62ee8",
			"data": {
					"TEMPERATURE": 123,
					"PRESSURE": 321,
					"ALTITUDE": 123
			}
		}
	]

save_sensor_data_to_cloud(list_sensors_data)

# (sensors, actuators) = loading_module()

# while True:
#     # print("while")
#     for actuator_id, actuator in actuators.items():
#         actuator.execute_triggers(sensors)
    # sleep(1)
# sleep(1)
# connected = connect_to_wifi("Facil", "12345678a")

# if(connected):
#     test_internet_connection()

# kvs = KeyValueStorage()
# kvs.wipe()
# print(kvs.get_store())
# kvs.set('ssid', 'Nome da rede')
# kvs.set('password', 'Senha da rede')
# print(kvs.get_store())
# print(kvs.get('password'))

# sleep(60)
# stop_wifi_network()
# sleep(30)


# def start_api_background():
#     print("start_api after")
#     start_api()


# _thread.start_new_thread(start_api_background, ())
# print("after thread")
# sleep(30)
# stop_api()
# print("fim loop cabo")
