# Recursividade é um método para simplificação de problemas que consiste em dividir um problema em subproblemas menores más sempre do mesmo tipo
# os subproblemas são resolvidos e os resultados de cada subproblema são passados para o problema principal combinando os resultados até que o problema geral
# seja resolvido
#  Uma função recursiva é uma função que chama a si mesma quando ela é invocada

# Criando exemplo de cálculo recursivo de uma função que cálcula o fatorial de um num fornecido de forma recursiva
# Recursividade

# Formula geral para o fatorial
# fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'
# fatorial (num) = num * fatorial(num - 1), se num > 1 'Caso Recursivo' esse caso vai chamar a si mesmo varias vezes até chegar no caso base

# Cálculando o fatorial de 4
# 4! => 4 * fatorial(3) # Se lê: 4! = 4 * 3
# explicando: Caso recursivo,  4* fatorial (3). Pela minha regra do caso recursivo se o num for diferente de 0 ou 1, ele vai multiplicar o num por fatorial(num - 1) assim sendo o 3
# 4! => 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) =>
# 4! = 4 * 3 * 2 * 1 = 24
# ele vai chamando a própria função que cálcula o fatorial diversas vezes e cada vez que é chamado ele vai multiplicar o num por o fatorial do num anterior e assim sendo o 24
# até chegar no valor do caso base e assim terei o resultado final calculado


# Criando exemplo de cálculo recursivo de uma função que cálcula o fatorial de um num fornecido de forma recursiva
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


# Neste código se eu tentar com muitos num ou num negativo vai me voltar um erro
# if __name__ == "__main__":
#     x = int(input("Digite um número positivo:"))
#  em res que está o erro sendo assim vou lançar uma exceção
#     res = fatorial(x)
#     print(f"O fatorial de {x} é {res}")


if __name__ == "__main__":
    x = int(input("Digite um número positivo:"))
    try:
        res = fatorial(x)
    except RecursionError:
        print("Impossível cálcular o fatorial de um número negativo ou muito grande!")
    else:
        print(f"O fatorial de {x} é {res}")
