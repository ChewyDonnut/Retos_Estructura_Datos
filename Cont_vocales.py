frase = str(input("Introduce una palabra: "))
frase=frase.lower()
vocales = ["a","e","i","o","u"]
for vocal in vocales:
    times = 0
    for letter in frase:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")