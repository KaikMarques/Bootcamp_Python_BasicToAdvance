# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1, n2 = map(float, input("Entre com a primeira e segunda nota, separado pelo espaço: ").strip().split())
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# Calcular a média artmética das notas
media = (n1 + n2) / 2

if (media >= 7): # Os dois pontos é um caracter para delimitação de blocos dizendo o que está dentro do if
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("Você está de recuperação")
else:
    print("Aluno reprovado...")


print("Sua média é {}".format(media)) # em format(media) vai aparecer dentro das chaves