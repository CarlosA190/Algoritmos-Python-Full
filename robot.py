# Diccionario inicial
memoria_robot = {
    "001": "Hola",
    "010": "Adiós",
    "100": "Aceite"
}
 
# 1. Agregar la nueva palabra: "111" significa "Amigo"
memoria_robot["111"] = "Amigo"
 
# 2. Un usuario dice "010", imprimir la traducción
print("Traducción de 010:", memoria_robot["010"])
 
# 3. Intentar traducir "101" usando .get() para evitar error
codigo = "101"
traduccion = memoria_robot.get(codigo, "Error: Código no encontrado en mi base de datos")
 
print("Traducción de 101:", traduccion)