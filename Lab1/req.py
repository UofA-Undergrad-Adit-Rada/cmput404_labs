import requests

resp = requests.get('https://raw.githubusercontent.com/adit333/cmput404_labs/master/Lab1/req.py')
print(resp.text)
