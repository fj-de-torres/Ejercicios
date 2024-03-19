import requests

url = "https://httpbin.org/post"

my_data = dict(title="Sesión python2 22", author = "Cisco, Fran Cisco")

response = requests.post(url, data= my_data)

print("Response")
print(response.json())