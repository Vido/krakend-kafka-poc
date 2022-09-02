"""                     
 _ __  _ __ ___   __| |_   _  ___ ___ _ __ 
| '_ \| '__/ _ \ / _` | | | |/ __/ _ \ '__|
| |_) | | | (_) | (_| | |_| | (_|  __/ |   
| .__/|_|  \___/ \__,_|\__,_|\___\___|_|   
|_|
"""
import time
import requests

print('start...')
for _ in range(10):
    requests.post('http://localhost:8080/v1/data', data={'test': 'ok'})
    print('some_message_bytes')
    time.sleep(5)

