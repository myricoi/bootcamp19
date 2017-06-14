import requests
print("These are the people and crafts in the space right now\n\n")
response=requests.get("http://api.open-notify.org/astros.json")
data = response.json()
for people in data['people']:
	for item,value in people.items():
		print(item,": ",value)
