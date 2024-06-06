puntajes = []

for dia in range(1, 16):
    puntaje = int(input(f"Ingrese el puntaje del día {dia}: "))
    puntajes.append(puntaje)

puntajes_bajos = []
puntajes_altos = []
for i, puntaje in enumerate(puntajes, start=1):
    if puntaje < 70:
        puntajes_bajos.append(f"día {i}")
    else:
        puntajes_altos.append(f"día {i}")

print("Días con puntaje menor a 70:")
for dia in puntajes_bajos:
    print(dia, end=", ")
print("\nDías con puntaje mayor o igual a 70:")
for dia in puntajes_altos:
    print(dia, end=", ")
