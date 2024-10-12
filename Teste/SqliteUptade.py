import sqlite3

#Criar uma conexão com o banco de dados.
conn = sqlite3.connect('mercado.db')

#Atualizando dados na tabela

def UptVenda():
    altera_venda = input("Digite o nome do produto: ")
    altera_precoV = float(input("Digite o novo preço de venda: "))
    conn.execute(f"UPDATE stocks SET Preco_Venda = {altera_precoV} WHERE produto = '{altera_venda.capitalize()}' ")

def UptCompra():
    altera_compra = input("Digite o nome do produto: ")
    altera_precoC = float(input("Digite o novo preço de compra: "))
    conn.execute(f"UPDATE stocks SET Preco_Compra = {altera_precoC} WHERE produto = '{altera_compra.capitalize()}' ")

#Salvando as alterações
UptVenda()
UptCompra()
conn.commit()
#Fechar a conexão com o banco de dados
conn.close()