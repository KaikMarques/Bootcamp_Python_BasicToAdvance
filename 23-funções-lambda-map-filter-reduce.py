# Funções lambda (anônimas) são funções que não tem nome e podem ser criadas e usadas no mesmo momento pois não definimos uma função previamente para usar depois, você cria e usa na mesma hora.
# Trata-se de uma expressão única numa instrução e pode ser empregada em lugares no código onde a gente não conseguiria usar uma função def comum
# Exempl: dentro de uma lista ou até dentro da chamada de outra função

# Sintaxe: lambda argumentos: expressão

# Função lambda que retorna o quadrado de um número
quadrado = lambda x: x**2

# Calculando os quadrados de uma faixa de números
# for i in range(1, 11): # range ele não itera o ultimo valor 11 sendo o stop.
#     print(quadrado(i))

# for i in range(1, 11):
#     print(quadrado(i))

# Criando uma variável que se comporta como uma função
# Verificando se o resto da divisão é igual a 0

# par = lambda x: x % 2 == 0
# print(par(8))

# Criando um programa para converter a temperatura de fahrenheit para célcius
# f: de fahrenheit, fahrenheit(f) - 32 que multiplica cinco nonos
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(322))

# Usando função map(), ela permite aplicar outra função a cada elemento de um objeto iterável
# sintaxe: map(funcao, objeto) o objeto é o que irá receber a função

# Exemplo: Quero multiplicar cada valor de uma lista por 2
# num = [1, 2, 3, 4, 5, 6, 7, 8]
# dobro = map(lambda x: x * 2, num)
# map vai aplicar a função lambda a cada um dos valores da lista e vai armazenar isso em dobro. 
# essa função map, retorna um objeto do tipo map e queremos uma lista, então irei converter para uma lista usando a func list()
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# Convertendo a lista inteira para letras maiusculas
# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# converti para lista, usei a função map para mapear cada palavra que será convertida para letra maiscula com o método str.upper, palavras indiquei onde será realizado
# maisculas = list(map(str.upper, palavras))
# print(maisculas)

# Função Filter = ela filtra elementos de uma sequência
# Sintaxe:
# filter(função, sequencia)












