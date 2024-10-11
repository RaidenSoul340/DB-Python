import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#Selecionando todos os dados da tabela
cursor = conn.execute("SELECT * from stocks")

#Iterar sobre os dados e exibi-los
for row in cursor:
    print(row)

#Fechar a conexão com o banco de dados
conn.close()


