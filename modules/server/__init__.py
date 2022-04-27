import json
from time import sleep
import uasyncio
import machine

from constants import ASSOCIATE_DEVICE_USER_URL, CREATE_NEW_DEVICE_URL

import libs.request as request
import libs.ulogging as logging
import libs.picoweb as picoweb

from modules.auth import generate_token
from modules.network import connect_to_wifi
from modules.storage import get_kvs


async def ping(req, resp):
    await picoweb.start_response(resp, content_type="application/json; charset=utf-8")
    await resp.awrite(json.dumps({"ping": "pong"}))


def reboot(req, resp):
    if req.method == "POST":
        body = yield from req.read_json_body()

        user = body['user']
        username = user['username']
        password = user['password']

        kvs = get_kvs()
        print(kvs.get('USER_LOGIN'), kvs.get('USER_PASSWORD'))
        if username == kvs.get('USER_LOGIN') and password == kvs.get('USER_PASSWORD'):
            machine.reset()
        else:
            return (yield from picoweb.http_error(resp, "500"))

    yield from picoweb.http_error(resp, "500")

    # await picoweb.http_error(resp, "500")


async def credentials(req, resp):
    if req.method == "POST":
        body = await req.read_json_body()

        network = body['network']
        user = body['user']

        success = connect_to_wifi(network['ssid'], network['password'])

        if(success):
            try:

                kvs = get_kvs()

                # Saves the network credentials
                kvs.set('WIFI_SSID', network['ssid'])
                kvs.set('WIFI_PASSWORD', network['password'])

                # Save user credentials
                kvs.set('USER_LOGIN', user['username'])
                kvs.set('USER_PASSWORD', user['password'])

                # Generate a new device ID for the current device
                response = request.post(CREATE_NEW_DEVICE_URL)
                response_data = response.json()

                # Save created device to futher usage
                kvs.set('DEVICE_ID', response_data['id'])
                kvs.set('ACCESS_CODE', response_data['accessCode'])

                # Creates user token to be used to associate device to user
                token = generate_token(user['username'], user['password'])

                body = json.dumps({"accessCode": response_data['accessCode']})

                response = request.post(ASSOCIATE_DEVICE_USER_URL, data=body, headers={
                    'Authorization': token, 'content-type': 'application/json'})
                response_data = response.json()

                # Saves associated userId
                kvs.set('USER_ID', response_data['userId'])

                # Set the device has configured to use
                kvs.set('CONFIGURED', True)

                await picoweb.start_response(
                    resp, content_type="application/json; charset=utf-8")
                await resp.awrite(response.text)

            except Exception as e:
                print(e)
                return picoweb.http_error(resp, 500)
        else:
            return picoweb.http_error(resp, 500)
    else:
        return picoweb.http_error(resp, 500)


ROUTES = [
    ("/ping", ping),
    ("/credentials", credentials),
    ("/reboot", reboot),
]

app = picoweb.WebApp(__name__, ROUTES)


def start_api():
    # debug values:
    # -1 disable all logging
    # 0 (False) normal logging: requests and errors
    # 1 (True) debug logging
    # 2 extra debug logging
    app.run(debug=0, host='192.168.4.1', port=80)
