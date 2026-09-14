from Database import conn 

class SaleItems:

    @staticmethod
    def create_table():
        cur = conn.cursor() 
        cur.execute(
            """CREATE TABLE IF NOT EXISTS sale_items (
                id SERIAL PRIMARY KEY,
                sale_id INTEGER 
                REFERENCES sales(id)
                ON DELETE CASCADE,
                product_id INTEGER 
                REFERENCES products(id)
                ON DELETE CASCADE,
                quantity INTEGER NOT NULL, 
                price DECIMAL(10,2) NOT NULL
                )"""
        )
        conn.commit()
        cur.close()
