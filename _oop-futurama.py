import requests

class Futurama:
  def __init__(self):
    self.url = "https://futurama-dam.web.app/api"

  def characters(self):
    response = requests.get(f"{self.url}/characters")
    data = response.json()["hits"]
    return [character["name"] for character in data]

  def charactersDead(self):
    response = requests.get(f"{self.url}/characters")
    data = response.json()["hits"]
    return [character["name"] for character in data if character["status"] == "DEAD"]

  def charactersByGender(self, gender):
    response = requests.get(f"{self.url}/characters")
    data = response.json()["hits"]
    return [character["name"] for character in data if character['gender'] == gender]

  def humans(self):
    response = requests.get(f"{self.url}/characters")
    data = response.json()["hits"]
    return [character["name"] for character in data if character['species'] == "HUMAN"]

  def episode(self, season, episode):
    response = requests.get(f"{self.url}/episodes")
    data = response.json()['hits']

    for item in data:
      if item['season']['id'] == season and item['number'] == episode:
        return item['name']
    return None


futurama = Futurama()
print("{characters}\n", futurama.characters())
print("{charactersDead}\n", futurama.charactersDead())
print("{charactersByGender}\n", futurama.charactersByGender("FEMALE"))
print("{episode}{3, 5}\n", futurama.episode(3, 5))

