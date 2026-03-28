# Definir los articulos
inventario = {
    "Cuadernos": 50,
    "Lapiceros": 60,
    "Saca Puntas": 10
}
print("\n"+"-"*20 + "\n")
#  REcorrido
print("Articulos disponibles")
for producto in inventario.keys():
    print(f"- {producto}")

print("\n"+"-"*20 + "\n")

# Recrrido 2: soplo las cantidades
total_productos = 0
for cantidad in inventario.values():
    total_productos += cantidad
print(f"Total de productos en bodega: {total_productos}")

print("\n"+"-"*20 + "\n")




# Reporte detallado
print("Reporte inventario")
for producto, cantidad in inventario.items():
    print(f"Hay {cantidad} unidades de {producto}")
print("\n"+"-"*20 + "\n")