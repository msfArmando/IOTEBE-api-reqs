import requests
import json
from datetime import datetime, timedelta

now = datetime.now()
one_day_later = now + timedelta(days=0)
seven_days_earlier = now - timedelta(days=1)

timestamp_now = int(one_day_later.timestamp())
timestamp_sde = int(seven_days_earlier.timestamp())

URL = 'https://api.iotebe.com/v2'
API_KEY = 'HnfIJel3Bw3cEri5AAYJvzwSFw30maZ43kZmpp4g'

#sectors_json = json.dumps(["Extração"])
# response = requests.get(url=f"{URL}/metrics/diagnostic", 
#                         headers={"x-api-key" : f"{API_KEY}", 
#                                  "accept": "application/json"}, 
#                         params={"data_type": "closed_alarms", 
#                                 "start_time": timestamp_sde, 
#                                 "end_time": timestamp_now})

# response_pending = requests.get(url=f"{URL}/metrics/diagnostic", 
#                         headers={"x-api-key" : f"{API_KEY}", 
#                                  "accept": "application/json"}, 
#                         params={"data_type": "pending_alarms", 
#                                 "start_time": timestamp_sde, 
#                                 "end_time": timestamp_now})

response = requests.get(url=f"{URL}/diagnostics",
                        headers={"x-api-key" : f"{API_KEY}", 
                                 "accept": "application/json"}, 
                        params={"status": "concluded", 
                                "start_time": timestamp_sde, 
                                "end_time": timestamp_now,
                                "has_financial_return": False,
                                "group_by_spot": False,
                                "limit": 1000,
                                "offset": 0,
                                })

with open('result.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(response.json(), ensure_ascii=False))

alarms = response.json().get('items', [])

if not alarms:
    average_time: int = 0
else:
    average_time: int = int(sum(alarm['end_time'] - alarm['start_time'] for alarm in alarms) / len(alarms))

print(average_time)

