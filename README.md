# Examen 2º DAM

API de futurama doc endpoint: [https://futurama-dam.web.app/dam2](https://futurama-dam.web.app/dam2)

## Parte 1: `futurama.py` (4pts)

### Ejemplo de uso de la API

```python
import requests

url = "https://futurama-dam.web.app/api/v3/characters"
response = requests.get(url)
data = response.json()
print(data)
```


1. **(2.5pts) Crea una función que muestre una lista de personajes de futurama. La función debe de llamarse `characters(limit)`. Y debe de recibir un parámetro `limit` que por defecto sea `500`. La lista debe consistir solo con los nombres de los personajes. Si el parámetro `limit` es mayor que la cantidad de personajes, la función debe de retornar todos los personajes. Si el parámetro `limit` es menor que 0, la función debe de retornar los últimos `limit` personajes.**


Ejemplo:

```python
characters(10)
Output: ["Philip J. Fry", "Morgan Proctor", "Mugger", ...]
characters(0)
Output: []
characters(-10)
Output: ["Morbo", "Mom", "Mildred Fry", ...]
```


## Parte 2: `oop_futurama.py`


1. **(2.5pts) Crea una clase llamada `Futurama` que tenga los siguientes métodos:**
    - `characters(limit)`. La clase debe guardar los personajes en una lista y retornar la lista de personajes. La lista debe consistir solo con los nombres de los personajes. Si el parámetro `limit` es mayor que la cantidad de personajes, la función debe de retornar todos los personajes. Si el parámetro `limit` es menor que 0, la función debe de retornar los últimos `limit` personajes.


2. **(2pts) Crea un método dentro de la clase `Futurama` que muestre el `nombre del episodio` que se pasa por parámetro a la función. La función debe de llamarse `episode(season, episode)`**. Usa el endpoint `/api/v3/seasons` para obtener el nombre del episodio. 

Ejemplo:
```python
futurama.episode(3, 5)
Output: "Amazon Women in the Mood"
```

3. **(3pts) Crea la clase Character que tenga los siguientes métodos:**
    - `__init__(self, info)`: El constructor debe de recibir el nombre del personaje.
    - `__str__(self)`: Debe de retornar el nombre del personaje.
    - `__len__(self)`: Debe de retornar la cantidad de letras del nombre del personaje.
    - `__add__(self, other)`: Debe de retornar el nombre del personaje concatenado con el nombre del personaje que se pasa por parámetro.
    - `__eq__(self, other)`: Debe de retornar `True` si el nombre del personaje es igual al nombre del personaje que se pasa por parámetro.
    - `__gt__(self, other)`: Debe de retornar `True` si el nombre del personaje es mayor al nombre del personaje que se pasa por parámetro.

Ejemplo:
```python
api = Futurama()
characters = api.characters(10)
character = Character(characters[0])
print(character) # Output: "Philip J. Fry"
print(len(character)) # Output: 13
print(character + Character(characters[1])) # Output: "Philip J. FryMorgan Proctor"
...

```

**Notas:**
- Puedes usar la librería `requests` para hacer las peticiones a la API.
- No olvides manejar los errores en caso de que el endpoint no responda.
- No olvides de imprimir los resultados para comprobar que tu código es correcto.
- Revisa los nombres de los métodos y parámetros que debes de usar.
- El archivo debe de ejecutar sin errores.
- No olvides de subir el archivo a github o enviarlo al correo: `rgiles@metrodoraeducation.com`