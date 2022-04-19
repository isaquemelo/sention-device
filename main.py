from modules.network import connect_to_wifi, start_wifi_network, stop_wifi_network, test_internet_connection
from time import sleep

from modules.server import app
from modules.storage import KeyValueStorage


# start_wifi_network()
# connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")
# connected = connect_to_wifi("Facil", "12345678a")

# if(connected):
#     test_internet_connection()

# app()
# sleep(60)
# stop_wifi_network()
# sleep(30)

# kvs = KeyValueStorage()
# kvs.wipe()
# print(kvs.get_store())
# kvs.set('ssid', 'Nome da rede')
# kvs.set('password', 'Senha da rede')
# print(kvs.get_store())
# print(kvs.get('password'))
