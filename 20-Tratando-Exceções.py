# Uma exceção é um objeto que representa um erro que ocorreu na execução do programa
# para tratar os erros, usamos o try e o except
# Try: Vou colocar o código que eu suspeito que possa ocasionar o erro
# Except: Vou colocar o tratamento do erro
"""
            Exceções:

    Exception - classe base para todas as exceções
    ArithmeticError- Classe base para todos os erros que ocorrem em cálculos numéricos
    OverflowError - Um cálculo excedeu o limite máximo de um tipo numérico
    ZeroDivisionError - Lançada quando uma divisão ou módulo por zero é executada em tipos numéricos
    ImportError - Lançada quando uma declaração import falha
    NameError - Um identificador (nome) não foi encontrado no namespace local ou global
    IOError - Ocorre quando uma operação de E/S (entrada/saida), como ler ou escrever em um arquivo falha
    IndentationError - A identação não foi aplicada corretamente
    RecursionError - O interpretador detectou que a profundidade máxima de recursão foi excedida
    TypeError - Um argumento com um tipo inesperado foi passado para uma função
"""


def div(k, j):
    return round(k / j, 2)


if __name__ == "__main__":
    while True:
        try:
            n1 = int(input("Digite um número: "))
            n2 = int(
                input("Digite outro número: ")
            )  # O zero como denominador vai apresentar o erro ZeroDivisionError
            break  # Se o user digitar apenas num vai ser executado o break
        except (
            ValueError
        ):  # cai nesse código se o user digitar um valor que não seja num
            print("Digite apenas números!")

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print("Impossível dividir por zero!")
    except TypeError:
        print("Ocorreu um erro de tipo inesperado!")
    except:
        print("Ocorreu um erro inesperado!")  # para um erro gerérico
    else:
        print(f"Resultado: {r}")
    finally:  # sempre vai ser executado tendo erro ou não
        print(f"\nFim do programa!")
