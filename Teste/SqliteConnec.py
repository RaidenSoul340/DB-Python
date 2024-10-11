import sqlite3

#Criar uma conexão com o banco de dados.
conn = sqlite3.connect('mercado.db')

#Criar uma tabela
conn.execute('''CREATE TABLE stocks (data next, produto next, Marca text, Preco_Compra real, Preco_Venda real)''')

#Salvando as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()