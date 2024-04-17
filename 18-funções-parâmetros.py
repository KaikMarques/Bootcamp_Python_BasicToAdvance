# Outra coisa sobre as funções é que podemos utilizar parâmetros opcionais e valores padrão ao criá-las
# As vezes não preciso passar um parâmetro para a função e neste caso posso usar um valor previamente codificado

# Função é um bloco de código que executa uma determinada tarefa. ELas são uteis pois:
# Modularização permitindo criar um bloco de códigos e usar posteriormente
# Reúso de código, legibilidade

# sintaxe da função
# def <nome_função ([argumentos]):
#     <instruções>

# def mensagem(): # esta minha função ñ recebe nenhum parâmetro
#     print("Bóson Treinamentos em Tecnologia")
#     print("Curso Completo de Python.")

# Chamada da função
# mensagem()


# Função com argumetnos "argumentos = variaveis" parêmetros=valores que passo
# def soma(a, b):
#     print(a+b)

# soma(12, 7)

# No exemplo acima, o valor que foi cálculado é simplemente impresso na tela e não consigo fazer mais nada além de olhar o valor no terminal
# e talvez eu precisasse desse valor para continuar realizando um cálculo mais complexo que tem vários passos ou precisasse armazenar o valor em algum lugar
# POderia fazer com que a função RETORNE o valor para dentro de uma variável ou para outra função, bastaria utilizar a palavra chave RETURN


# Função com RETURN
# quando o código chega no return ele não lê o que estiver abaixo
# def mult(x, y):
#     return x * y # X será multiplicado com Y e vai ser guardado para ser reutilizado em outro processo

# a = 5
# b = 8
# c = mult(a, b) # Não preciso usar os mesmos nomes dos argumentos que criei na função
# print(f'O produto de {a} e {b} é {c}')


# Função que divide 2 números
# Divisão não pode ser por zero, o demoninador não pode ser 0
# Nesta versão não tratei o possivel erro de ser dividido por 0
# def div(k, j):
#     return k / j

# if __name__ == '__main__': # if name == main para indicar o ponto principal de entrada no programa e separar isso organizando melhor o código deixando as declarações de funções e outros elementos fora desta area
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')


# Versão com o tratamendo do erro com divisão por 0
# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossível dividir por zero!'

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')




# Calculando os valores de quadrados
# Funções podem passar também sequências inteiras,lista,tuplas inteiras de valores para ser trabalhadas dentro da função
# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados


# Função que escreve um caracter X numero de vezes
# def contar(num=11, caractere='+'): #argumento num é inicializado com valor 11, ao chamar a func se eu ñ passar nenhum valor diferente será usado o valor 11
#     for i in range(1, num):
#         print(caractere)

# if __name__ == '__main__':
    # opção 1
    # contar(num=8, caractere='&') # neste caso estou usando o nome do parametro/argumento e não o nome de uma variavel qualquer, pois estou substituindo o valor padrão
    # opção 2
    # contar(6, '@') # se eu quiser colocar o @ primeiro, como vai estar fora de ordem, ai seria necessário escrever os parâmetros/argumentos


x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a+b+c
    

if __name__ == '__main__':
    res = soma_mult(x,y,z) # se eu passar só 2 argumentos, vai multiplicar caindo na primeira condição. Se eu passar 3 argumentos cai na segunda condição
    print(res)















