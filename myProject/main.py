import requests 
req = requests.get('https://www.google.com/') 
print(req.encoding) 
print(req.status_code) 
