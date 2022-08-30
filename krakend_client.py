"""
      _ _            _
  ___| (_) ___ _ __ | |_
 / __| | |/ _ \ '_ \| __|
| (__| | |  __/ | | | |_
 \___|_|_|\___|_| |_|\__|
"""

import time
import requests

print('start...')
for _ in range(10):
    requests.post('http://localhost:8080/v1/data', data={'test': 'ok'})
    print('some_message_bytes')
    time.sleep(5)

