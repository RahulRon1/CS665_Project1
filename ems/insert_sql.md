INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-23 10:30:00', 'Marketing', 'Kansas', '2023-07-23 10:30:00');

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-24 11:15:10', 'Human Resources', 'Dallas', '2023-07-24 11:15:00');

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-25 12:15:00', 'Engineering', 'Huston', '2023-07-24 11:15:00');

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-26 09:15:00', 'Finance', 'Chicago', '2023-07-24 11:15:00');

INSERT INTO department (created, name, location, updated) 
VALUES ('2023-07-27 10:15:00', 'Management', 'Dallas', '2023-07-24 11:15:00');


INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-25 09:00:00', 'xxxxxxx', '2023-07-25 09:00:00', 0, 'abc', 1, 1, '2023-07-25 09:00:00', 'abc', 'xyx', '1234567890', 'abc.xyx@example.com', 'Manager', 1, '2023-07-25 09:00:00');

INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-26 10:00:00', 'xxxxxxx', '2023-07-26 10:00:00', 0, 'xyx', 1, 1, '2023-07-26 10:00:00', 'abcd', 'xyxa', '0987654321', 'abcd.mus@example.com', 'HR', 2, '2023-07-26 10:00:00');

INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-25 09:00:00', 'xxxxxxx', '2023-07-25 09:00:00', 0, 'abc', 1, 1, '2023-07-25 09:00:00', 'abc', 'xyx', '1234567890', 'abc.xyx@example.com', 'Senior Software Engineer', 3, '2023-07-25 09:00:00');

INSERT INTO employee (created, password, last_login, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, mobile_number, email, position, department_id, updated) 
VALUES ('2023-07-26 10:00:00', 'xxxxxxx', '2023-07-26 10:00:00', 0, 'xyx', 1, 1, '2023-07-26 10:00:00', 'abcd', 'xyxa', '0987654321', 'abcd.mus@example.com', 'Software Engineer', 4, '2023-07-26 10:00:00');


INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-27 08:30:00', '2023-07-27', 8, '2023-07-27 08:30:00', 1);

INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-28 09:30:00', '2023-07-28', 8, '2023-07-28 09:30:00', 2);

INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-28 09:30:00', '2023-07-28', 5, '2023-07-28 09:30:00', 3);

INSERT INTO timesheet (created, date, hours_worked, updated, employee_id) 
VALUES ('2023-07-28 09:30:00', '2023-07-28', 5, '2023-07-28 09:30:00', 4);


INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-29 10:30:00', 5000, '2023-07-29 10:30:00', 1);

INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-30 11:30:00', 4500, '2023-07-30 11:30:00', 2);

INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-30 11:30:00', 7500, '2023-07-30 11:30:00', 3);

INSERT INTO salary (created, monthly_salary, updated, employee_id) 
VALUES ('2023-07-30 11:30:00', 9500, '2023-07-30 11:30:00', 4);
