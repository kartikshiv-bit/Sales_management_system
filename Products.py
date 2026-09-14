from Database import conn

class Products:
    def __init__(self):
        pass
        # self.name = name
        # self.contact = contact

    @staticmethod
    def create_table():
        cur = conn.cursor() 
        cur.execute(
            """CREATE TABLE IF NOT EXISTS Products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INTEGER NOT NULL
                )"""
        )
        conn.commit()
        cur.close()
    
    @staticmethod
    def insert_product(name, description, price, quantity):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO Products(name, description, price, quantity)
            values(%s, %s, %s, %s)""",
            (name, description, price, quantity,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_product(product_id, name = None, description=None, price=None, quantity= None):
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        
        product = cur.fetchone()
        if not product:
            print(">>>>Product not found!")
            cur.close()
            return 
            
        update_fields = []

        if name:
            update_fields.append(f"name = '{name}'")
        if description:
            update_fields.append(f"description = '{description}'")
        if price:
            update_fields.append(f"price = '{price}'")
        if quantity:
            update_fields.append(f"quantity = '{quantity}'")

        update_query = f"UPDATE products SET {','.join(update_fields)} WHERE id = {product_id}"

        cur.execute(update_query)
        conn.commit()
        cur.close()

    @staticmethod
    def delete_product(product_id):
        cur = conn.cursor()
        cur.execute(
            """DELETE FROM products WHERE id = %s""",(product_id,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def view_products():
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM products """
        )
        products = cur.fetchall()
        cur.close()
        return products
    
    def view_product_id(product_id):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM products WHERE id = %s """,(product_id,)
        )
        product = cur.fetchone()
        cur.close()
        return product

    @staticmethod
    def product_menu():

        while True:
            print("1. Create Table")
            print("2. Insert Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. View Product")
            print("6. View Product by id")
            print("0. Exit")
            choice = input("Enter Choice: ")

            match (choice):

                case "1" : 
                    Products.create_table()
                    print("<<<<<< Product table created!")

                case "2" :
                    name = input("Enter Product name: ")
                    description = input("Enter Product description: ")
                    price = input("Enter Product price: ")
                    quantity = input("Enter Product quantity: ")
                    Products.insert_product(name, description, price, quantity)
                    print("<<<<<< Product created!")

                case "3" : 
                    product_id = input("Enter Product id: ")
                    name = input("Enter Product name: ")
                    description = input("Enter Product description: ")
                    price = input("Enter Product price: ")
                    quantity = input("Enter Product quantity: ")

                    Products.update_product(product_id, name, description, price, quantity)
                    print("<<<<<< product updated!")
                    
                case "4" :
                    product_id = input("Enter Products id: ")
                    Products.delete_product(product_id)
                    print("<<<<<< Product deleted!")

                case "5" : 
                    products = Products.view_products()
                    print(products)
                    print("<<<<<< Products fetched!")

                case "6" : 
                    product_id = input("Enter Products id: ")
                    product = Products.view_products_id(product_id)
                    print(product)
                    print("<<<<<< Product fetched!")
                
                case '0':
                    print("Exiting....")
                    break
                case _:
                    print("Invalid choice. Please try again.")

# Products().product_menu()