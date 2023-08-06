# *----------------------------------------------------------------
# * MobAI.API.ApiData
# * Write by MoYeRanQianZhi
# * 2023.7.26
# *----------------------------------------------------------------

import json


class A:
    def __init__(self, _data):
        self._data = _data

    def __str__(self):
        return json.dumps(self._data, indent=4)

    def __repr__(self):
        return json.dumps(self._data, indent=4)


class ChatData(A):
    def __init__(self, _data):
        A.__init__(self, _data)
        self.time = _data['time']
        self.state = _data['state']
        if _data['state'] == 'success':
            self.data = A(_data['data'])
            self.data.reply = _data['data']['reply']
        else:
            self.data = A(_data['data'])
            self.data.error = _data['data']['error']


class NewData(A):
    def __init__(self, _data):
        A.__init__(self, _data)
        self.time = _data['time']
        self.state = _data['state']
        if _data['state'] == 'success':
            self.data = A(_data['data'])
            self.data.id = _data['data']['id']
            self.data.password = _data['data']['password']
            self.data.reply = _data['data']['reply']
        else:
            self.data = A(_data['data'])
            self.data.error = _data['data']['error']
