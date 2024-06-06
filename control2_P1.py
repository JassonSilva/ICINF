def ingresar_puntajes():
    puntajes = []
    for dia in range(1, 16):
        puntaje = int(input(f"Digite el puntaje del dia {dia}: "))
        puntajes.append(puntaje)
    return puntajes

def mostrar_puntajes(puntajes):
    print("Dias con el puntaje menor a 70:")
    for dia, puntaje in enumerate(puntajes, start=1):
        if puntaje < 70:
            print(f"Día {dia}: {puntaje}")

    print("\nDias con el puntaje igual o mayor a 70:")
    for dia, puntaje in enumerate(puntajes, start=1):
        if puntaje >= 70:
            print(f"Día {dia}: {puntaje}")

def main():
    print("Ingrese los puntajes diarios del alumno durante el curso de 15 días:")
    puntajes = ingresar_puntajes()
    mostrar_puntajes(puntajes)

if __name__ == "__main__":
    main()