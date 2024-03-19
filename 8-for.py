# For: Funciona como um método iterador, permitindo executar um conjunto de comandos 
#       sobre cada item na sequencia

# for item in sequencia:
#     instruções executadas para item da sequencia
# item: é o nome da variavel
# in: é o operador de associação
# sequencia: é o conjunto de valores sobre os quais você quer aplicar algum tipo de processo
# que vai estar dentro das instruções para cada item da sequencia


# exemplo prático 1
# lista = [2,6,9,4,0,12,3,7]
# palavras = 'Bóson'
# for letra in lista: # para cada varial(letra) na lista faça alguma coisa
#     print(letra) 

# Se eu quiser imprimir uma lista de números sem precisar criar uma lista, posso usar a função RANGE

# for numero in range(1, 11): # poderia passar só 1 argumento, exemplo o número 10. Seria imprimido do numero 1 ao 9, é sempre o valor -1
#     print(numero)

# Escrevendo 10 vezes um nome fornecido pelo usuário

# nome = input("Digite seu nome: ")
# for x in range(10)
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)

# for x in range(20, 1, -2) outra possibilidade imprimindo ao contrario
# for x in range(2,20): # neste caso irá imprimir do 2 ao 19, se eu adicionar o numero 2, vai ter o incremento de 2 em 2
#     print(x)


# Quero imprimir nomes de itens contidos na lista um por linha. Se um dos nome estiver escritos na lista não deve ser impresso

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo' or 'quartzo':
        continue # Ela encerra a iteração atual do laço. A próxima instrução (quando chegar em Quartzo) dentro do for não será executada, porém o laço não termina
    print(pedra)