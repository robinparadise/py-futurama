# Examen DAM 2ª Evaluación

API de futurama
endpoint: [https://futurama-dam.web.app](https://futurama-dam.web.app)

## Parte 1: `futurama.py` (4pts)

### Ejemplo de uso de la API

```python
import requests

url = "https://futurama-dam.web.app/api/characters"
response = requests.get(url)
data = response.json()
print(data)
```


1. **(2pts) Crea una función que muestre una lista de personajes de futurama. La lista debe consistir solo con los nombres de los personajes. La función debe de llamarse `characters()`.**

Ejemplo:

```python
Output: ["Philip J. Fry", "Morgan Proctor", "Mugger", ...]
```

2. **(1pts) Crea una función que filtre los personajes muertos (dead) de la lista de personajes. La lista debe consistir solo con los nombres de los personajes. La funcion debe de llamarse `charactersDead()`.**

Ejemplo:
```python
Output: ["Mr. Panucci", "Njörd", "Mildred Fry", ...]
```

3. **(1pts) Crea una función que filtre los personajes por género (FEMALE, MALE, UNKNOWN). La lista debe consistir solo con los nombres de los personajes. La funcion debe de llamarse `charactersByGender(gender)`.**
Ejemplo:
```python
Output: ["Amy Wong", "LaBarbara Conrad", "Morgan Proctor", ...]
```

## Parte 2: `oop_futurama.py` (5pts + 1pt)

### Ejemplo de la clase `Futurama`

```python
class Futurama:
    def __init__(self):
        self.url = "https://futurama-dam.web.app/api"
        ...

    def characters(self):
        pass

    def charactersDead(self):
        pass

    ...

futurama = Futurama()
print(futurama.characters())
...

```

1. **(3pts) Crea una clase llamada `Futurama` que tenga los siguientes métodos:**
    - `characters()`
    - `charactersDead()`
    - `charactersByGender(gender)`

2. **(1pts) Crea un método dentro de la clase `Futurama` que muestre todos los personajes que sean de la especie `HUMAN`. La función debe de llamarse `humans()`**

Ejemplo:
```python
Output: ["Philip J. Fry", "Mr. Panucci", "Mildred Fry", ...]
```

3a. **(2pts) Crea un método dentro de la clase `Futurama` que muestre el nombre del episodio que se pasa por parámetro a la función. La función debe de llamarse `episode(season, episode)`**

Ejemplo:
```python
futurama.episode(3, 5)
Output: "Amazon Women in the Mood"
```

3b. **(2pts) Crea un método dentro de la clase `Futurama` que muestre todas las especies de los personajes. La función debe de llamarse `species()` y no debe de retornar especies repetidas.**

Ejemplo:
```python
Output: ["HUMAN", "ROBOT", "HEAD", "MONSTER", "UNKNOWN", "ALIEN"]
```



