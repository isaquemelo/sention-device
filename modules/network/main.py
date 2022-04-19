import helpers.urequest as requests
import network
import time

from constants import DEFAULT_AP_STATION_NAME, DEFAULT_AP_STATION_PASS, TESTING_INTERNET_SITE, TIME_LIMIT_TO_CONNECT_TO_WIFI

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

        start = time.ticks_ms()

        while not sta_if.isconnected():
            delta = time.ticks_diff(time.ticks_ms(), start)

            if(delta > TIME_LIMIT_TO_CONNECT_TO_WIFI):
                print('Failed to connect to provided Wi-Fi network')
                return False

            pass

    print('Conected to Wi-Fi network')
    print(sta_if.ifconfig())
    return True


def test_internet_connection():
    print("Testing internet connection")

    try:
        response = requests.get(url=TESTING_INTERNET_SITE)
    except OSError:
        print("Failed to connect to internet")
        return False

    if (len(response.content)):
        print("Success connecting to internet")
        return True
