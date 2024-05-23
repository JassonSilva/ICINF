Preguntas = int(input("¿Cuantas preguntas se le hicieron al entrevistado? "))
Correctas = int(input("¿cuantas de esas respuestas fueron correctas? "))
Puntaje = Correctas / Preguntas * 100

if Puntaje >= 95:
    print("El entrevistado posee el nivel maximo de conocimiento")
else:
    if Puntaje >= 70:
        print("El entrevistado posee el nivel medio de conocimiento")
    else:
        if Puntaje >= 40:
            print("El entrevistado posee el nivel regular de conocimiento")
        else:
            print("El entrevistado posee el nivel insuficiente de conocimiento")


print("el puntaje de la entrevista es de: ", Puntaje) 