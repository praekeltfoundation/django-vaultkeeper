import json


class ConfigParser(object):
    def __init__(self, config=None):
        self.config = config
        self.entry_script = None
        self.output_path = None
        self.refresh_interval = None
        self.renewal_grace = None

    def load_data(self, data):
        self.entry_cmd = data['entry_cmd']
        self.output_path = data['output_path']
        self.refresh_interval = data['refresh_interval']
        self.renewal_grace = data['renewal_grace']

    def load_configs(self):
        data = json.loads(self.config)
        self.load_data(data)
