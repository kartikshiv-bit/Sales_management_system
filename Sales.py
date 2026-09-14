from Database import conn

class Sales:
    def __init__(self):
        pass
        # self.name = name
        # self.contact = contact

    @staticmethod
    def create_table():
        cur = conn.cursor() 
        cur.execute(
            """CREATE TABLE IF NOT EXISTS sales (
                id SERIAL PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                date DATE NOT NULL,
                total_amount DECIMAL(10, 2) NOT NULL,
                CONSTRAINT fk_sales_customer
                FOREIGN KEY(customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
                )"""
        )
        conn.commit()
        cur.close()
    
    @staticmethod
    def insert_sale(customer_id, date, total_amount):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO sales(customer_id, date, total_amount)
            values(%s, %s, %s)""",
            (customer_id, date, total_amount,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_sale(sale_id,customer_id=None, date=None, total_amount= None):
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
        
        sale = cur.fetchone()
        if not sale:
            print(">>>>sale not found!")
            cur.close()
            return 
            
        update_fields = []

        if customer_id:
            update_fields.append(f"cusotmer_id = '{customer_id}'")
        elif date:
            update_fields.append(f"date = '{date}'")
        elif total_amount:
            update_fields.append(f"total_amount = '{total_amount}'")

        update_query = f"UPDATE sales SET {','.join(update_fields)} WHERE id = {sale_id}"

        cur.execute(update_query)
        conn.commit()
        cur.close()

    @staticmethod
    def delete_sale(sale_id):
        cur = conn.cursor()
        cur.execute(
            """DELETE FROM sales WHERE id = %s""",(sale_id,)
        )
        conn.commit()
        cur.close()
    
    @staticmethod
    def view_sales():
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM sales 
            ORDER BY id ASC"""
        )
        sales = cur.fetchall()
        cur.close()
        return sales
    
    @staticmethod
    def view_sales_id(sale_id):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM sales WHERE id = %s """,(sale_id,)
        )
        sales = cur.fetchone()
        cur.close()
        return sales

    @staticmethod
    def generate_bill(sale_id):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM sales WHERE id = %s """,(sale_id,)
        )
        sale_items = cur.fetchone()
        for item in sale_items:
            total_amount += item[4] * item[3]
        cur.close()
        return total_amount
    
    # Analytical Queries
        
    @staticmethod
    def total_sale_by_date(start_date, end_date):
        cur = conn.cursor()
        cur.execute(
            """SELECT SUM(total_amount) FROM sales WHERE date BETWEEN = %s AND %s """,(start_date, end_date,)
        )
        sales = cur.fetchone()
        cur.close()
        return sales
    
    @staticmethod
    def get_top_selling_products():
        cur = conn.cursor()
        cur.execute('''
        SELECT product_id, SUM(quantity) as total_quantity FROM sale_items
        GROUP BY product_id
        ORDER BY total_quantity DESC
        LIMIT 5''')
        top_products = cur.fetchall()
        cur.close()
        return top_products
    
    @staticmethod
    def get_sales_by_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM sales WHERE customer_id = %s""", (customer_id,)
        )
        sales = cur.fetchall()
        cur.close()
        return sales

    @staticmethod
    def sale_menu():

        while True:
            print("1. Create Table")
            print("2. Insert sale")
            print("3. Update sale")
            print("4. Delete sale")
            print("5. View sale")
            print("6. View sale by ID")
            print("7. Generate bill")
            print("8. Total Sales by Date ")
            print("9. Top 5 Selling Products")
            print("10. Sales By Customer")
            print("0. Exit")
            choice = input("Enter Choice: ")

            match (choice):

                case "1" : 
                    Sales().create_table()
                    print("<<<<<< Sale table created!")

                case "2" :
                    customer_id = input("Enter customer id: ")
                    sales_date = input("Enter sales date: ")
                    total_amount = input("Enter sale amount: ")
                    Sales().insert_sale(customer_id, sales_date, total_amount)
                    print("<<<<<< Sale created!")

                case "3" : 
                    customer_id = input("Enter customer id: ")
                    sales_date = input("Enter sales date: ")
                    total_amount = input("Enter sale amount: ")

                    Sales().update_sale(customer_id, sales_date, total_amount)
                    print("<<<<<< Sale updated!")
                    
                case "4" :
                    sale_id = input("Enter sales id: ")
                    Sales().delete_sale(sale_id)
                    print("<<<<<< sale deleted!")

                case "5" : 
                    sales = Sales().view_sales()
                    print(sales)
                    print("<<<<<< sales fetched!")

                case "6" : 
                    sale_id = input("Enter sales id: ")
                    sale = Sales().view_sales_id(sale_id)
                    print(sale)
                    print("<<<<<< Sale fetched!")
                
                case "7" : 
                    sale_id = input("Enter sales id: ")
                    sale = Sales().generate_bill(sale_id)
                    print(sale)
                    print("<<<<<< Sale fetched!")
                
                case "8" : 
                    start_date = input("Enter Start Date")
                    end_date = input("Enter End Date")
                    sale = Sales().total_sale_by_date(start_date, end_date)
                    print(sale)
                    print("<<<<<< Sale fetched!")
                
                case "9" : 
                    products = Sales().get_top_selling_products()
                    print(products)
                    print("<<<<<< Products fetched!")
                
                case "10" : 
                    customer_id = input("Enter customer ID: ")
                    sales = Sales().get_top_selling_products()
                    print(sales)
                    print("<<<<<< Sales fetched!")
                
                case '0':
                    print("Exiting....")
                    break
                case _:
                    print("Invalid choice. Please try again.")

# Sales().sale_menu()