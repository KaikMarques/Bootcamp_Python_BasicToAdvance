"""_summary_
    Suponha que temos um programa que realiza um cálculo, e esse cálculo só funciona se for fornecidos valores positivos. Se for digitado um valor negativo ocorrerá um erro
    que pode travar minha aplicação. Para tratar esse erro, eu posso usar a palavra chave Raise.
"""

from math import sqrt

# em raiz quadrada não existe numero negativo, sendo assim não quero que o user forneça um número negativo


class NumeroNegativoError(
    Exception
):  # Criei a minha própria classe para tratar erro e disse da onde ela vem sendo Exception
    def __init__(self):
        pass  # Está dizendo para ignorar e passar adiante, da familia de continue e break


if __name__ == "__main__":

    while True:
        try:
            num = int(input("Digite um número positivo: "))
            if num < 0:
                raise NumeroNegativoError  # Lançamdo o erro aritmético
        except NumeroNegativoError:
            print("Foi passado um número negativo!")
        else:
            print(f"A raiz quadrada de {num} é {sqrt(num)}")
        finally:
            print(f"Fim do cálculo.")
