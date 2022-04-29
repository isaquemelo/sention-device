
import json
from constants import INTERVAL_BETWEEN_SAVING_DATA_TO_CLOUD, POST_SENSOR_DATA_BULK_URL
import libs.request as request
from modules.storage import get_kvs
import _thread
import time
import sys


last_time_called = time.ticks_ms()


def _content(body, auth_token, lock):
    lock.acquire()

    start_time = time.ticks_ms()
    try:
        request.post(POST_SENSOR_DATA_BULK_URL, data=json.dumps(body), headers={
            'content-type': 'application/json', 'Authorization': auth_token}, timeout=5).close()
        print("Sent data to server")
    except:
        print("Error during cocurrent saving data to server")
    finally:
        delta = time.ticks_diff(time.ticks_ms(), start_time)
        # print("response", delta)

        lock.release()
        sys.exit(0)


def save_sensor_data_to_cloud(list_sensors_data, lock):
    global last_time_called
    delta = time.ticks_diff(time.ticks_ms(), last_time_called)

    if(delta < INTERVAL_BETWEEN_SAVING_DATA_TO_CLOUD):
        return False
    else:
        auth_token = get_kvs().get("AUTH_TOKEN")
        body = {"data": list_sensors_data}
        last_time_called = time.ticks_ms()

        _thread.start_new_thread(_content, (body, auth_token, lock))
