from modules.network.main import connect_to_wifi, start_wifi_network, stop_wifi_network, test_internet_connection
from time import sleep

# start_wifi_network()
# connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")
connected = connect_to_wifi("Facil", "12345678a")

if(connected):
    test_internet_connection()

sleep(60)
# stop_wifi_network()
# sleep(30)
