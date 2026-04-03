"""num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma dos dois números é:", soma)"""

numeros = ['42', '20']

soma = lambda k: int(numeros.pop()) + int(numeros.pop())
print(soma(numeros))
# O código acima define uma lista chamada `numeros` com os valores '42' e '20'. Em seguida, é criada uma função lambda que realiza a soma dos dois números presentes na lista, utilizando o método `pop()` para remover e retornar os últimos elementos da lista. Por fim, a soma é calculada e impressa no console.
