# Ejercicio 2: Consumo de PokeApi

import requests

# Solicitamos el nombre del Pokémon al usuario
pokemon = input("Ingrese el nombre del Pokémon: ").strip().lower()


# Construimos la URL de la API
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"


# Hacemos la petición HTTP
respuesta = requests.get(url)

# Verificamos si la respuesta es existosa
if respuesta.status_code == 200:
    datos = respuesta.json()

    # Mostramos la información básica del Pokémon
    print(f"\nNombre: {datos['name'].capitalize()}")
    print(f"ID: {datos['id']}")
    print(f"Altura: {datos['height']}")
    print(f"Peso: {datos['weight']}")

    # Mostramos los tipos de Pokémon
    print("Tipos: ")
    for tipo in datos['types']:
        print (f" - {tipo['type']['name'].capitalize()}")
    
    # Mostramos las habilidades
    print("Habilidades: ")
    for habilidad in datos['abilities']:
        print(f" - {habilidad['ability']['name'].capitalize()}")

else:
    print("\nError: Pokémon no encontrado. Verifique el nombre e intente nuevamente")