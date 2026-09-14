from Database import conn

class Customers:
    def __init__(self):
        pass
        # self.name = name
        # self.contact = contact

    @staticmethod
    def create_table():
        cur = conn.cursor() 
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(15) NOT NULL
                )"""
        )
        conn.commit()
        cur.close()
    
    @staticmethod
    def insert_customer(name, contact):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO customers (name, contact)
            values(%s, %s)""",
            (name,contact)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_customer(customer_id, name=None, contact=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        customer = cur.fetchone()
        if not customer:
            print(">>>>Customer not found!")
            cur.close()
            return 
        update_fields = []
        if name:
            update_fields.append(f"name = '{name}'")
        if contact:
            update_fields.append(f"contact = '{contact}'")

        update_query = f"UPDATE customers SET {', '.join(update_fields)} WHERE id = %s"
        cur.execute(update_query, (customer_id,))
        conn.commit()
        cur.close()

    @staticmethod
    def delete_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            """DELETE FROM customers WHERE id = %s""",(customer_id,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def get_all_customers():
        cur = conn.cursor()
        cur.execute('SELECT * FROM customers')
        customers = cur.fetchall()
        cur.close()
        return customers
    
    @staticmethod
    def view_customers():
        cur = conn.cursor()
        cur.execute('SELECT * FROM customers')
        customers = cur.fetchall()
        for customer in customers:
            print(customer)
        cur.close()
    
    @staticmethod
    def view_customer_by_id(customer_id):
        cur = conn.cursor()
        cur.execute('SELECT * FROM customers WHERE id = %s', (customer_id,))
        customer = cur.fetchone()
        if customer:
            print(customer)
        else:
            print("Customer not found")
        cur.close()

    @staticmethod
    def get_sales_by_customer(customer_id):
        cur = conn.cursor()
        cur.execute('''SELECT s.id, s.date, s.total_amount FROM sales s
                       JOIN customers c ON s.customer_id = c.id
                       WHERE c.id = %s''', (customer_id,))
        sales = cur.fetchall()
        for sale in sales:
            print(sale)
        cur.close()

    @staticmethod
    def search_customer(name):
        cur = conn.cursor()
        cur.execute('SELECT * FROM customers WHERE name ILIKE %s', ('%' + name + '%',))
        customers = cur.fetchall()
        for customer in customers:
            print(customer)
        cur.close()
    @staticmethod
    def customer_menu():

        while True:
            print("1. Create Table")
            print("2. Insert Customer")
            print("3. UPdate Customer")
            print("4. Delete Customer")
            print("5. View Customers")
            print("6. View Customer by ID")
            print("7. Get Sales by Customer")
            print("8. Search Customer")
            print("0. Exit")
            choice = input("Enter Choice: ")

            match (choice):

                case "1" : 
                    Customers.create_table()
                    print("<<<<<< customer table created!")

                case "2" :
                    name = input("Enter customer name: ")
                    contact = input("Enter customer contact: ")
                    Customers.insert_customer(name, contact)
                    print("<<<<<< customer created!")

                case "3" : 
                    customer_id = input("Enter Customer id: ")
                    name = input("Enter customer name: ")
                    contact = input("Enter customer contact: ")
                    Customers.update_customer(customer_id, name, contact)
                    print("<<<<<< cusotmer updated!")
                    
                case "4" :
                    customer_id = input("Enter Customer id: ")
                    Customers.delete_customer(customer_id)
                    print("<<<<<< customer deleted!")

                case'5':
                    Customers.view_customers()
                    print("Customers viewed")
                case '6':
                    customer_id = int(input("Enter customer id: "))
                    Customers.view_customer_by_id(customer_id)
                    print("Customer viewed")
                case '7':
                    customer_id = int(input("Enter customer id: "))
                    Customers.get_sales_by_customer(customer_id)
                    print("Sales viewed")
                case '8':
                    name = input("Enter customer name: ")
                    Customers.search_customer(name)
                    print("Customer searched")

                case 0:
                    print("Exiting....")
                    break
                case _:
                    print("Invalid choice. Please try again.")

# Customers().customer_menu()