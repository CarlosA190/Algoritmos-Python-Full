import requests

def obtener_pokemon(limite=20):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"
    
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        pokemon_lista = datos["results"]
        
        print("Lista de Pokémon:\n")
        for i, pokemon in enumerate(pokemon_lista, start=1):
            print(f"{i}. {pokemon['name']}")
    
    except requests.exceptions.ConnectionError as e:
        print(f"Error de conexión: {e}")
    except requests.exceptions.Timeout:
        print("Error: La API tardó demasiado en responder.")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

obtener_pokemon()