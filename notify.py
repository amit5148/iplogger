import requests
import slack
import slack.chat

class SlackNotifier(object):
    _SLACK_TOKEN = ''
    _SLACK_CHANNEL = '#general'

    def __init__(self):
        slack.api_token = self._SLACK_TOKEN

    def send_msg(self, msg):
        slack.chat.post_message(self._SLACK_CHANNEL, msg)

def get_selfip():
    response = requests.get('https://api.ipify.org/?format=json')
    return response.text

sn = SlackNotifier()
sn.send_msg(get_selfip())