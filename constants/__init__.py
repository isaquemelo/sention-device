DEFAULT_AP_STATION_NAME = "Sention"
DEFAULT_AP_STATION_PASS = "12345678"
TIME_LIMIT_TO_CONNECT_TO_WIFI = 20000  # in milliseconds
TESTING_INTERNET_SITE = "https://www.google.com/"
KVS_FILE_NAME = "store.json"
KVS_FILE_PATH = "storage/"
SENTION_API_BASE_URL = "http://192.168.18.5:8080"
# SENTION_API_BASE_URL = "http://192.168.50.64:8080"
CREATE_NEW_DEVICE_URL = f"{SENTION_API_BASE_URL }/devices/"
AUTH_USER_URL = f"{SENTION_API_BASE_URL}/auth/user/"
ASSOCIATE_DEVICE_USER_URL = f"{SENTION_API_BASE_URL}/user/devices/associate"
GET_DEVICE_URL = f"{SENTION_API_BASE_URL}/user/devices/"
POST_SENSOR_DATA_URL = f"{SENTION_API_BASE_URL}/user/devices/sensors/sensorId/data"
