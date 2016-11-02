import sqlite3

connect = sqlite3.connect('01.db')

# creat table
# connect.execute('''create table company (id int primary key not null, 
# 	name text not null, age int not null, address char(50),salary real);''')

# insert data
# connect.execute('''insert into company values(101, 'apple', 18, 'haven', 10)''')
# connect.commit()

select = connect.execute('select * from company')
for x in select:
	print x

connect.close()