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
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__': # se o nome invocado for o programa principal
    valores = [2,5,7,9,12]

    
    resultados = quadrado(valores) # var resultado recebe o retorno do chamado dessa função quadrado, passando como argumento a lista valores
    for g in resultados:
        print(g)








