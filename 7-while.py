
# Laço While: Um teste lógico é realizado no inicio do loop do laço e sempre que retornar verdadeiro 
# executa os comando no bloco, só para quando retorna falso

#Imprimindo números de 1 a 10

# num = 1

# while (num <= 10):
#     print(num)
#     num += 1 # está incrementando mais 1 ao valor da variavel
# print("Laço encerrado!")

""" Fazendo um programa que pergunte o nome do usuário com mensagem de boas vindas para um número indetermidado de usuários,
Só para quando alguém aperta X
"""

nome = None # como não tenho o nome do usuário, estou iniciando ela com o tipo NONE = nada

while True:
    print("Digite seu nome, ou X para parar: ")
    nome = input()
    if nome == 'x' or nome == 'X': # Em Python tem diferença letra maiuscula ou minuscula
        break # Quando cair nessa condição ele para o laço
    print(f"Bem-Vindo", {nome}) # fiz o uso de F-String
print("Até logo")
