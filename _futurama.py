import requests

url = "https://futurama-dam.web.app/api"

def characters():
  response = requests.get(f"{url}/characters")
  data = response.json()["hits"]
  return [character["name"] for character in data]

def charactersDead():
  response = requests.get(f"{url}/characters")
  data = response.json()["hits"]
  return [character["name"] for character in data if character["status"] == "DEAD"]

def charactersByGender(gender):
  response = requests.get(f"{url}/characters")
  data = response.json()["hits"]
  return [character["name"] for character in data if character["gender"] == gender]

print("{characters}\n", characters())
print("{Dead}\n", charactersDead())
print("{ByGender}\n", charactersByGender("FEMALE"))