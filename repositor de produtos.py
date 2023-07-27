lista_produtos = []

def cadastrar_produto():


    produto = input('nome do produto: ')


    while True:
        preço = input('preço do produto: ').replace(',' , '')
        if preço.isdigit() and float(preço) > 0:
            break
        else:
            print('digite um valor valido!')


    while True:
        quantidade = input('quantidade do produto: ')
        if quantidade.isdigit() and int(quantidade) > 0:
            break
        else:
            print('digite um valor valido!')
        

    dicionario_produto = {
        'produto' : produto,
        'quantidade' : int(quantidade),
        'preço' : f"{float(preço):.2f}"
    }
    

    lista_produtos.append(dicionario_produto)
    print('produto registrado com sucesso!!!')




def menu():
    print('======================')
    print("[1] Cadastrar Produto")
    print("[2] Listar Produtos")
    print("[3] Pesquisar Produto")
    print("[4] Alterar Produto")
    print("[5] Remover Produto")
    print("[0] Sair do programa")
    print('======================')





while True:
    menu()
    opção = int(input('Escolha sua opção: '))
    match opção:    
        case 1:
            cadastrar_produto()