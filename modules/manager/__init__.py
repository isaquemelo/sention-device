from time import sleep
from modules.auth import generate_token
from modules.loading_handler import get_user_preferences, setup_pins_and_imports
from modules.network import connect_to_wifi, test_internet_connection
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
        while len(user_preferences.sensors) == 0 or len(user_preferences.actuators) == 0:
            user_preferences = get_user_preferences(device_id)
            sleep(5)

        # Generate sensors and actuators instances for further usage
        (sensors_instance, actuators_instance) = setup_pins_and_imports(
            user_preferences)

        while True:
            sensors_data_bundle = []

            # Get all sensors data and saves to bundle
            for sensor_id, sensor_instance in sensors_instance.items():
                sensor_data = sensor_instance.get_data()

                sensors_data_bundle.append({
                    "id": sensor_id,
                    "data": sensor_data,
                })
