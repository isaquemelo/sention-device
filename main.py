from constants import CREATE_NEW_DEVICE_URL
import libs.request as request
from modules.loading_handler import get_user_preferences, loading_module, setup_pins_and_imports
from modules.network import connect_to_wifi, start_wifi_network, stop_wifi_network, test_internet_connection
from time import sleep
from modules.save_sensor_data_to_cloud import save_sensor_data_to_cloud

from modules.server import start_api
from modules.storage import get_kvs
import _thread


# start_wifi_network()
connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")

has_connection = test_internet_connection()

# connected = connect_to_wifi("ERICK_PIMENTEL", "6B896DBDE2")
# kvs = get_kvs()
# kvs.wipe()
# print(kvs.get_store())

# (sensors, actuators) = loading_module()

# while True:
#     # print("while")
#     for actuator_id, actuator in actuators.items():
#         actuator.execute_triggers(sensors)
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

# start_api()
