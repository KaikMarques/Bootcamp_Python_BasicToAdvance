# Funções lambda (anônimas) são funções que não tem nome e podem ser criadas e usadas no mesmo momento pois não definimos uma função previamente para usar depois, você cria e usa na mesma hora.
# Trata-se de uma expressão única numa instrução e pode ser empregada em lugares no código onde a gente não conseguiria usar uma função def comum
# Exempl: dentro de uma lista ou até dentro da chamada de outra função

# Sintaxe: lambda argumentos: expressão

# Função lambda que retorna o quadrado de um número
quadrado = lambda x: x**2

# Calculando os quadrados de uma faixa de números
# for i in range(1, 11): # range ele não itera o ultimo valor 11 sendo o stop.
#     print(quadrado(i))
