from requests import request
from decouple import config
import json

CLUSTER_ID = config('PIESOCKET_CLUSTER_ID')
API_KEY = config('PIESOCKET_API_KEY')
API_SECRET = config('PIESOCKET_API_SECRET')
URL = f'https://{CLUSTER_ID}.piesocket.com/api/publish'
HEADERS = {
    'Content-Type': 'application/json'
}


class NotificationAPI:

    def send(self, room_id, event_id, data):
        data = json.dumps({
            'key': API_KEY,
            'secret':  API_SECRET,
            'roomId': room_id,
            "message": {
                "event": event_id,
                "data": data
            }
        })

        response = request('POST', URL, headers=HEADERS, data=data)
        print('notification-', response.text)
