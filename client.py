import requests
from datetime import datetime

r = requests.get('http://0.0.0.0:5000/now')
current = r.content.decode('utf-8')

print(datetime.fromtimestamp(float(current)))
