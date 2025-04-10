create database DataAnalytics;

use DataAnalytics;

create table Persons (
	personID int,
    lastname varchar(255),
    firstname varchar(255),
    Address varchar(255),
    city varchar(255)
);

insert into Persons values(1,"kotla","manikanta","mbnr","Hyd");

insert into Persons values(2,"kmk","mani","jcl","chennai"),
(3,"kar","naveen","npt","Hyd");

select * from Persons;
select lastname from Persons;

delete from Persons where personID=2;

update persons set lastname="kanike" where personID=3;

create table Users (
	userID int 	auto_increment primary key,
    username varchar(50) unique not null,
    email varchar(50) unique not null,
    firstname varchar(255),
    lastname varchar(255),
    dateofbirth date,
    createdAt datetime default current_timestamp,
    lastlogin datetime,
    status enum('active','inactive','suspended') default ('active'),
    index(email)
);

insert into Users(username,email,firstname,lastname,dateofbirth,lastlogin,status)
 values('bablumani','mani@gmail.com','kotla','manikanta','2000-01-11',NOW(),'active');
 
 insert into Users(username,email,firstname,lastname,dateofbirth,lastlogin,status)
 values('bablu','bablu@gmail.com','kotla','bablu','2005-07-21','2024-10-18','inactive');
 
 select * from Users;
 
create table Student(
	student_id int  primary key,
    name varchar(50),
	age int,
    check (age>18));

insert into Student values(1,'mani',21),(2,'kmk',25);

create table Enrollments(
	enrollment_id int primary key,
    student_id int,
    course_id int,
    foreign key(student_id) references Student(student_id));

insert into Enrollments values(101,2,501);

select * from Enrollments;

select s.name,e.enrollment_id
from Student s
join Enrollments e
on s.student_id=e.student_id;

drop  table Users;

truncate table Persons;

create table composite(
	order_id int,
    product_id int,
    quantity int,
    primary key(order_id,product_id));
    
create table Products(productID int,productname varchar(255), price int);

insert into Products values(1,'bike',95000),(2,'car',700000);
insert into Products values(1,'bike2',80000);
insert into Products values(2,'car2',800000);
insert into Products values(4,'car3',800000);
select * from Products;

select min(price) from Products;
select max(price) from Products;
select sum(price) from Products;

select min(price) as min, productID
from Products
group by productID;

select avg(price) as avg_price, productID
from Products
group by productID;

select count(*) from Products;

select count(productID)
from Products
where price>700000; 

select count(distinct price)
from Products;

# Cascade

create table customer (
	customerid int primary key,
    name varchar(100)
);
insert into customer values(1,'kmk'),(2,'mani'),(3,'naveen');
create table orders (
	orderid int primary key,
    customerid int,
    productname varchar(50),
    foreign key(customerid) references customer(customerid)
    on delete cascade
);
insert into orders values(11,1,'car'),(22,2,'bike'),(33,3,'cycle');

delete from customer where customerid=3;
select * from customer;
select * from orders;

create table employee (
	employeeid int primary key,
    name varchar(100)
);
insert into employee values(1,'kmk'),(2,'mani'),(3,'naveen');
create table organisation (
	orgid int primary key,
    employeeid int,
    orgname varchar(50),
    foreign key(employeeid) references employee(employeeid)
    on update cascade
);
insert into organisation values(11,1,'tcs'),(22,2,'info'),(33,3,'cgi');

update employee set employeeid=5 where name='prabhu';
select * from employee;
select * from organisation;

select * from Products 
order by price;

select * from Products 
order by price desc;


CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);

# Inner join
select customerstable.CustomerID,
		customerstable.CustomerName,
        orderstable.OrderID,
        orderstable.OrderDate,
        orderstable.Amount
from customerstable 
inner join orderstable on customerstable.CustomerID=orderstable.CustomerID;

 # left join
