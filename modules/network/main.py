import network
from constants import DEFAULT_AP_STATION_NAME, DEFAULT_AP_STATION_PASS

ap = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)


def start_wifi_network(ssid=DEFAULT_AP_STATION_NAME, password=DEFAULT_AP_STATION_PASS):
    ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK,
              password=password, max_clients=5)

    ap.active(True)
    print("Wi-Fi network started")


def stop_wifi_network():
    print("Wi-Fi network stopped")
    ap.active(False)


def get_ap_instance():
    return ap


def connect_to_wifi(ssid, password):
    if not sta_if.isconnected():
        print('Connecting to Wi-Fi network')

        sta_if.active(True)
        sta_if.connect(ssid, password)

        while not sta_if.isconnected():
            pass
    print('Conected to Wi-Fi network')
