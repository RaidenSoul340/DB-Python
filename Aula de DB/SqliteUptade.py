import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Atualizar dados na tabela
conn.execute("UPDATE stocks SET price = 53.00 WHERE symbol = 'RHAT'")

#Salvando as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()
