CREATE TABLE departments (
  dep_id INTEGER PRIMARY KEY,
  dep_name VARCHAR(100) NOT NULL
);

INSERT INTO departments VALUES (1, 'south_dep');
INSERT INTO departments VALUES (2, 'north_dep');
INSERT INTO departments VALUES (3, 'west_dep');

CREATE TABLE employees (
  emp_id INTEGER PRIMARY KEY,
  emp_dep_id INTEGER
);

INSERT INTO employees VALUES (1, 2);
INSERT INTO employees VALUES (2, 2);
INSERT INTO employees VALUES (3, 1);
INSERT INTO employees VALUES (4, 3);
INSERT INTO employees VALUES (5, 1);
INSERT INTO employees VALUES (6, 1);

SELECT * FROM departments;
SELECT * FROM employees;

select dep_name as 'Название подразделения', count(emp_id) as 'Количество сотрудников'
from departments d join employees e on d.dep_id = e.emp_dep_id
group by(emp_dep_id)
having count(emp_id)>1
