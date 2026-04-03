#Odem decrescente

num1 = int(input("Informe o 1° Número: "))
num2 = int(input("Informe o 2° Número: "))
num3 = int(input("Informe o 3° Número: "))

if num1 >= num2 and num1 >= num3:
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else: 
    print(num3)