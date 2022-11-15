print('Bem vindo ao Centro de Controle de Funcionários do Matheus Pulis!')

# exigencia1 cadastrar_funcionario(id)

def cadastrar_funcionário(id):
    nome = input('Por favor entre com o NOME do funcionário: ')
    setor = input('Por favor entre com o SETOR do funcionário: ')
    salario = float(input('Por favor entre com o SALÁRIO (R$): '))

    return nome, setor, salario

# exigencia2 consultar_funcionario()

def consultar_funcionario(id, nome, setor, salario):
    # exibir as opções
    while True:
        print('Escolha a opção desejada: ')
        print('1 - Consultar todos os funcionários')
        print('2 - Consultar funcionario por id')
        print('3 - Consultar funcionario por setor')
        print('4 - Retornar')
        opcao = int(input('>>: '))
        n = len(id)

        if opcao == 1:
            for i in range(n):
                print('ID: {}'.format(id[i]))
                print('NOME: {}'.format(nome[i]))
                print('SETOR: {}'.format(setor[i]))
                print('SALÁRIO: {:.2f}'.format(salario[i]))
        elif opcao == 2:
            funcionarioProcurado = int(input('Digite o ID do funcionário: '))
            # encontrar - usar contador
            contador = 0 
            for i in range(n):
                if (funcionarioProcurado == id[i]):
                    contador += 1
                    print('ID: {}'.format(id[i]))
                    print('NOME: {}'.format(nome[i]))
                    print('SETOR: {}'.format(setor[i]))
                    print('SALÁRIO: {:.2f}'.format(salario[i]))
                    break
            if contador == 0:
                print('ID não cadastrado.')
        elif opcao == 3:
            funcionarioProcurado = input('Digite o SETOR do funcionário: ')
            # encontrar funcionarios do setor
            contador = 0
            for i in range(n):
                if (funcionarioProcurado == setor[i]):
                    contador += 1
                    print('ID: {}'.format(id[i]))
                    print('NOME: {}'.format(nome[i]))
                    print('SETOR: {}'.format(setor[i]))
                    print('SALÁRIO: {:.2f}'.format(salario[i]))
            if contador == 0:
                print('SETOR não cadastrado.')
        elif opcao == 4:
            break
        else:
            continue

# funcao remover funcionário

def remover_funcionario():
    Id_Remover = int(input('Digite o ID do funcionário a ser removido: '))
    Id_Remover -= 1

    # remover todas entradas relacionadas ao ID
    del (id[Id_Remover])
    del (nome[Id_Remover])
    del (setor[Id_Remover])
    del (salario[Id_Remover])

# executando tudo

contador = 0
id = []
nome = []
setor = []
salario = []

# while loop para exibir as opções ate que se execute sair

while True:
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar funcionário')
    print('2 - Consultar funcionários')
    print('3 - Remover funcionário')
    print('4 - Sair')
    opcao2 = int(input('>>: '))

    if opcao2 == 1:
        print('Você selecionou a opção CADASTRAR FUNCIONÁRIO')
        contador += 1
        print('ID do funcionário: 00{}'.format(contador))
        novoNome, novoSetor, novoSalario = cadastrar_funcionário(contador)
        # inserir o cadastro no banco de dados
        id.append(contador)
        nome.append(novoNome)
        setor.append(novoSetor)
        salario.append(novoSalario)

    elif opcao2 == 2:
        print('Você selecionou a opção CONSULTAR FUNCIONÁRIO')
        consultar_funcionario(id,nome,setor,salario)

    elif opcao2 == 3:
        print('Você selecionou a opção REMOVER FUNCIONÁRIO')
        remover_funcionario()

    elif opcao2 == 4:
        ('Você escolheu SAIR. O programa será fechado.')
    else:
        print('Opção inválida, tente novamente.')
        continue
