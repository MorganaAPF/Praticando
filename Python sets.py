"""Exercício: Análise de Dados de Clientes

Você trabalha em uma empresa de e-commerce e sua tarefa é analisar a lista de clientes que realizaram compras em dois períodos 
diferentes. Você tem duas listas: uma com clientes que compraram em janeiro e outra com clientes que compraram em fevereiro. Você deve
identificar clientes que:

Compraram em ambos os meses.
Compraram apenas em janeiro.
Compraram apenas em fevereiro.
Todos os clientes únicos nos dois meses."""

clientes_janeiro = {'Alice', 'Bob', 'Carlos', 'Daniela', 'Eduardo'}
clientes_fevereiro = {'Carlos', 'Daniela', 'Felipe', 'Gabriela', 'Alice'}
clientes_ambos = clientes_janeiro & clientes_fevereiro
clientes_total = clientes_janeiro.union(clientes_fevereiro)
onlyjan = clientes_janeiro - clientes_fevereiro
onlyfeb = clientes_fevereiro - clientes_janeiro

print(f'Clientes que compraram em ambos os meses: {clientes_ambos}')
print(f'Clientes que compraram apenas em janeiro: {onlyjan}')
print(f'Clientes que compraram apenas em fevereiro: {onlyfeb}')
print(f'Todos os clientes únicos: {clientes_total}')
