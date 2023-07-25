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