import requests

#get ip 
response = requests.get('https://api.ipify.org/?format=json')
get_ip=response.json().get('ip')

#get location
location = f'https://ipinfo.io/{get_ip}/geo'
response = requests.get(location)
location_data = response.json()

country=location_data.get('country')
city=location_data.get('city')


print(f"My public IP address is: {get_ip}")
print(f"my location : country: {country}, city: {city}")
