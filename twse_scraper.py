import requests
import json

response = requests.get('https://www.twse.com.tw/zh/exchangeReport/BWIBBU_d')
# print(response.json()['data'][1])

print(response.json()['data'][1])
print(response.json()['data'][2])
print(response.json()['data'][3])



