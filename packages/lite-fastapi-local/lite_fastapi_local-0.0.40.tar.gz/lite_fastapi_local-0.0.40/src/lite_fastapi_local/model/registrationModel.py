import json
import os

from lite_fastapi_local.common.variable import common
from lite_fastapi_local.settings import mqtt

class Registration():

    def register_iot_core_by_mac_address(self):
        mac = common.get_MACHINE_MAC(),
        iot_core_name = os.environ['iot_core_name']
        mqtt.publish(f'tg/{mac}/registration', json.dumps({
            'MAC':mac,
            'serial_number': iot_core_name
        }))

    
registration = Registration()