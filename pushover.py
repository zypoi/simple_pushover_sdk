import requests
import json


class pushover:
    user = ''
    application = ''
    s = requests.session()
    header = {'Content-Type': "application/json"}

    def __init__(self, user, application):
        self.user = user
        self.application = application

    def push(self, message):
        session = self.s
        dict_payload = {
            "token": self.application,
            "user": self.user,
            "message": message}
        print(message)
        print(json.dumps(dict_payload))
        resp = session.post('https://api.pushover.net/1/messages.json', headers=self.header, data=json.dumps(dict_payload))
        dict_resp = resp.json()
        if dict_resp["status"] == 1:
            print(dict_resp)
            print('Push message {} success'.format(message))
        else:
            print(dict_resp)
            print('Push message {} failed'.format(message))


