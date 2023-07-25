`department` table

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-23 10:30:00', 'Marketing', 'Kansas', '2023-07-23 10:30:00');

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-24 11:15:10', 'Human Resources', 'Dallas', '2023-07-24 11:15:00');

SELECT * FROM department;

DELETE FROM department WHERE department_id = 3;

UPDATE department SET location = 'San Diego' WHERE department_id = 3;

`employee` table

INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-25 09:00:00', 'xxxxxxx', '2023-07-25 09:00:00', 0, 'abc', 1, 1, '2023-07-25 09:00:00', 'abc', 'xyx', '1234567890', 'abc.xyx@example.com', 'Manager', 1, '2023-07-25 09:00:00');

INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-26 10:00:00', 'xxxxxxx', '2023-07-26 10:00:00', 0, 'xyx', 1, 1, '2023-07-26 10:00:00', 'abcd', 'xyxa', '0987654321', 'abcd.mus@example.com', 'HR', 2, '2023-07-26 10:00:00');

select * from employee;

DELETE FROM employee WHERE employee_id = 3;

UPDATE employee SET position = 'Senior Manager' WHERE employee_id = 3;

`timesheet` table

INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-27 08:30:00', '2023-07-27', 8, '2023-07-27 08:30:00', 1);

INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-28 09:30:00', '2023-07-28', 8, '2023-07-28 09:30:00', 2);

SELECT * FROM timesheet;

UPDATE timesheet SET hours_worked = 9 WHERE timesheet_id = 3;

DELETE FROM timesheet WHERE timesheet_id = 3;

`salary` table

INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-29 10:30:00', 5000, '2023-07-29 10:30:00', 1);

INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-30 11:30:00', 4500, '2023-07-30 11:30:00', 2);

SELECT * FROM timesheet;

UPDATE timesheet SET hours_worked = 9 WHERE timesheet_id = 3;

DELETE FROM timesheet WHERE timesheet_id = 3;
