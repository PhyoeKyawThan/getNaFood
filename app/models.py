import sqlite3

class Connect:
    def __init__(self)->None:
        self.conn = sqlite3.connect("database/data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            username VARCHAR(20) NOT NULL,
                            email VARCHAR(50) NOT NULL,
                            password VARCHAR(100) NOT NULL
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                            user_id INTEGER,
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_name VARCHAR(20), 
                            order_count INTEGER,
                            price INTEGER,
                            FOREIGN KEY(user_id) REFERENCES user(id)
                            )""")
    def show(self, table_name:str)->object:
        return self.cursor.execute(f"select * from {table_name}")
    
    def close(self)->str:
        self.cursor.close()
        self.conn.close()
        return " all Conn closed"

class User(Connect):
    def insert(self, username:str, email:str, password:str)->bool:
        new_user = (username, email, password)
        self.cursor.execute("insert into user(username, email, password) values(?, ?, ?)", new_user)
        self.conn.commit()
        return True
    
class Order(Connect):
    # def __init__(self)->None:
    #     self.cursor.execute("""create table if not exists order(
    #                         user_id integer,
    #                         id primary key autoincrement,
    #                         item_name varchar(20), 
    #                         order_count integer,
    #                         price numeric(10, 2),
    #                         foreign key(user_id) references user(id)
    #                         )""")

    def insert(self,user_id:int, item_name: str = None, order_count:int = None, price:float = None)->bool:
        datas = (user_id, item_name, order_count, price)
        self.cursor.execute("insert into orders(user_id, item_name, order_count, price) values(?,?,?,?)",datas)
        self.conn.commit()
        return True


if __name__ == '__main__':
    order = Order()
    user = order.cursor.execute("select id from user where username = 'domak'")
    # user.insert("domak", "domak@gmail.com", "password")
    user = order.cursor.fetchone()[0]
    order.insert(user, "apple", 5, 4)
    for x in order.show(table_name="orders"):
        print(x)
    order.close()
