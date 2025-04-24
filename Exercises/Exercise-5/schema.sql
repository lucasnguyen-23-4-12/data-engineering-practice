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
