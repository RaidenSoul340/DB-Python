import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mercado.db')
#===================================================================#
#Adicionando produto e suas informações
def inserir():
    data = input("Digite a data: ")
    produto = input("Nome do produto: ")
    Marca = input("Digite a Marca do produto: ")
    Preco_Compra = float(input("Por quanto você comprou: "))
    Preco_Venda = float(input("Digite o valor de venda: "))

    conn.execute(f"INSERT INTO stocks VALUES ('{data}', '{produto.capitalize()}', '{Marca.capitalize()}', '{Preco_Compra}', {Preco_Venda})")
    conn.commit()
#===================================================================#
#Mostrando os produtos
def LerTodas():
    #Selecionando todos os dados da tabela
    ver = conn.execute("SELECT * from stocks")

    #Iterar sobre os dados e exibi-los
    for row in ver:
        print(row)
#-------------------------------------------------------------------#
def LerProduto():
    #Selecionando todos os dados da coluna produto
    verP = conn.execute("SELECT produto FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowP in verP:
        print(rowP)
#-------------------------------------------------------------------#
def LerData():
    #Selecionando todos os dados da coluna data
    verD = conn.execute("SELECT data FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowD in verD:
        print(rowD)
#-------------------------------------------------------------------#
def LerMarca():
    #Selecionando todos os dados da coluna Marca
    verMar = conn.execute("SELECT Marca FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowMar in verMar:
        print(rowMar)
#-------------------------------------------------------------------#
def LerPrecoCompra():
    #Selecionando todos os dados da coluna Preco_Compra
    verComp = conn.execute("SELECT Preco_Compra FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowComp in verComp:
        print(rowComp)
#-------------------------------------------------------------------#
def LerPrecoVenda():
    #Selecionando todos os dados da coluna Preco_Venda
    verVend = conn.execute("SELECT Preco_Venda FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowVend in verVend:
        print(rowVend)
#===================================================================#
#Função pra visualizar todas as informações
def VisualizarTudo():
	while True:
            print('''
                  1-Ver Todos os Produtos
                  
                  2-Ver Produtos
                  
                  3-Ver Datas
                  
                  4-Ver Marcas
                  
                  5-Ver Preço de Compra dos Produtos
                  
                  6-Ver Preço de Venda dos Produtos
                  
                  7-Encerrar
                  ''')
            
            ver = input("Digite um número: ")
            
            if ver == '1':
                LerTodas()
                conn.close
                
            elif ver == '2':
                LerProduto()
                conn.close

            elif ver == '3':
                LerData()
                conn.close()

            elif ver == '4':
                LerMarca()
                conn.close()

            elif ver == '5':
                LerPrecoCompra()
                conn.close()


            elif ver == '6':
                LerPrecoVenda()
                conn.close()

            elif ver == '7':
                break

            else: 
                print("Valor desconhecido! Por favor tente novamente")
#===================================================================#
#Atualizar Dados da Tabela

#Atualizando o Preco de Venda
def UptVenda():
    altera_venda = input("Digite o nome do produto: ")
    altera_precoV = float(input("Digite o novo preço de venda: "))
    conn.execute(f"UPDATE stocks SET Preco_Venda = {altera_precoV} WHERE produto = '{altera_venda.capitalize()}' ")
#-------------------------------------------------------------------#
#Atualizando o Preco de Compra
def UptCompra():
    altera_compra = input("Digite o nome do produto: ")
    altera_precoC = float(input("Digite o novo preço de compra: "))
    conn.execute(f"UPDATE stocks SET Preco_Compra = {altera_precoC} WHERE produto = '{altera_compra.capitalize()}' ")
#-------------------------------------------------------------------#
def AtualizarDados():
    while True:
        print("1-Atualizar preços de venda")
        print("2-Atualizar preços de compra")
        print("3-Encerrar")
		
        atualizar = input("Escolha qual deseja atualizar: ")
		
        if atualizar == '1':
            UptVenda()

        elif atualizar == '2':
            UptCompra()

        elif atualizar == '3':
            print("Encerrando")
            break
        else:
            print("Valor Errado!")
#===================================================================#
#Deletando produtos na tabela:
def deleteProduto():
    deletePro = input("Digite o nome do produto que deseja deletar: ")
    
    conn.execute(f"DELETE from stocks WHERE produto = '{deletePro.capitalize()}' ")

#===================================================================#
while True:
    print("Lista de Informações de Produtos")
    print('''
          1-Adicionar Produtos
          
          2-Ver Produtos 
          
          3-Atualizar Produtos 
          
          4-Deletar Produtos
          
          5-Finalizar Operação
          ''')

    esc = input("Digite o número da ação que deseja realizar: ")
    
    if esc == '1':
        inserir()
        conn.commit()       
        conn.close()
        
    elif esc == '2':
        VisualizarTudo()
        conn.commit()
        conn.close()

    elif esc == '3':
        AtualizarDados()
        conn.commit()
        conn.close()

    elif esc == '4':
        deleteProduto()
        conn.commit()
        conn.close()

    elif esc == '5':
        print("Finalizado")
        break
    
    else:
        print("Valor errado tente novamente!")