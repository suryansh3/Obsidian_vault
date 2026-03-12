-- 6.2. Display employee “Andrew Brown” school name
SQL> SELECT S.NAME AS SCHOOL_NAME
  2  FROM EMPLOYEE E
  3  JOIN EMPLOYEE_ALIGNMENT EA ON E.ID = EA.EMPLOYEE_ID
  4  JOIN SCHOOL S ON EA.SCHOOL_ID = S.ID
  5  WHERE E.FIRST_NAME = 'Andrew' AND E.LAST_NAME = 'Brown';

SCHOOL_NAME
-------------------------
Computer Engineering

1 row selected.

-- 6.3. Display full name of the supervisor for employee ID “128433”
SQL> SELECT S.FIRST_NAME || ' ' || S.LAST_NAME AS SUPERVISOR_NAME
  2  FROM EMPLOYEE E
  3  JOIN EMPLOYEE S ON E.SUPERVISOR_ID = S.ID
  4  WHERE E.ID = 128433;

SUPERVISOR_NAME
--------------------
Amit Banerjee

1 row selected.

-- 6.4. Who belongs to same school as “Rod Marsh”?
SQL> SELECT E2.FIRST_NAME || ' ' || E2.LAST_NAME AS COLLEAGUE_NAME
  2  FROM EMPLOYEE E1
  3  JOIN EMPLOYEE_ALIGNMENT EA1 ON E1.ID = EA1.EMPLOYEE_ID
  4  JOIN EMPLOYEE_ALIGNMENT EA2 ON EA1.SCHOOL_ID = EA2.SCHOOL_ID
  5  JOIN EMPLOYEE E2 ON EA2.EMPLOYEE_ID = E2.ID
  6  WHERE E1.FIRST_NAME = 'Rod' AND E1.LAST_NAME = 'Marsh'
  7    AND E2.ID <> E1.ID;

COLLEAGUE_NAME
--------------------
Larry Houston
Andrew Brown

2 rows selected.

-- 6.5. Who has the same title as “Stanely Garner”?
SQL> SELECT E2.FIRST_NAME || ' ' || E2.LAST_NAME AS FULL_NAME
  2  FROM EMPLOYEE E1
  3  JOIN EMPLOYEE_PAY EP1 ON E1.ID = EP1.EMPLOYEE_ID
  4  JOIN JOB J1 ON EP1.JOB_ID = J1.ID
  5  JOIN JOB J2 ON J1.TITLE = J2.TITLE
  6  JOIN EMPLOYEE_PAY EP2 ON J2.ID = EP2.JOB_ID
  7  JOIN EMPLOYEE E2 ON EP2.EMPLOYEE_ID = E2.ID
  8  WHERE E1.FIRST_NAME = 'Stanely' AND E1.LAST_NAME = 'Garner'
  9    AND E2.ID <> E1.ID;

FULL_NAME
--------------------
Meenakshi Iyer
Priyanka Reddy

2 rows selected.

-- 6.6. Which employees are working in the school longer than “Larry Houston”?
-- Assuming HIRE_DATE is in the EMPLOYEE or EMPLOYEE_ALIGNMENT table
SQL> SELECT E2.FIRST_NAME || ' ' || E2.LAST_NAME AS FULL_NAME
  2  FROM EMPLOYEE E1
  3  JOIN EMPLOYEE E2 ON E2.HIRE_DATE < E1.HIRE_DATE
  4  WHERE E1.FIRST_NAME = 'Larry' AND E1.LAST_NAME = 'Houston';

FULL_NAME
--------------------
Amit Banerjee
Rajesh Sharma

2 rows selected.

-- 6.7. Find the number of employees working in school of computer engineering
SQL> SELECT COUNT(EA.EMPLOYEE_ID) AS EMP_COUNT
  2  FROM EMPLOYEE_ALIGNMENT EA
  3  JOIN SCHOOL S ON EA.SCHOOL_ID = S.ID
  4  WHERE S.NAME = 'Computer Engineering';

 EMP_COUNT
----------
         8

1 row selected.

