#                    BÁO CÁO THỰC HÀNH LAB 09



------



## Exercise #5 - Data Modeling for Postgres + Python.



### Mục tiêu

+ Khởi tạo hệ thống cơ sở dữ liệu PostgreSQL với Docker Compose.

+ Load dữ liệu từ các file CSV (accounts.csv, products.csv, transactions.csv) vào database thông qua script Python.

+ Xác thực dữ liệu đã được nhập thành công vào database.

  

### CÁC CHỈNH SỬA ĐÃ THỰC HIỆN Ở EXERCISE 5 VÀ KẾT QUẢ:

- ***viết lại code dockerfile***

  ```
  FROM python:latest
  
  WORKDIR /app
  COPY . /app
  COPY data /app/data
  
  RUN python3 -m pip install -r requirements.txt
  ```

+ ***tạo file schema.sql***

  ```
  DROP TABLE IF EXISTS transactions;
  DROP TABLE IF EXISTS products;
  DROP TABLE IF EXISTS accounts;
  
  CREATE TABLE accounts (
      customer_id     INT PRIMARY KEY,
      first_name      VARCHAR(50),
      last_name       VARCHAR(50),
      address_1       VARCHAR(100),
      address_2       VARCHAR(100),
      city            VARCHAR(50),
      state           VARCHAR(20),
      zip_code        VARCHAR(10),
      join_date       DATE
  );
  
  CREATE TABLE products (
      product_id           INT PRIMARY KEY,
      product_code         VARCHAR(10),
      product_description  TEXT
  );
  
  CREATE TABLE transactions (
      transaction_id    VARCHAR(50) PRIMARY KEY,
      transaction_date  DATE,
      product_id        INT,
      quantity          INT,
      account_id        INT,
      FOREIGN KEY (product_id) REFERENCES products(product_id),
      FOREIGN KEY (account_id) REFERENCES accounts(customer_id)
  );
  
  -- Index để tăng hiệu suất tìm kiếm
  CREATE INDEX idx_transaction_date ON transactions(transaction_date);
  CREATE INDEX idx_account_state ON accounts(state);
  
  ```

+ ***viết lại code file main.py***

  ```
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
  ```



Khi đọc file CSV bằng Python (`pandas`, `csv.reader`) hoặc chèn vào PostgreSQL, các khoảng trắng dư thừa ở đầu/cuối mỗi trường dữ liệu có thể gây:

Lỗi khi so sánh dữ liệu (`'Widget Medium'` khác `' Widget Medium'`)

Gây kết nối sai giữa các bảng khi thiết lập `FOREIGN KEY`, vì giá trị có khoảng trắng không trùng khớp

Gây khó khăn trong việc truy vấn SQL chính xác



**nên nhóm đã quyết định bỏ khoảng trắng sau dấu phẩy ở 3 file trong mục data**

- ***accounts.csv***

  ```
  customer_id,first_name,last_name,address_1,address_2,city,state,zip_code,join_date
  4321,john,doe,1532 East Main St.,PO BOX 5,Middleton,Ohio,50045,2022/01/16
  5677,jane,doe,543 Oak Rd.,,BigTown,Iowa,84432,2021/05/07
  ```

+ ***products.csv***

  ```
  product_id,product_code,product_description
  345,01,Widget Medium
  241,02,Widget Large
  ```

+ ***transactions.csv***

  ```
  transaction_id,transaction_date,product_id,product_code,product_description,quantity,account_id
  AS345-ASDF-31234-FDAAD-9345,2022/06/01,345,01,Widget Medium,5,4321
  9234A-JFDA-87654-BFAEA-0932,2022/06/02,241,02,Widget Large,1,5677
  ```



## CÁC BƯỚC KHỞI TẠO VÀ ẢNH KẾT QUẢ CỦA EXERCISE 5

-  ***bước 1***

```
docker build --tag=exercise-5 .
```

<img src="C:\Users\DAT\Downloads\EXERCISE 5\z6537495827132_ad4591a274bb46a7402e7322adf039c4.jpg" alt="z6537495827132_ad4591a274bb46a7402e7322adf039c4" style="zoom: 67%;" />

+ ***bước 2***

  ```
  docker-compose build
  docker-compose up run
  ```

  ![image-20250424162117011](C:\Users\DAT\AppData\Roaming\Typora\typora-user-images\image-20250424162117011.png)

  







