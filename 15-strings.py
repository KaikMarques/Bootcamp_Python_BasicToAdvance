"""
São sequências de caracteres, são extremamente importantes pois elas permite que seja armazenado dados textuais em variáveis e processe esses dados.
 Elas são sequências assim como listas, tuplas e etc... Conseguimos acessar no python cada caractere por um número de índice e as strings são imutáveis
uma vez que foi criado uma vez criado eu não consigo alterar o conteúdo de uma string, más consigo alterar o conteúdo de uma variável que contém a string

"""



# nome = 'Curso de Python'
# letra = nome[2] # acessando o conteudo da string por indice, será impresso a letra b
# frase = 'Vamos aprender Python hoje'
# palavras = frase.split() # split() = divide a string em partes separadas por espaço por padrão criando assim uma lista de Strings
# print(palavras) # ['Vamos', 'aprender', 'Python', 'hoje'] cada palavra separada por espaço se transformou em item de uma lista e agora consigo acessar as palavras individualmente com mais facilidade
# print(palavras[1]) # aprender será o resultado, porque estou acessando o que está no indice 1 da minha lista
# for palavra in palavras:
#     print(palavra) # resultado será uma palavra impressa abaixo da outra

# for letra in frase:
#     print(letra) # vai imprimir cada letra, porque na var frase não foi usado o método split


# Slicing / Fatiamento nas strings
# print(frase[0:5]) # Vamos será impresso com um espaço
# print(frase[-3:]) # je. será retornado, sendo os 3 ultimos caracteres da string

 # Usando o Slicing com o método Find
# email = input('Digitte seu endereço de e-mail: ')
# arroba = email.find('@') # pedindo para encontrar em qual indice está o caracter @
# print(arroba) # vai retornar o indice do meu arroba
# separando o usuario e o dominio usando slicing
# usuario = email[0:arroba] # vai retornar do indice 0 até o conteudo da variavel arroba
# dominio = email[arroba+1:] # vai retornar do conteudo da variavel arroba até o final. OBs: arroba+1 pula o @, para imprimir ele devo tirar o +1
# print(usuario) # exem: kaik
# print(dominio) # exem: @hotmail.com

 # Usando operadores de associação IN, NOT IN para verificar se um caracter ou a sequencia do mesmo está dentro de uma string
# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos) # retorna true
# print('magnésio' not in produtos) # retorna true

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos) # retorna a posição apartir da onde encontrou o valor
# pos = item.find('flu')
# print(pos) # vai retornar -1 querendo dizer que não encontrou o valor


 # Trabalhando com maiusculos e minusculos também
# objeto_celeste = 'galaxia esPiral M31'
# print(objeto_celeste.upper()) # tudo maiusculo
# print(objeto_celeste.lower()) # tudo minusculo
# print(objeto_celeste.capitalize()) # primeira letra maiuscula
# print(objeto_celeste.title()) # primeira letra de cada palavra em maiusculo

 # Substituindo strings
# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco') # alterando o valor
# print(suplemento)
# print(n_suplemento)

 # Trabalhando com espaços em branco
# frase = '     Ômega 3 é bom para a saúde!    '
# print(frase)
# print(frase.lstrip) # remove os espaço a esquerda
# print(frase.rstrip)# remove os espaço a direta
# print(frase.strip) # remove todos os espaços

 # Trabalhando com alinhamento de texto para exibição
# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20)) # rjust é justificar a direta e dentro do () passei meus argumentos sendo o número de caracteres ao usar sendo, use 20 espaço para escrever a palavra abacate e alinhe a direta
# print(fruta.center(20, '-')) # linha no centro da tela com traços a esquerda e direita
# print(fruta.ljust(20, '-')) # mesma função do r porém neste caso a esquerda e preenche usando os traços

 # Trabalhando co prefixos e sufixos. Verificando se a string inicia ou termina com uma sequencia de char
# p = 'Bóson Treinamentos'
# print(p.startswith('b')) # retorna False porq começa com B maiusculo
# print(p.endswith('o')) # retorna false por finaliza com s

 # Docstrings: usado para documentar trechos especificos no code como módulo, classe e função
texto = """
    Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no python, entre outros locais.
        Respeita deslocamento do texto e é multilinhas
"""
print(texto) # neste caso optei por deixar numa variavel












