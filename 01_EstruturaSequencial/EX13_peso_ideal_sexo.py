# Calculadora de peso ideal exemplo 1
"""sexo = input('Qual é o seu sexo?: ')
altura = float(input('Inserir sua altura em (m): '))

if sexo == 'Masculino':
    peso_Ideal = (72.7 * altura) -58
    print(f"O Peso ideal para um homen de {altura}m é: {peso_Ideal:.2f}")
elif sexo == 'Feminino':
    peso_Ideal = (62.1* altura) -44.7
    print(f"O Peso ideal para uma mulher de {altura}m é: {peso_Ideal:.2f}")
else:
    print("Sexo inválido")"""

# Calculadora de peso ideal exemplo 2
    
sexo = input('Informe seu sexo (M/F): ')
altura = float(input('Informe sua altura (em metros): '))
peso = float(input('Informe o seu peso (em kg): '))

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

if (peso > peso_ideal):
    print (f'Você esta acima do seu peso ideal: {peso_ideal:.2f}')

elif (peso < peso_ideal):
    print(f'Você esta abaixo do seu peso ideal: {peso_ideal:.2f}')

else:
    print(f'Você esta no seu peso ideal: {peso_ideal:.2f}')
