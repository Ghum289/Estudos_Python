import sqlite3

banco = sqlite3.connect("primeiro_banco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)" )

#tipos de dados em sqlite3

""" null - valor nulos
integer - interiros
real - ponto flutuante
text - texto
blob - Dado binário(imagens, arquivos, qualquer coisa).
""" 
cursor.execute('INSERT INTO pessoas VALUES("Joao",20,"joao@gmail.com")')

banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
