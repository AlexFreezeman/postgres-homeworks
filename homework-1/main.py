"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import pathlib
import csv

# адрес файлов
path_customers = pathlib.Path.cwd() / 'north_data' / 'customers_data.csv'
path_employees = pathlib.Path.cwd() / 'north_data' / 'employees_data.csv'
path_orders = pathlib.Path.cwd() / 'north_data' / 'orders_data.csv'

customers = path_customers
employees = path_employees
orders = path_orders

# коннектимся
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1337')
cur = conn.cursor()


def open_file_customers():
    """
    открываем и возвращаем файл с клиентами
    """
    with open(customers, 'r', encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=',')
        customers_data = list()
        for d in data:
            customers_data.append(d)
        return customers_data


def open_file_employees():
    """
    открываем и возвращаем файл с сотрудниками
    """
    with open(employees, 'r', encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=',')
        employees_data = list()
        for d in data:
            employees_data.append(d)
        return employees_data


def open_file_orders():
    """
    открываем и возвращаем файл с заказами
    """
    with open(orders, 'r', encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=',')
        orders_data = list()
        for d in data:
            orders_data.append(d)
        return orders_data


def insert_into_table_customers(customers_data):
    """
    вставляем клиентов в таблицу через цикл
    """
    for line in customers_data:
        customer_id = line['customer_id']
        company_name = line['company_name'].replace("'", "''")
        contact_name = line['contact_name']
        cur.execute(f"INSERT INTO customers VALUES ('{customer_id}', '{company_name}', '{contact_name}');")


def insert_into_table_employees(employees_data):
    """
    вставляем сотрудников в таблицу через цикл
    """
    for line in employees_data:
        employee_id = line['employee_id']
        first_name = line['first_name']
        last_name = line['last_name']
        title = line['title']
        birth_date = line['birth_date']
        notes = line['notes']
        cur.execute(f"INSERT INTO employees VALUES ('{employee_id}', '{first_name}', '{last_name}', '{title}', '{birth_date}', '{notes}');")


def insert_into_table_orders(orders_data):
    """
    вставляем заказы в таблицу через цикл
    """
    for line in orders_data:
        order_id = line['order_id']
        customer_id = line['customer_id']
        employee_id = line['employee_id']
        order_date = line['order_date']
        ship_city = line['ship_city']
        cur.execute(f"INSERT INTO orders VALUES ('{order_id}', '{customer_id}', '{employee_id}', '{order_date}', '{ship_city}');")


# само действие программы
try:
    with conn:
        with conn.cursor() as cur:
            customer_list = open_file_customers()
            insert_into_table_customers(customer_list)
            employee_list = open_file_employees()
            insert_into_table_employees(employee_list)
            order_list = open_file_orders()
            insert_into_table_orders(order_list)
            cur.execute("SELECT * FROM customers")
#            cur.execute("SELECT * FROM employees")
#            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()
