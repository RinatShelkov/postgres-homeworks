-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	title text NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL

);


CREATE TABLE customers

(
	customer_id varchar(5) PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text NOT NULL
);


CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5)  REFERENCES customers(customer_id),
	employee_id int  REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city text NOT NULL

);

