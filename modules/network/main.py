import network
from constants import DEFAULT_AP_STATION_NAME, DEFAULT_AP_STATION_PASS

ap = network.WLAN(network.AP_IF)


def start_wifi_network(ssid=DEFAULT_AP_STATION_NAME, password=DEFAULT_AP_STATION_PASS):
    ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK,
              password=password, max_clients=5)

    ap.active(True)


def stop_wifi_network():
    ap.active(False)


def get_ap_instance():
    return ap
