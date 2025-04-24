import psycopg2
import csv
from datetime import datetime

def create_tables(cur):
    with open('schema.sql', 'r') as f:
        cur.execute(f.read())

def insert_accounts(cur):
    with open('data/accounts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO accounts (customer_id, first_name, last_name, address_1, address_2, city, state, zip_code, join_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                int(row['customer_id']),
                row['first_name'],
                row['last_name'],
                row['address_1'],
                row['address_2'] if row['address_2'] else None,
                row['city'],
                row['state'],
                row['zip_code'],
                datetime.strptime(row['join_date'], '%Y/%m/%d').date()
            ))

def insert_products(cur):
    with open('data/products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO products (product_id, product_code, product_description)
                VALUES (%s, %s, %s)
            """, (
                int(row['product_id']),
                row['product_code'],
                row['product_description']
            ))

def insert_transactions(cur):
    with open('data/transactions.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO transactions (transaction_id, transaction_date, product_id, quantity, account_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                row['transaction_id'],
                datetime.strptime(row['transaction_date'], '%Y/%m/%d').date(),
                int(row['product_id']),
                int(row['quantity']),
                int(row['account_id'])
            ))

def main():
    conn = psycopg2.connect(
        host="postgres",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    create_tables(cur)
    insert_accounts(cur)
    insert_products(cur)
    insert_transactions(cur)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Database loaded successfully.")

if __name__ == "__main__":
    main()
