import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mercado.db')

#===============================================#
def LerTodas():
    #Selecionando todos os dados da tabela
    ver = conn.execute("SELECT * from stocks")

    #Iterar sobre os dados e exibi-los
    for row in ver:
        print(row)
#-----------------------------------------------#
def LerProduto():
    #Selecionando todos os dados da coluna produto
    verP = conn.execute("SELECT produto FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowP in verP:
        print(rowP)
#-----------------------------------------------#
def LerData():
    #Selecionando todos os dados da coluna data
    verD = conn.execute("SELECT data FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowD in verD:
        print(rowD)
#-----------------------------------------------#
def LerMarca():
    #Selecionando todos os dados da coluna Marca
    verMar = conn.execute("SELECT Marca FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowMar in verMar:
        print(rowMar)
#-----------------------------------------------#
def LerPrecoCompra():
    #Selecionando todos os dados da coluna Preco_Compra
    verComp = conn.execute("SELECT Preco_Compra FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowComp in verComp:
        print(rowComp)
#-----------------------------------------------#
def LerPrecoVenda():
    #Selecionando todos os dados da coluna Preco_Venda
    verVend = conn.execute("SELECT Preco_Venda FROM stocks")

    #Iterar sobre os dados e exibi-los
    for rowVend in verVend:
        print(rowVend)
#===============================================#
LerTodas()
LerProduto()
LerMarca()
LerData()
LerPrecoCompra
LerPrecoVenda
conn.close()