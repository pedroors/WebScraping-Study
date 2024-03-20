import requests

response = requests.get('https://g1.globo.com/')

print(response.status_code)
#print("--- HEADER ---")
#print(response.headers)

print("---- CONTENT ----")
print(response.content)
