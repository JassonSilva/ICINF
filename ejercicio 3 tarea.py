altura = 0
sumalturas = 0
cont = 0

while altura >= 0:
    altura = float(input("Ingrese la estatura:"))
    if altura == 0:
        break
    sumalturas= sumalturas + altura
    cont = cont + 1

promedio= sumalturas / cont
print("El promedio de estatura es:", promedio)