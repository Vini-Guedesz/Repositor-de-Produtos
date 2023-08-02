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




def listar():
    print()
    print('---------------------')
    lista_produtos_ordenados = sorted(lista_produtos, key=lambda x: x['produto'].lower())
    for produto in lista_produtos_ordenados:
        for chave, valor in produto.items():
                print(f"  {chave.capitalize()}: {valor}")
        print('---------------------')




def pesquisar():

    produto = input('Digite o nome do produto: ')

    for dicionário in lista_produtos:
        if dicionário['produto'] == produto.lower():
            print()
            print("Produto encontrado!!!")
            print('---------------------')
            for chave, valor in dicionário.items():
                print(f"  {chave.capitalize()}: {valor}")
            print('---------------------')
            break
        
    else:
        print('Produto não encontrado!!!')
        pesquisar()




def alterar():

    produto = input('Digite o nome do produto: ')
    
    for i in lista_produtos:
        if i['produto'] == produto.lower():
            print()
            print("Produto encontrado!!!")
            print('======================')
            print("[1] Alterar nome do produto")
            print("[2] Alterar quantidade do produto")
            print("[3] Alterar preço do produto")
            print('======================')

            modificador = int(input('o que alterar no produto?'))

            
            match modificador:
                case 1:   
                    novo_nome = input('digite o novo nome: ')
                    i['produto'] = novo_nome
                    print('Produto aterado!!!')
                    print('---------------------')
                    for chave, valor in i.items():
                        print(f"  {chave.capitalize()}: {valor}")
                    print('---------------------')
                    break
                case 2:
                    while True:
                        nova_quantidade = input('digite a nova quantidade: ')
                        if nova_quantidade.isdigit():
                            i['quantidade'] = nova_quantidade
                            print('Produto aterado!!!')
                            print('---------------------')
                            for chave, valor in i.items():
                                print(f"  {chave.capitalize()}: {valor}")
                            print('---------------------')
                            break
                        else:
                            print('digite um valor valido!!!')
                case 3:
                    while True:
                        novo_preço = input('digite a novo preço: ')
                        if novo_preço.isdigit():
                            i['preço'] = f"{float(novo_preço):.2f}"
                            print('Produto aterado!!!')
                            print('---------------------')
                            for chave, valor in i.items():
                                print(f"  {chave.capitalize()}: {valor}")
                            print('---------------------')
                            break
                        else:
                            print('digite um valor valido!!!')
                
        
    else:
        print('Produto não encontrado!!!')
        alterar()




def remover():
    produto = input('Digite o nome do produto: ')

    for dicionário in lista_produtos:
        if dicionário['produto'] == produto.lower():
            print()
            print("Produto encontrado!!!")
            lista_produtos.remove(dicionário)
            print('Produto deletado!!!')
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
    opção = input('Escolha sua opção: ')
    if not opção.isdigit():
        print('digite um valor valido!!!')
    else:
        opção = int(opção)
        match opção:    
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                pesquisar()
            case 4:
                alterar()
            case 5:
                remover()
            case 0:
                break
            case _:
                print('Digite um valor valido!!!')