lista_produtos = [{'produto' : 'heiniken', 'quantidade' : 4, 'preço' : 23 },
                  {'produto' : 'amstel', 'quantidade' : 2, 'preço' : 13 }]

def cadastrar():


    produto = input('nome do produto: ').lower()


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




def listar(lista_produtos):
    print()
    print('---------------------')
    lista_produtos_ordenados = sorted(lista_produtos, key=lambda x: x['produto'].lower())
    for produto in lista_produtos_ordenados:
        for chave, valor in produto.items():
                print(f"  {chave.capitalize()}: {valor}")
        print('---------------------')




def pesquisar():

    produto = input('Digite o nome do produto: ')

    for i in lista_produtos:
        if i['produto'] == produto.lower():
            print()
            print("Produto encontrado!!!")
            print('---------------------')
            for chave, valor in i.items():
                print(f"  {chave.capitalize()}: {valor}")
            print('---------------------')
            break
        
    else:
        print('Produto não encontrado!!!')
        pesquisar()




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
            cadastrar()
        case 2:
            listar(lista_produtos)
        case 3:
            pesquisar()