ventas = [120,150,90,200,175]

# Calcular el total de ventas
total = 0

for venta in ventas:
    if venta > 150:
        print("Venta alta: ", venta)
    else:
        print("Venta Normal: ", venta)
    

total = sum(ventas)
print("Total de ventas: ", total)