nombres = []

for i in range(7):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombres_filtrados = []
for nombre in nombres:
    if nombre[-1] != 'a':
        nombres_filtrados.append(nombre)

print("Lista resultante al eliminar los nombres terminados por la letra 'a':")
for nombre in nombres_filtrados:
    print(nombre)
