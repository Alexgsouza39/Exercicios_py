#preço do produto

preco1 = int(input("Informe o 1° preco: "))
preco2 = int(input("Informe o 2° preco: "))
preco3 = int(input("Informe o 3° preco: "))

if preco1 == preco2 and preco1 == preco3:
    print(f"O preço é igual compre qualquer um")
elif preco1 < preco2 and preco1 < preco3:
    print(f"O preço 1 é o melhor")
elif preco2 < preco3:
    print(f"O preço 2 é o melhor")
else:
    print(f"O preço 3 é o melhor")

