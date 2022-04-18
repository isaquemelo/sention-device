from modules.network.main import connect_to_wifi, start_wifi_network, stop_wifi_network
from time import sleep

start_wifi_network()
connect_to_wifi("Facil", "12345678a")
sleep(30)
stop_wifi_network()
sleep(30)
