import json

from lite_fastapi_local.common.variable import common
from lite_fastapi_local.settings import mqtt

class Setup():

    def change_volume(self, volume: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            'volume': str(volume)
        }))

    def change_motor_movement(self, motor_on_time: int, motor_on_close_time: int, door_hold_time: int, door_open_hold_time: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            'motor_on_time': str(motor_on_time),
            'motor_on_close_time': str(motor_on_close_time),
            'door_hold_time': str(door_hold_time),
            'door_open_hold_time': str(door_open_hold_time)
        }))

    def change_count_max(self, count_max: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            'count_max': str(count_max)
        }))

    def change_count_set(self, count_set: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            'count_set': str(count_set)
        }))

    def change_door_holding_pwm(self, door_holding_pwm: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "door_holding_pwm": str(door_holding_pwm)
        }))

    def change_door_open_pwm(self, door_open_pwm: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "door_open_pwm": str(door_open_pwm)
        }))
        
    def change_motor_normal_current(self, motor_normal_current: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "motor_normal_current": str(motor_normal_current)
        }))
        
    def change_motor_end_current(self, motor_end_current: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "motor_end_current": str(motor_end_current)
        }))
        
    def change_door_safe_pwm(self, door_safe_pwm: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "door_safe_pwm": str(door_safe_pwm)
        }))
        
    def change_door_slow_pwm(self, door_slow_pwm: int):
        mac = common.get_MACHINE_MAC()
        mqtt.publish(f'tg/{mac}/setup', json.dumps({
            "door_slow_pwm": str(door_slow_pwm)
        }))


setup = Setup()