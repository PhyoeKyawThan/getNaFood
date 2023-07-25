from . import app
import sqlite3

class Connect:
    def __init__(self)->None:
        self.conn = sqlite3.connect(app.config["DATABASE_URI"])
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
                            FOREIGN KEY(user_id) REFERENCES user(id),
                            FOREIGN KEY(item_name) REFERENCES products(product_name)
                            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            product_name varchar(100) NOT NULL,
                            description varchar(255),
                            price INTEGER,
                            count INTEGER,
                            product_img varchar(225)
        )""")

    def get_record(self, table_name:str)->object:
        return self.cursor.execute(f"select distinct * from {table_name}")
    
    def get_record_by_id(self, id:int, table_name:str)->object:
        return self.cursor.execute(f"select * from {table_name} where id = {id}")
    
    def get_product(self, product_name: str):
        return self.cursor.execute(f"select * from products where product_name = '{product_name}'")
    def get_order_by_user(self, username:str):
        return self.cursor.execute(f"select orders.id, orders.item_name, orders.order_count from orders, user where user.username = '{username}' and user.id = orders.user_id")
    
    def get_order_item_name(self, order_id:int)->str:
        return self.cursor.execute(f"select item_name from orders where id = {order_id}")
    def close(self)->str:
        self.cursor.close()
        self.conn.close()
        return " all Conn closed"

class User(Connect):
    def insert(self, new_user:tuple)->bool:
        self.cursor.execute("insert into user(username, email, password) values(?, ?, ?)", new_user)
        self.conn.commit()
        return True
    def get_user_id_by_name(self, username: str)->int:
        return self.cursor.execute(f"select id from user where username = '{username}'")

    def delete_user(self, username: str)->bool:
        self.cursor.execute(f"delete from user where username='{username}'")
        self.conn.commit()
        return True
    def delete_user_order(self, user_id: int)->bool:
        self.cursor.execute(f"delete from orders where user_id='{user_id}")
        self.conn.commit()
        return True

class Order(Connect):
    def insert(self,user_id:int, item_name: str = None, order_count:int = None)->bool:
        datas = (user_id, item_name, order_count)
        self.cursor.execute("insert into orders(user_id, item_name, order_count) values(?,?,?)",datas)
        self.conn.commit()
        return True
    def order_count(self, order_id:int)->int:
        return self.cursor.execute(f"select order_count from orders where id = {order_id}").fetchone()[0]
    def order_confirm(self, user_id, order_id, item_name, count)->bool:
        self.cursor.execute(f"update products set count = count - {count} where product_name = '{item_name}'")
        self.cursor.execute(f"delete from orders where user_id = {user_id} and id = {order_id}")
        self.conn.commit()
        return True
    def cancal_order(self, user_id:int, order_id:int)->bool:
        self.cursor.execute(f"delete from orders where user_id = {user_id} and id = {order_id}")
        self.conn.commit()
        return True
    
class Product(Connect):
    def insert(self, product_name: str='', description: str='', price: int = 0, count: int = 0, product_img: str='')->bool:
        datas = (product_name, description, price, count, product_img)
        self.cursor.execute("insert into products(product_name, description, price, count, product_img) values(?, ?, ?, ?, ?)", datas)
        self.conn.commit()
        return True
    def get_count(self, item_name:str)->int:
        return self.cursor.execute(f"select count from products where product_name = '{item_name}'")
    def update_product(self, id: int, *args)->bool:
        for x in args:
            self.cursor.execute(f"update products set {x[0]} = {x[1]} where id = {id}")
            self.conn.commit()
        return True

    def delete_product(self, product_name: int, id: int = 0)->bool:
        self.cursor.execute(f"delete from products where product_name = '{product_name}'")
        self.conn.commit()
        return True

if __name__ == '__main__':
    product = Product()
    product.insert("Phyoe Kyaw Than", "A valuabel product for ur INfo")
    get_data = product.get_record("products")
    get_data = get_data.fetchall()
    print(get_data)
    product.close()
    