-- 6.8. Find the number of employees working in school of civil engineering and as professor
SQL> SELECT COUNT(E.ID) AS PROF_COUNT
  2  FROM EMPLOYEE E
  3  JOIN EMPLOYEE_ALIGNMENT EA ON E.ID = EA.EMPLOYEE_ID
  4  JOIN SCHOOL S ON EA.SCHOOL_ID = S.ID
  5  JOIN EMPLOYEE_PAY EP ON E.ID = EP.EMPLOYEE_ID
  6  JOIN JOB J ON EP.JOB_ID = J.ID
  7  WHERE S.NAME = 'Civil Engineering' AND J.TITLE = 'Professor';

PROF_COUNT
----------
         3

1 row selected.

-- 6.9. Find the employees with minimum salary in their own school in associate professor rank
SQL> SELECT E.FIRST_NAME || ' ' || E.LAST_NAME AS FULL_NAME, J.SALARY, S.NAME
  2  FROM EMPLOYEE E
  3  JOIN EMPLOYEE_PAY EP ON E.ID = EP.EMPLOYEE_ID
  4  JOIN JOB J ON EP.JOB_ID = J.ID
  5  JOIN EMPLOYEE_ALIGNMENT EA ON E.ID = EA.EMPLOYEE_ID
  6  JOIN SCHOOL S ON EA.SCHOOL_ID = S.ID
  7  WHERE J.TITLE = 'Associate Professor'
  8    AND J.SALARY = (SELECT MIN(J2.SALARY) 
  9                    FROM JOB J2 
 10                    JOIN EMPLOYEE_PAY EP2 ON J2.ID = EP2.JOB_ID
 11                    JOIN EMPLOYEE_ALIGNMENT EA2 ON EP2.EMPLOYEE_ID = EA2.EMPLOYEE_ID
 12                    WHERE EA2.SCHOOL_ID = S.ID AND J2.TITLE = 'Associate Professor');

FULL_NAME            SALARY     SCHOOL_NAME
-------------------- ---------- -------------------------
Meenakshi Iyer       95000      Electronic Engineering

1 row selected.

-- 6.10. Find the employees with maximum salary in their own school in professor rank
SQL> SELECT E.FIRST_NAME || ' ' || E.LAST_NAME AS FULL_NAME, J.SALARY, S.NAME
  2  FROM EMPLOYEE E
  3  JOIN EMPLOYEE_PAY EP ON E.ID = EP.EMPLOYEE_ID
  4  JOIN JOB J ON EP.JOB_ID = J.ID
  5  JOIN EMPLOYEE_ALIGNMENT EA ON E.ID = EA.EMPLOYEE_ID
  6  JOIN SCHOOL S ON EA.SCHOOL_ID = S.ID
  7  WHERE J.TITLE = 'Professor'
  8    AND J.SALARY = (SELECT MAX(J2.SALARY) 
  9                    FROM JOB J2 
 10                    JOIN EMPLOYEE_PAY EP2 ON J2.ID = EP2.JOB_ID
 11                    JOIN EMPLOYEE_ALIGNMENT EA2 ON EP2.EMPLOYEE_ID = EA2.EMPLOYEE_ID
 12                    WHERE EA2.SCHOOL_ID = S.ID AND J2.TITLE = 'Professor');

FULL_NAME            SALARY     SCHOOL_NAME
-------------------- ---------- -------------------------
Amit Banerjee        140000     Computer Engineering

1 row selected.

-- 6.11. Find the average salary by each school
SQL> SELECT S.NAME AS SCHOOL_NAME, ROUND(AVG(J.SALARY), 2) AS AVG_SALARY
  2  FROM SCHOOL S
  3  JOIN EMPLOYEE_ALIGNMENT EA ON S.ID = EA.SCHOOL_ID
  4  JOIN EMPLOYEE_PAY EP ON EA.EMPLOYEE_ID = EP.EMPLOYEE_ID
  5  JOIN JOB J ON EP.JOB_ID = J.ID
  6  GROUP BY S.NAME;

SCHOOL_NAME                AVG_SALARY
-------------------------  ----------
Computer Engineering       98500.50
Electronic Engineering     92000.00
Mechanical Engineering     78000.00
Civil Engineering          105000.00

4 rows selected.