# Sistema de descuento de videojuegos

# Soliciatamos datos al usuario
precio = float(input("Ingrese el precio del Videojuego: Q. "))
vip = input("¿El cliente es un cliente VIP? (Si/No): ").strip().lower()

# Aplicar precio de descuento del 10% si el precio es >= 500
if precio >= 500:
    precio = precio * 0.90 #Descuento del 10% si aplica.


# Verificamos si el ciente es VIP y se le aplica el descuento adicional
if vip == 'si' or vip == "sí":
    precio = precio * 0.85 #Descuento del 15% si es cliente VIP


# Mostramos Precio final
print(f"El precio final a pagar es: Q{precio:.2f}")