select customerstable.CustomerID,
		customerstable.CustomerName,
        orderstable.OrderID,
        orderstable.OrderDate,
        orderstable.Amount
from customerstable 
left join orderstable on customerstable.CustomerID=orderstable.CustomerID;

# right join
select customerstable.CustomerID,
		customerstable.CustomerName,
        orderstable.OrderID,
        orderstable.OrderDate,
        orderstable.Amount
from customerstable 
right join orderstable on customerstable.CustomerID=orderstable.CustomerID;

create table drinks(id int,name varchar(50));
insert into drinks values (1,'tea'),(2,'coffee');

create table snacks(snacksid int,snacksname varchar(50));
insert into snacks values (10,'kukure'),(11,'moongdal');

select drinks.id,drinks.name,snacks.snacksid,snacks.snacksname
from drinks
cross join snacks;


create table new_employee (empid int,name varchar(50),job_desc varchar(50),salary int,hire_date date);

insert into new_employee values (1,'mani','admin',10000,date '2024-02-02'),(2,'kmk','manager',20000,date '2024-02-02'),
(3,'bablu','sales',30000,date '2024-02-02'),(4,'naveen','sales',40000,date '2024-02-02'),(5,'prabhu','hr',50000,date '2024-02-02');

#avg salary for each dept
select job_desc,avg(salary) from new_employee group by job_desc;
#count no of emp
select job_desc,count(empid) from new_employee group by job_desc;

select job_desc,count(empid) 
from new_employee
group by job_desc
having count(empid)>1
order by job_desc;

select job_desc,count(empid) 
from new_employee where salary>20000
group by job_desc
having count(empid)>1
order by job_desc;

#sub queries
select name from new_employee where salary <
(select avg(salary) from new_employee);


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');

Insert into departments values(4,'development');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);

select * from employees 
where department_id in
(select department_id 
from departments 
where department_name="sales");

select employee_name,
	(select department_name from departments
    where departments.department_id=employees.department_id)
as department_name from employees;

select employee_name,department_id from employees where department_id in
	(select department_id from employees
    group by department_id having count(*)>1);
 
 # find departments that have atleast one employee
select department_name 
from departments d where exists
(select 1 from employees e where e.department_id=d.department_id);

# find departments that do not have any employee
select department_name 
from departments d where not exists
(select 1 from employees e where e.department_id=d.department_id);

#find departments where the avg empid is greater than 102
select department_id 
from employees
group by department_id
having avg(employee_id)>102;

#scalar functions
select ucase('Hello World') as uppercase_string;

select lcase('Hello World') as lowercase_string;

select mid('Hello World',4,2) as sub_string;

select length('Hello World') as string_length;

select round(1560.425,2) as round_value;

select now() as currentdatetime;

select format(1234.1447,2) as format_number;

create table users (userid int auto_increment,
						username varchar(100),
                        primary key(userid));
                        
alter table users auto_increment=1001;
insert into users(username) values('kmk'),('mani');
select * from users;

create table coupons(id int,
						customername varchar(100),
                        code varchar(100) null);
insert into coupons values(1,'kmk',null),(2,'dsp','flat100'),
							(3,'abc',null);
select * from coupons;
select id,customername,coalesce(code,'DEFAULT') As applied_coupon
from coupons;

#TCL commit , rollback

start transaction;

insert into products values(5,'tractor',99999);
insert into products values(6,'tractor2',88888);
savepoint point;
select * from products;

rollback to point;

commit;


# stored procedure
DELIMITER //
create procedure getallproducts()
begin
	select * from products;
end;
//
call getallproducts;

# procedure-called by user input
DELIMITER //
create procedure getproductid(in productno int)
begin
	select productID,productname,price 
    from products
    where productID=productno;
end;
//

call getproductid(2);

DELIMITER //
create procedure getproductsname(in productno int,out name varchar(100))
begin
	select productname into name
    from products
    where productID=productno;
end;
//

set @product_name='';

call getproductsname(4,@product_name);

select @product_name;
