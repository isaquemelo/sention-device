import _thread
from time import sleep
from modules.auth import generate_token
from modules.contact_cloud import save_sensor_data_to_cloud
from modules.loading_handler import get_user_preferences, setup_pins_and_imports
from modules.network import connect_to_wifi, start_wifi_network, test_internet_connection
from modules.server import start_api
from modules.storage import get_kvs


def managing():
    kvs = get_kvs()

    # Is device configured?
    configured = kvs.get("CONFIGURED")

    if(configured):
        connected = connect_to_wifi(
            kvs.get("WIFI_SSID"), kvs.get("WIFI_PASSWORD"))

        if not connected:
            kvs.set("CONFIGURED", False)
            managing()

        has_connection = test_internet_connection()

        # Tests internet connection
        if not has_connection:
            kvs.set("CONFIGURED", False)
            managing()

        # Since the user login and password are validated on the API route we
        # can trust that those values are valid
        generate_token(kvs.get("USER_LOGIN"), kvs.get("USER_PASSWORD"))

        # Request user preferences
        device_id = kvs.get("DEVICE_ID")
        user_preferences = get_user_preferences(device_id)

        # Not associated to any user
        if not user_preferences:
            kvs.wipe()
            managing()

        # As long as the user doesnt have any setting we don't need to proceed
        while len(user_preferences["sensors"]) == 0 and len(user_preferences["actuators"]) == 0:
            print("Fetching user preferences...")
            user_preferences = get_user_preferences(device_id)
            sleep(5)

        # Generate sensors and actuators instances for further usage
        (sensors_instance, actuators_instance) = setup_pins_and_imports(
            user_preferences)

        lock = _thread.allocate_lock()

        while True:
            sensors_data_bundle = []

            # Get all sensors data and saves to bundle
            for sensor_id, sensor_instance in sensors_instance.items():
                sensors_data_bundle.append({
                    "id": sensor_id,
                    "data": sensor_instance.get_data(),
                })
            # print("sensors_data_bundle", sensors_data_bundle)

            # Toggles actuators
            for _, actuator_instance in actuators_instance.items():
                # This will force sensor data refetching, notice if some delay occurr it'll be here
                actuator_instance.execute_triggers(sensors_instance)

            # Send bundled data to cloud
            with lock:
                save_sensor_data_to_cloud(sensors_data_bundle, lock)

            # start_time = time.ticks_ms()
            # delta = time.ticks_diff(time.ticks_ms(), start_time)
            # print("delta", delta)

    else:
        start_wifi_network()
        start_api()
