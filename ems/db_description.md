## Description about database.

I am using the sqlite database for developing the Employee Management System and using this database, we can manage
each employee information, department information, timesheets of each employee and salary of each employee.

We using the relational database so it will make ease management and querying the data due to relational established 
among the tables through the foreign keys.

Employee Table: This is the main table of our application and this table will use to store the employee personal
information like employee id, name, mobile number, address and email address.

Timesheet table: This table is using the storing the time sheet details of the employee and this table has foreign 
key relationship to employee table. 

Salary table: This table is using for storing the salary of the employee and this table also has the foreign 
key relationship to employee table because employee is the root table in the database.

Department table: Department table is using for storing the department details of the employee, Each employee
belongs to any one of the department.

# Tables

CREATE TABLE IF NOT EXISTS "department" 
(
"created" datetime NOT NULL, 
"department_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(256) NOT NULL, 
"location" varchar(100) NOT NULL,
"updated" datetime NOT NULL
);


CREATE TABLE IF NOT EXISTS "employee" 
(
"created" datetime NOT NULL, "password" varchar(128) NOT NULL, 
"last_login" datetime NULL, "is_superuser" bool NOT NULL, 
"username" varchar(150) NOT NULL UNIQUE, 
"is_staff" bool NOT NULL, 
"is_active" bool NOT NULL, 
"date_joined" datetime NOT NULL, 
"employee_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"first_name" varchar(100) NOT NULL, 
"last_name" varchar(50) NOT NULL,
"mobile_number" varchar(12) NOT NULL, 
"email" varchar(254) NOT NULL, "position" varchar(126) NOT NULL, 
"department_id" integer NOT NULL REFERENCES "management_department" ("department_id") DEFERRABLE INITIALLY DEFERRED, 
"updated" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "timesheet" (
"created" datetime NOT NULL, "timesheet_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"date" date NOT NULL, 
"hours_worked" real NOT NULL, 
"updated" datetime NOT NULL, 
"employee_id" integer NOT NULL REFERENCES "management_employee" ("employee_id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "salary" (
"created" datetime NOT NULL, "salary_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"monthly_salary" real NOT NULL, 
"updated" datetime NOT NULL, 
"employee_id" integer NOT NULL REFERENCES "management_employee" ("employee_id") DEFERRABLE INITIALLY DEFERRED
);

# attributes, primary keys, foreign keys.

`department` table

attributes: name, updated, location, department_id, created

primary key: department_id

foreign key: None

Foreign Key Constraints: This table has no foreign key relationships with other tables.

`employee` table

attributes: username, is_staff, is_active, date_joined, employee_id, first_name, last_name, position,email,mobile_number
password, last_login, created, updated

primary key: employee_id

foreign key: department_id

Foreign Key Constraints:  This table has foreign key relationship with department table, if the department entry
deleted then employee rows also will delete.

`timesheet` table

attributes: timesheet_id, date, hours_worked, updated, created

primary key:timesheet_id

foreign key: employee_id

Foreign Key Constraints: This table has foreign key relationship with employee table, if the employee entry
deleted then timesheet rows also will delete.

`salary` table

attributes: salary_id, monthly_salary,updated, created, employee_id

primary key: salary_id

foreign key: employee_id

Foreign Key Constraints:  This table has foreign key relationship with salary table, if the employee entry
deleted then salary rows also will delete.








