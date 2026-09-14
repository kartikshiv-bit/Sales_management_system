ALTER TABLE sales
ADD CONSTRAINT fk_sales_customer
FOREIGN KEY (customer_id)
REFERENCES customerS(id)
ON DELETE CASCADE;

CREATE TABLE sale_items(
	id SERIAL PRIMARY KEY,
	sale_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL, 
	price DECIMAL(10,2) NOT NULL
);