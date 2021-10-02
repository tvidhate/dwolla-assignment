import requests
import datetime

r = requests.get('http://127.0.0.1:5000/v1/currentDateTime')
data = r.json()
date_time_str=data['currentTime']
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
print('Time is:', date_time_obj.time())
