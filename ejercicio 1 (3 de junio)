def contar_vocales_consonantes(palabra):
    vocales = "aeiouAEIOU"
    cantidad_vocales = 0
    cantidad_consonantes = 0

    for letra in palabra:
        if letra in vocales:
            cantidad_vocales += 1
        elif letra.isalpha():
            cantidad_consonantes += 1
    
    return cantidad_vocales, cantidad_consonantes

def main():
    palabras = []

    while True:
        palabra = input("Ingresa una palabra (o presiona enter para finalizar): ")
        if palabra == "":
            break
        palabras.append(palabra)

    for palabra in palabras:
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocales}, Consonantes: {consonantes}")

if __name__ == "__main__":
    main()

