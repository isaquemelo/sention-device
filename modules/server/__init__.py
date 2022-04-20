import libs.ulogging as logging
import libs.picoweb as picoweb
import json

from modules.network import connect_to_wifi


async def ping(req, resp):
    await picoweb.start_response(resp, content_type="application/json; charset=utf-8")
    await resp.awrite(json.dumps({"ping": "pong"}))


async def credentials(req, resp):
    if req.method == "POST":
        body = await req.read_json_body()

        network = body['network']
        user = body['user']

        print(network, user)

        success = connect_to_wifi(network['ssid'], network['password'])

        if(success):
            print("Aeee")

        await picoweb.start_response(resp, content_type="application/json; charset=utf-8")

    else:
        picoweb.http_error(resp, 500)


ROUTES = [
    ("/ping", ping),
    ("/credentials", credentials),
]

app = picoweb.WebApp(__name__, ROUTES)


def start_api():
    # debug values:
    # -1 disable all logging
    # 0 (False) normal logging: requests and errors
    # 1 (True) debug logging
    # 2 extra debug logging
    app.run(debug=0, host='192.168.18.16', port=80)
