# Escopo ele vai indicar a visibilidade de uma variável dentro do código
# Existe Escopo Local e Escopo Global

# Var de escopo local é geralmente criando dentro de uma função/rotina e ela existe somente dentro da função onde foi declarada
# Var de escopo global é declarada fora das funções e pode ser acessada por todo o código

var_global = 'Curso Completo de Python'

def escreve_texto():
    # mesmo var_global tendo o mesmo nome foi criado uma var nova apontando para um novo endereço de memória
    # var_global = 'Banco de Dados com SQL' # na chamada da função vai aparecer essa info, porém quando eu usar a var_global fora da func vai aparecer outra info
    # neste caso devo especificar que a seguinte variável é global:
    global var_global
    var_global = 'Banco de Dados com SQL' # agora, foi atribuido um novo valor para a mesma var, tanto a da func como a fora dela terá a mesma info
    var_local = "Kaik Xavevier"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

# Criando a rotina principal do programa
if __name__ == "__main__":
    print(f'Executar a função escreve texto()')
    escreve_texto()

















































