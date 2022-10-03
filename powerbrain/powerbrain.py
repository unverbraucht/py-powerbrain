import requests

class Powerbrain:
    def __init__(self, url, verify_ssl=False):
        self.session = requests.Session()
        self.base_url = url
        self.verify_ssl = verify_ssl
        self.meta = None
    
    def connect(self):
        self.meta = self.session.get(f'{self.base_url}/cnf?cmd=get_params').json()
        self.max_total_evse_power = self.meta['max_total_evse_power']
        self.version = self.meta['version']
        if 'dev_meta' in self.meta:
            self.device_names = self.meta['dev_meta']
        else:
            self.device_names = self.session.get(f'{self.base_url}/cnf?cmd=get_dev_types').json()
    
    def get_dev_info(self, get_raw_response=False):
        response = self.session.get(f'{self.base_url}/cnf?cmd=get_dev_info').json()
        if get_raw_response:
            return response
        devices = {}
        output = {}
        if 'devices' in response:
            for raw_device in response['devices']:
                dev_id = raw_device['dev_id']
                dev_type = raw_device['dev_type']
                raw_device['dev_type_label'] = self.device_names[dev_type]
                devices[dev_id] = raw_device
        
        # Copy all dict keys except for devices
        for key in response:
            if key != 'devices':
                output[key] = response[key]
        output['devices'] = devices
        
        return output