# Calcular area triagulo simples

try:
    lado1 = float(input("Informe lado1 "))
    lado2 = float(input("Informe lado2 "))
    lado3 = float(input("Informe lado3 "))
except ValueError:
    print("Erro: Por favor, insira apenas números.")
    exit()

#Verificar se é triangulo

triangulo = (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2)

if (triangulo):
    print ('Os valores formam um Triangulo')
    # Verifica o tipo de triangulo
    if (lado1 == lado2) and (lado2 == lado3):
        print ('Triangulo Equilatero')
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print ('Triangulo Isosceles')
    else:
        print ('Triangulo Escaleno')
else:
    print ('Os valores não formam um Triângulo')
