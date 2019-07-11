import sqlite3
connect = sqlite3.connect('hw4t2.sqlite')
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (id text, name text, address text)")
connect.close()
class User:
    def __init__(self, id):
        self.id = id#
        self.name = Column()#
        self.address = Column()#




class Column:
    def __init__(self, id, data):
        self.id = User.id
    def __get__(self, instance, owner):
        connect = sqlite3.connect('hw4t2.sqlite')
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Users (id text, name text, address text)")
        pass

    def __set__(self, instance, value):
        connect = sqlite3.connect('hw4t2.sqlite')
        cursor = connect.cursor()
        cursor.execute(
            """INSERT
         INTO Users({instance}) 
         VALUES ({value})"""
        )
        connect.commit()
        connect.close()


    def __delete__(self, instance):
        pass

    def __set_name__(self, owner, name):
        print(f'It is {name} attribute')
