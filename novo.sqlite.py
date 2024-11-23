import sqlite3

banco=sqlite3.connect('segundo_banco.db')

cursor=banco.cursor()

#cursor.execute("create table pessoa(nome text, idade integer, email text)")
cursor.execute("INSERT INTO pessoa VALUES('PedroM',21,'PedroM@gmail.com')")

banco.commit()

#cursor.execute("select * from pessoa")
#print(cursor.fetchall())