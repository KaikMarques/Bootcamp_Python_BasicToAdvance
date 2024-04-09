# Sets são conjuntos/coleções não ordenadas de valores unicos que usamos para armazenar múltiplos itens dentro de um objeto
# Eles armazenam apenas itens não duplicados e suportam operações matemáticas sobre conjuntos união, intersecção...
# Não conseguimos modificar os itens porém conseguimos adicionar novos elementos
# O conjunto do set é mutável e podemos armazenar elementos de qualquer tipo


# Ele é diferente de um dicionário, pois não trabalha com chave:valor
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))
# print('Lua' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper(), " ", end='') # o end faz com que seja impresso tudo na mesma linha, o coloquei o espaço se não seria impresso tudo junto

# Transformando uma lista em Set/conjunto
# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua'] # Quando for imprimido, vai aparecer sómente 1 lua, pois valores iguais no conjunto se refere ao mesmo valor
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Comenta de Halley'}

# Utilizando operador de comparação
print(astros1 != astros2)

# Utilizando operador de união
print(astros1 | astros2)
print(astros1.union(astros2))

# Fazendo intersecção dos conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

# Verificando a diferença simétrica de um conjunto. Traz os elementos que não aparecem em ambos os conjuntos
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

# Adicionando elementos. Os elementos do conjunto vem sempre em ordem aleatória
astros1.add('Urano')
astros2.add('Sol')

# Removendo os elementos
astros1.remove('Io')
astros1.remove('Plutão') # vai dar erro, pois não está no conjunto
astros1.discard('Plutão') # neste método, se o elemento não estiver no conjunto não vai ser apresentado erro
astros1.pop() # Remove um dos elementos do conjunto em ordem aleatória
astros1.clear() # Limpando todo o conjunto











