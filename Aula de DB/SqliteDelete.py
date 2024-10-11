import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Deletar dados com o banco de dados
conn.execute("DELETE from stocks WHERE symbol = 'IBM'")

#Salvar as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()




