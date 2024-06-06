palabras = []

print("Ingrese una palabra, para finalizar digite 'Enter'")
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "":
        break
    palabras.append(palabra)

if len(palabras) == 0:
    print("No ingresaste ninguna palabra.")
else:
    menos_caracteres = min(len(palabra) for palabra in palabras)
    print("La palabra más corta tiene", menos_caracteres, "caracteres.")