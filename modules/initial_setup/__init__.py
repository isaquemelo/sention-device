from modules.network import start_wifi_network
from modules.server import start_api


def initial_setup():
    # Creates a wifi network to expose the API
    start_wifi_network()

    # Start server to provide API
    # The API will save all the required data inside the KVS
    start_api()
