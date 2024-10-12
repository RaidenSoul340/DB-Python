import sqlite3

#Criar uma conexão com o banco de dados.
conn = sqlite3.connect('mercado.db')

def deleteProduto():
    deletePro = input("Digite o nome do produto que deseja deletar: ")
    
    conn.execute(f"DELETE from stocks WHERE produto = '{deletePro.capitalize()}' ")

deleteProduto()
conn.commit()
conn.close()