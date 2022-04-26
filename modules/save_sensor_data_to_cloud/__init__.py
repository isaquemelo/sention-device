
import json
import libs.request as request
from constants import POST_SENSOR_DATA_URL
from modules.storage import get_kvs


def save_sensor_data_to_cloud(sensor_id, sensor_data):
    kvs = get_kvs()
    auth_token = kvs.get("AUTH_TOKEN")
    response = request.post(POST_SENSOR_DATA_URL.replace("sensorId", sensor_id), data=json.dumps(sensor_data), headers={'content-type': 'application/json', 'Authorization': auth_token})
    return response.json()