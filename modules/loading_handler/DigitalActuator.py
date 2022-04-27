from modules.loading_handler.IActuator import IActuator

from machine import Pin


class DigitalActuator(IActuator):

    def __init__(self, port, triggers):
        self.port = Pin(port, Pin.OUT)
        self.triggers = triggers

    def set_state(self, state):
        self.port.value(state)

    def do_action(self, action):
        if action == "TURN_ON":
            self.set_state(True)
        else:
            self.set_state(False)

    def execute_triggers(self, sensors_instance):
        for trigger in self.triggers:
            action = trigger["action"]
            logic_operator = trigger["logicOperator"]
            value = trigger["value"]
            sensor_id = trigger["sensorId"]
            sensor_data_source = trigger["dataSource"]

            sensor_instance = sensors_instance[sensor_id]
            sensor_value = False

            if(len(sensor_data_source)):
                sensor_value = sensor_instance.get_data(sensor_data_source)
            else:
                sensor_value = sensor_instance.get_data()

            # print(sensor_id, "=>", sensor_value)

            if logic_operator == "GREATER_THAN":
                if(sensor_value > value):
                    self.do_action(action)
            elif logic_operator == "SMALLER_THAN":
                if(sensor_value < value):
                    self.do_action(action)
