# 1. Crear el diccionario con los platos y sus puntuaciones
banquete = {
    "Sopa de pantano": 4,
    "Pastel de rocas": 7,
    "Filete de dragón": 10
}
 
# 1. Actualizar la puntuación de "Sopa de pantano" a 6
banquete["Sopa de pantano"] = 6
 
# 2. Imprimir solo los nombres de los platos (las llaves)
# print("\n"+"-"*20 + "\n")
print("Menú del ogro:")
for plato in banquete.keys():
    print(plato)
 
# 3. Si "Filete de dragón" tiene puntuación mayor a 8, imprimir mensaje especial
if banquete["Filete de dragón"] > 8:
    print("¡Un festín digno de un rey ogro!")

print("\n"+"-"*20 + "\n")