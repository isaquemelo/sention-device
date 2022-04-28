import machine
from modules.manager import managing
from modules.storage import get_kvs

machine.freq(240000000)
print(machine.freq())

# start_wifi_network()
# connected = connect_to_wifi("PROXXIMA_206415-2.4G", "nazareno")

# has_connection = test_internet_connection()

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


# def start_api_background():
#     print("start_api after")
#     start_api()


# _thread.start_new_thread(start_api_background, ())
# print("after thread")
# sleep(30)
# stop_api()
# print("fim loop cabo")
kvs = get_kvs()
# kvs.set('USER_LOGIN', 'isaquegbmelo2@gmail.com')
# kvs.set('USER_PASSWORD', 'tester')
# kvs.set('DEVICE_ID', '7aeaa7ac-3769-40ed-b36a-4ed70f15c272')
# kvs.set('ACCESS_CODE', 'h3g8IllYv')
# kvs.set('USER_ID', '8e18c316-1e2c-48fe-8079-16e54d27e244')
kvs.set('CONFIGURED', True)
managing()
