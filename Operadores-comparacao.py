x = z = y = False
n1 = n2 = 0

# Forma simples
print("Digite um número: ")
n1 = int(input())
n2 = int(input("Digite outro número: "))

# Forma com métodos
#n1, n2 = map(float, input("Digite 2 números diferentes separados por espaço: ").strip().split())

x = n1 == n2
print("São iguais? ", x, '\n') #\n é quebra de linha

z = n1 > n2
print(n1, ' é maior que ', n2, '? ', z, '\n')

y = n1 !=n2
print('São diferentes?' + str(y)) # Minha variável Y é um booleano, esse tipo só pode ser concatenado com o uso de strings "str". A virgula permite qualquer tipo, porém o sinal de mais é com o uso de str