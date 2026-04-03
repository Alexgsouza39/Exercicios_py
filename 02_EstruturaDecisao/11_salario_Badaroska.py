# Salario funcionario

salario = float(input("Digite o salario do Funcionario: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
novoSalario = salario + aumento

print(f'Salario antes do reajuste: {salario}')
print(f'Percentual de aumento: {percentual}','%')
print(f'Valor do aumento: {aumento}')
print(f'Novo Salario: {novoSalario}')

"""
Logica:
- Salarios até R$ 280,00 (incluindo) : aumento de 20%
- Salarios entre R$ 280,00 e R$ 700,00 : aumento de 15%
- Salarios entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- Salarios de R$ 1500,00 em diante : aumento de 5%
- Após o aumento ser realizado, informe na tela:
- O salario antes do reajuste;
- O percentual de aumento aplicado;
- O valor do aumento;
- O novo salario, após o aumento.    
"""