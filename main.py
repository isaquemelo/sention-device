from constants import CREATE_NEW_DEVICE_URL
import libs.request as request
from modules.loading_handler import get_user_preferences, setup_pins_and_imports
from modules.network import connect_to_wifi, start_wifi_network, stop_wifi_network, test_internet_connection
from time import sleep

from modules.server import start_api
# from modules.storage import KeyValueStorage

user_preferences = get_user_preferences("285cc101-e76e-4a5e-b69f-e8fe9e5da73f")
setup_pins_and_imports(user_preferences)

# connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")
#start_wifi_network()
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

#start_api()
