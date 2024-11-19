# Write your MySQL query statement below
SELECT employees_1.name AS Employee
FROM Employee employees_1, Employee employees_2
WHERE employees_1.managerId = employees_2.id AND employees_1.salary > employees_2.salary;