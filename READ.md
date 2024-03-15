# Curso  Python (bootcamp)

    * Curso completo em python abrangendo do básico ao avançado 

## Conteudo do Bootcamp

    * Apresentação do Curso
    * Introdução ao Python e suas aplicações
    * Instalação do Python e editor VS Code e teste
    * Editores de Código e IDEs alternativos
    * Variáveis e Tipos de Dados
    * Operadores Aritméticos
    * Operadores de Comparação
    * Operadores Lógicos AND, OR, NOT
    * Desvios Condicionais - if, elif, else
    * Saída de dados com função print, format e f-strings
    * Laço de Repetição While
    * Laço de repetição for e função range
    * Encadeamento de Laços de Repetição
    * Import de módulos e gerenciamento de pacotes com pip
    * Números aleatórios com módulo random
    * Listas
    * Tuplas
    * Funções matemáticas built-In e o módulo Math
    * Manipulação de Strings
    * Dicionários
    * Sets
    * Funções em Python - Introdução
    * Parâmetros opcionais, obrigatórios e valor padrão
    * Escopos de Variáveis - Global e Local
    * Manipulação de Exceções - Tratamento de Erros
    * Funções Recursivas
    * Funções lambda, map, filter, reduce
    * Compreensões de Lista
    * Classes, Objetos, Métodos, Atributos, Herança - POO em Python
    * Gerenciamento de pastas e arquivos do sistema com módulo os
    * Manipulação de Arquivos de Texto - Leitura e Escrita
    * Outras técnicas - generators, enumerate, with, operador ternário


## Link do video

    * Canal no youtube: Bóson Treinamentos:  https://www.youtube.com/watch?v=-VeVq64Fgw0&t=11857s

## Tratando o conteudo do curso em python

import re # é uma função da biblioteca padrão re do Python, que é usada para realizar substituições em strings usando expressões regulares.

# Seu texto
texto = """
00:00:00 Apresentação do Curso
00:00:50 Introdução ao Python e suas aplicações
00:11:33 Instalação do Python e editor VS Code e teste
00:29:35 Editores de Código e IDEs alternativos
00:39:46 Variáveis e Tipos de Dados
01:00:07 Operadores Aritméticos
01:12:34 Operadores de Comparação
01:24:33 Operadores Lógicos AND, OR, NOT
01:35:57 Desvios Condicionais - if, elif, else
01:52:02 Saída de dados com função print, format e f-strings
02:10:43 Laço de Repetição While
02:24:22 Laço de repetição for e função range
02:39:41 Encadeamento de Laços de Repetição
02:46:23 Import de módulos e gerenciamento de pacotes com pip
03:09:35 Números aleatórios com módulo random
03:25:19 Listas
03:46:40 Tuplas
04:00:05 Funções matemáticas built-In e o módulo Math
04:10:37 Manipulação de Strings
04:36:24 Dicionários
04:51:23 Sets
05:05:12 Funções em Python - Introdução
05:25:14 Parâmetros opcionais, obrigatórios e valor padrão
05:37:04 Escopos de Variáveis - Global e Local
05:48:17 Manipulação de Exceções - Tratamento de Erros
06:13:02 Funções Recursivas
06:25:58 Funções lambda, map, filter, reduce
06:50:10 Compreensões de Lista
07:03:31 Classes, Objetos, Métodos, Atributos, Herança - POO em Python
07:35:30 Gerenciamento de pastas e arquivos do sistema com módulo os
08:07:44 Manipulação de Arquivos de Texto - Leitura e Escrita
08:34:37 Outras técnicas - generators, enumerate, with, operador ternário
08:55:18 Encerramento
"""

# Expressão regular para identificar padrões de tempo HH:MM:SS
padrao = r'\b\d{2}:\d{2}:\d{2}\b' 

# Substituir os padrões de tempo por uma string vazia
novo_texto = re.sub(padrao, '', texto)

# Adicionar * ao início de cada linha
novo_texto_com_asteriscos = '\n'.join(['*' + linha for linha in novo_texto.split('\n')])

print(novo_texto_com_asteriscos)

""" 
Explicação da empressão regular r'\b\d{2}:\d{2}:\d{2}\b':

* \b: Esta é uma âncora de palavra que indica uma fronteira de palavra. Ela garante que a correspondência ocorra apenas no início ou no final de uma palavra. No caso dessa expressão regular, ela garante que o padrão de tempo seja considerado como uma palavra completa.

* \d{2}: Isso corresponde a exatamente dois dígitos (0-9). No contexto do padrão de tempo, isso corresponde a horas, minutos ou segundos.

* :: Este é um caractere literal que corresponde ao caractere de dois pontos, usado para separar as horas, minutos e segundos no formato de tempo HH:MM:SS.

* \d{2}: Outros dois dígitos (0-9), correspondendo aos minutos.

* :: Outro caractere de dois pontos, separando os minutos dos segundos.

* \d{2}: Mais dois dígitos (0-9), correspondendo aos segundos.

* \b: Outra âncora de palavra para garantir que a correspondência ocorra apenas no início ou no final de uma palavra.

Em resumo, essa expressão regular está procurando por padrões que correspondem a uma sequência de dois dígitos, seguida por dois pontos, mais dois dígitos, outro dois pontos e finalmente mais dois dígitos, garantindo que estejam encapsulados por fronteiras de palavra. Essa sequência corresponde ao formato comum de tempo no formato HH:MM:SS.

"""