# Guardar las ventas en una lista
ventas = [120, 150, 90, 200, 175]

# Recorrer la lista y mostrar cada venta
for dia, monto in enumerate(ventas, start=1):
    print(f"Día {dia}: {monto} en ventas")

# Calcular el total
total = sum(ventas)

# Mostrar el total
print("Total de ventas en 5 días:", total)
