from .models import Product
def check(id, update):
    product = Product()
    current = product.get_record_by_id(2, "products")
    current = current.fetchall()
    for length in range(0, len(current)):
        print(length)