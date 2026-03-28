# Creación del diccionario
caldero = {
    "Colas de lagartija": 5,
    "Polvo de estrellas": 2
}
# Se agregan los 3 items
caldero["Colas de lagartija"] += 3

# Paso el cuervo y se robo todo el Polvo de estrellas
del caldero["Polvo de estrellas"]

# Imprimimos el inventario final después del robo
print("Inventario final del caldero:")
for ingrediente, cantidad in caldero.items():
    print(f"{ingrediente}: {cantidad}")
