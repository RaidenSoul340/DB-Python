import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')





#Inserir dados na tabela
conn.execute("INSERT INTO stocks VALUES ('{}', '{}', '{}', '{}', {})")


#Salvar as alterações
conn.commit()

#Fechar a conexão com o banco de dados
conn.close()
