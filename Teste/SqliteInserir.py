import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mercado.db')

def inserir():
    data = input("Digite a data: ")
    produto = input("Nome do produto: ")
    Marca = input("Digite a Marca do produto: ")
    Preco_Compra = float(input("Por quanto você comprou: "))
    Preco_Venda = float(input("Digite o valor de venda: "))

    conn.execute(f"INSERT INTO stocks VALUES ('{data}', '{produto.capitalize()}', '{Marca.capitalize()}', '{Preco_Compra}', {Preco_Venda})")
    conn.commit()

inserir()
conn.close()