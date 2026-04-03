escreva_numero_imprima = int(input("Digite um número: "))

def escreva_numero_imprima(num):
    if num == 42:
        print("O número é 42!")
    else:
        print("O número não é 42.")

escreva_numero_imprima(escreva_numero_imprima)
# O código acima solicita ao usuário que digite um número, armazena esse número em uma variável e, em seguida, define uma função chamada `escreva_numero_imprima` que verifica se o número é igual a 42. Se for, imprime "O número é 42!", caso contrário, imprime "O número não é 42.". Por fim, a função é chamada com o número digitado pelo usuário.