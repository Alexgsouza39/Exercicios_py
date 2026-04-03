# 06_maiora_de_3_numeros

num1 = int(input("Informe o 1° Número: "))
num2 = int(input("Informe o 2° Número: "))
num3 = int(input("Informe o 3° Número: "))

if num1 == num2 and num1 == num3:
    print("Numeros são Iguais")
elif num1 > num2 and num1 > num3:
    print(f"O maior nuúmero é: {num1} ")
elif num2> num3:
    print(f"O maior numero é: {num2}")
else:
    print(f"O maior número é: {num3}")