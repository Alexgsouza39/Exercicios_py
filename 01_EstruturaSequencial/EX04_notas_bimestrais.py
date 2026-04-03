
notas_bimestrais = ['7', '8', '9', '10']
media = sum(map(float, notas_bimestrais)) / len(notas_bimestrais)
print(f'A média anual é {media}')
# O código acima calcula a média anual das notas bimestrais fornecidas na lista `notas_bimestrais`. Ele converte cada nota de string para float usando a função `map`, soma as notas e divide pelo número de notas para obter a média. Por fim, imprime a média anual formatada.