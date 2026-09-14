from Customers import Customers
from Products import Products
from Sales import Sales



def main_menu():
    while True:
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Sales Management")
        print("4. Exit Application")
        choice = input("Select an option: ")

        match (choice):
            case '1': Customers.customer_menu()
            case '2': Products.product_menu()
            case '3': Sales.sale_menu()
            case '4':
                print("Exiting Application")
                break
            case _: print("Invalid choice. Please try again")

if __name__ == "__main__":
    main_menu() 