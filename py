import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
LC = int(input("Cantidad de caracteres (en numeros): "))
password = ""

for i in range(LC):
    password += random.choice(caracteres)

print("Su Contraseña Generada de",LC,"caracteres, Es:",password)
