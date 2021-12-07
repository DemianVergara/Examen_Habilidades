import requests
import json
import meraki


api_key='6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
headers= {'X-Cisco-Meraki-API-Key':api_key}
UrlMeraki= 'https://api.meraki.com/api/v1'


url1 = UrlMeraki +'/organizations'
response1 = requests.get(url1,headers=headers,verify=False)
response1Json = response1.json()
print (json.dumps(response1Json, indent=4))
IdOrganizacion= response1Json[0]["id"]
print ('*'*150)


url2 = url1 +'/549236/networks'.format(IdOrganizacion)
response = requests.get(url2,headers=headers,verify=False)
responsej2Json = response.json()
print (json.dumps(responsej2Json, indent=4))
RedId= responsej2Json[0]["id"]
print ('*'*150)

url3 = 'https://api.meraki.com/api/v1/networks/L_646829496481109720/devices'.format(RedId)
response = requests.get(url3,headers=headers,verify=False)
responsej3Json = response.json()
print (json.dumps(responsej3Json, indent=4))
DispositivoId= responsej3Json[0]["serial"]
print ('*'*150)

url4 = 'https://api.meraki.com/api/v1/networks/L_646829496481109720/devices/Q2FV-W72R-U7WX'.format(DispositivoId)
response = requests.get(url4,headers=headers,verify=False)
responsej4Json = response.json()
print (json.dumps(responsej4Json, indent=4))
SerialId= responsej3Json[0]["serial"]
print ('*'*150)
