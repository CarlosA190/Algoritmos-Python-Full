# Continuación de 2 Ejercicio


import requests

# Endpoint base
url = "https://pokeapi.co/api/v2/pokemon?limit=20"

# Petición GET
respuesta = requests.get(url)

# Validamos respuesta
if respuesta.status_code == 200:
    datos = respuesta.json()
    pokemones = datos["results"]

    # Iteramos sobre la lista de pokemones
    for pokemon in pokemones:
        nombre = pokemon["name"]
        # Regla: Si empieza con 'b' o 'B'
        if nombre.lower().startswith('b'):
            print(f"[ESPECIAL] {nombre.capitalize()}")
        else:
            print(f"Nombre: {nombre.capitalize()}")
else:
    print("Error: No se pudo obtener la lista de Pokémon. Verifique la conexión o el endpoint.")