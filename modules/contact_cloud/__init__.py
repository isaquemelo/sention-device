
import json
from constants import POST_SENSOR_DATA_BULK_URL
import libs.request as request
from modules.storage import get_kvs
import _thread

def _content(body, auth_token):
    response = request.post(POST_SENSOR_DATA_BULK_URL, data=json.dumps(body), headers={'content-type': 'application/json', 'Authorization': auth_token})
    return response.json()

def save_sensor_data_to_cloud(list_sensors_data):
    kvs = get_kvs()
    auth_token = kvs.get("AUTH_TOKEN")
    body = {"data": list_sensors_data}
    _thread.start_new_thread(_content, (body, auth_token))