import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host=" localhost",  
        user="root",
        password="123456789",
        database="bhola"
    )

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bhola (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def add_product(product_name, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bhola (product_name, quantity, price) VALUES (%s, %s, %s)", 
                   (product_name, quantity, price))
    conn.commit()
    cursor.close()
    conn.close()

def display_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bhola")
    products = cursor.fetchall()
    for product in products:
        print(product)
    cursor.close()
    conn.close()

def update_product(id, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE bhola SET quantity = %s, price = %s WHERE id = %s", 
                   (quantity, price, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_product(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bhola WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()

    
    add_product('Product1', 10, 9.99)
    add_product('Product2', 20, 19.99)
    add_product('Product3', 20, 19.11)
    
    print("All Products:")
    display_products()
    
    
    update_product(1, 15, 14.99)
    
    print("Products after update:")
    display_products()
    
    
    delete_product(2)
    
    print("Products after deletion:")
    display_products()
