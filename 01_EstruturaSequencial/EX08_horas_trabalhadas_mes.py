numeros = ['80', '55.62']

horas_trabalhadas = float(numeros[0])
valor_hora = float(numeros[1])  
salario = horas_trabalhadas * valor_hora
print('O salário do funcionário é:',f'{salario:.2f}')
# O código acima calcula o salário de um funcionário com base nas horas trabalhadas e no valor da hora, exibindo o resultado formatado com duas casas decimais.

horas_trabalhadas = float(input('Quantas horas trabalhadas mes?:'))
valor_hora = float(input('Quanto você ganha por hora?:'))
salario = horas_trabalhadas * valor_hora
print('O salário do funcionário é:',f'{salario:.2f}')
# O código calcula o salario solicitando ao funcionário, quantas horas de trabalho e o valor da hora trabalhada



def calcular_salario():
    horas_trabalhadas = float(input('Quantas horas trabalhadas mes?:'))
    valor_hora = float(input('Quanto voce ganha po hora?:'))
    print(f"Seu salário este mês será: R$ {salario:.2f}")
calcular_salario()
# O função calcula o salario solicitando ao funcionario, quantas horas de trabalho e o valor da hora trabalhada