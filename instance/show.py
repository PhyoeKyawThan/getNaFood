import sqlite3

class Connect:
    def __init__(self)->None:
        self.conn = sqlite3.connect('data.db')
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
    def get_record(self, table_name:str)->object:
        return self.cursor.execute(f"select * from {table_name}")
    
    def close(self)->str:
        self.cursor.close()
        self.conn.close()
        return " all Conn closed"

class User(Connect):
    def insert(self, new_user:tuple)->bool:
        self.cursor.execute("insert into user(username, email, password) values(?, ?, ?)", new_user)
        self.conn.commit()
        return True
    
class Order(Connect):
    def insert(self,user_id:int, item_name: str = None, order_count:int = None, price:float = None)->bool:
        datas = (user_id, item_name, order_count, price)
        self.cursor.execute("insert into orders(user_id, item_name, order_count, price) values(?,?,?,?)",datas)
        self.conn.commit()
        return True


if __name__ == '__main__':
    conn = Connect()
    for x in conn.get_record("user"):
        print(x)
    conn.close()
    
