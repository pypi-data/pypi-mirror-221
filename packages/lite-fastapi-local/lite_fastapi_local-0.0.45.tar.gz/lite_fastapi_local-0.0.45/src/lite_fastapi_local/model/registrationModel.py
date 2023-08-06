import json
import os

from lite_fastapi_local.common.variable import common
from lite_fastapi_local.settings import mqtt

class Registration():

    def register_iot_core_by_mac_address(self):
        mac_address = common.get_MACHINE_MAC()
        iot_name = os.environ['iot_name']
        mqtt.publish(f'tg/{mac_address}/updateMacAddress', json.dumps({
            'mac_address':mac_address,
            'serial_number': iot_name
        }))

    
registration = Registration()