import sqlite3

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        query = '''
        INSERT INTO products (product_id, product_name, price)
        VALUES (?, ?, ?);
        '''
        self.cursor.execute(query, (product_id, product_name, price))
        self.conn.commit()

    def update_product(self, product_id, new_product_name, new_price):
        query = '''
        UPDATE products
        SET product_name = ?, price = ?
        WHERE product_id = ?;
        '''
        self.cursor.execute(query, (new_product_name, new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        query = '''
        DELETE FROM products
        WHERE product_id = ?;
        '''
        self.cursor.execute(query, (product_id,))
        self.conn.commit()

    def select_all_products(self):
        query = '''
        SELECT * FROM products;
        '''
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        return products

    def close_connection(self):
        self.conn.close()

# 샘플 데이터 입력
product_manager = ProductManager()
sample_data = [
    (1, 'Laptop', 1200.0),
    (2, 'Smartphone', 800.0),
    (3, 'Headphones', 150.0),
    (4, 'Tablet', 500.0),
    (5, 'Camera', 1000.0),
    (6, 'Printer', 300.0),
    (7, 'Smartwatch', 200.0),
    (8, 'External Hard Drive', 150.0),
    (9, 'Bluetooth Speaker', 80.0),
    (10, 'Gaming Console', 400.0),
]

for data in sample_data:
    product_manager.insert_product(*data)

# 모든 제품 출력
all_products = product_manager.select_all_products()
print("All Products:")
for product in all_products:
    print(product)

# 제품 업데이트
product_manager.update_product(1, 'Updated Laptop', 1300.0)

# 업데이트된 제품 출력
updated_product = product_manager.select_all_products()
print("\nUpdated Product:")
for product in updated_product:
    print(product)

# 제품 삭제
product_manager.delete_product(3)

# 삭제된 제품을 제외한 모든 제품 출력
remaining_products = product_manager.select_all_products()
print("\nRemaining Products:")
for product in remaining_products:
    print(product)

# 연결 종료
product_manager.close_connection()
