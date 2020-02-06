import sqlite3

def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection):
    connection.close()

def db_query(query, query_parameters=None):
    try:
        connect, cursor = open_connection()
        if query_parameters:
            cursor.execute(query, query_parameters)
            connect.commit()
        else:
            for i in cursor.execute(query):
                print(i)
    except sqlite3.DataError as error:
            print(error)
    finally:
        close_connection(connect)
# db_query("PRAGMA table_info(employees)")
def exercise1():
    query1 ="""SELECT first_name FROM employees WHERE first_name LIKE '%b%' AND first_name LIKE '%c%';"""
    query2 ="""SELECT first_name, last_name, department_id FROM employees 
    WHERE department_id IN (30, 100) ORDER BY  department_id  ASC; """
    query3 ="""SELECT first_name, last_name, salary FROM employees WHERE salary NOT BETWEEN 10000 AND 15000;"""
    query4 ="""SELECT first_name FROM employees WHERE first_name LIKE '%b%' AND first_name LIKE '%c%';"""
    query5 ="""SELECT last_name, job_id, salary FROM employees 
    WHERE job_id IN ('IT_PROG', 'SH_CLERK') AND salary NOT IN (4500,10000, 15000);"""
    query6 ="""SELECT last_name FROM employees WHERE last_name LIKE '__e%';"""
    query7 ="""SELECT COUNT(DISTINCT job_id) FROM employees;"""
    query8 ="""SELECT SUM(salary) FROM employees;"""
    query9 ="""SELECT MAX(salary), MIN(salary) FROM employees;"""
    query10 ="""SELECT MAX(salary) FROM employees;"""
    db_query(query7)
exercise1()

def exercise2():
    query11 ="""SELECT COUNT(DISTINCT job_id) FROM employees"""
    query12 ="""SELECT first_name. last_name FROM employees WHERE (employee_id IN (SELECT manager_id FROM employees));"""
    query13 ="""SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
"""
    query14 ="""SELECT first_name, last_name, salary 
FROM employees 
WHERE employees.salary = (SELECT min_salary
FROM jobs
WHERE employees.job_id = jobs.job_id);
"""
    query15 ="""SELECT first_name, last_name, salary 
FROM employees 
WHERE department_id IN 
(SELECT Department_id FROM departments WHERE depart_name LIKE 'IT%') 
AND salary > (SELECT avg(salary) FROM employees);
"""
    query16 ="""SELECT first_name, last_name FROM employees 
WHERE manager_id in (select employee_id 
FROM employees WHERE Department_id 
IN (SELECT Department_id FROM departments WHERE location_id 
IN (select location_id from locations where country_id='US')));
"""
    db_query(query16)
exercise2()

def exercise3():
    query1 ="""SELECT depart_name AS 'Department Name', 
COUNT(*) AS 'No of Employees' 
FROM departments 
INNER JOIN employees 
ON employees.Department_id = departments.Department_id 
GROUP BY departments.Department_id, depart_name 
ORDER BY depart_name;
"""
    query2 = """SELECT d.department_name, e.first_name, l.city 
FROM departments d 
JOIN employees e 
ON (d.manager_id = e.employee_id) 
JOIN locations l USING (location_id);
"""
    query3 ="""SELECT jh.* FROM job_history jh 
JOIN employees e 
ON (jh.employee_id = e.employee_id) 
WHERE salary > 10000;
"""
    query4 ="""SELECT job_title, AVG(salary) 
	FROM employees 
		NATURAL JOIN jobs 
			GROUP BY job_title;
"""
    query5 = """SELECT employee_id, job_title, end_date-start_date Days FROM job_history 
NATURAL JOIN jobs 
WHERE Department_id=90;
"""
    query6 ="""SELECT e.first_name, e.last_name, e.hire_date 
FROM employees e 
JOIN employees davies 
ON (davies.last_name = "Jones") 
WHERE davies.hire_date < e.hire_date;
"""
    db_query(query6)
exercise3()
