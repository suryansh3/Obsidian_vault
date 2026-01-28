SQL> spool LAB_Output.txt
SQL> -- 3.1. Create following tables and insert appropriate rows
SQL> 
SQL> CREATE TABLE EMPLOYEE (
       ID NUMBER PRIMARY KEY,
      LAST_NAME VARCHAR2(50),
       FIRST_NAME VARCHAR2(50),
        MIDDLE_NAME VARCHAR2(50),
        FATHER_NAME VARCHAR2(50),
      MOTHER_NAME VARCHAR2(50),
        SEX CHAR(1),
        HIRE_DATE DATE,
       ADDRESS VARCHAR2(100),
       CITY VARCHAR2(50),
       STATE VARCHAR2(50),
       ZIP VARCHAR2(10),
 14      PHONE VARCHAR2(15),
 15      PAGER VARCHAR2(15)
 16  );

Table created.

SQL> CREATE TABLE SCHOOL (
  2      ID NUMBER PRIMARY KEY,
  3      NAME VARCHAR2(100)
  4  );

Table created.

SQL> CREATE TABLE EMPLOYEE_ALIGNMENT (
  2      EMPLOYEE_ID NUMBER,
  3      SCHOOL_ID NUMBER
  4  );

Table created.

SQL> CREATE TABLE JOB (
  2      ID NUMBER PRIMARY KEY,
  3      NAME VARCHAR2(50),
  4      TITLE VARCHAR2(50),
  5      SALARY NUMBER,
  6      BONUS NUMBER
  7  );

Table created.

SQL> CREATE TABLE EMPLOYEE_PAY (
  2      EMPLOYEE_ID NUMBER,
  3      JOB_ID NUMBER
  4  );

Table created.

SQL> CREATE TABLE PRODUCT (
  2      ID NUMBER PRIMARY KEY,
  3      NAME VARCHAR2(50),
  4      "DESC" VARCHAR2(100),
  5      STATUS VARCHAR2(20),
  6      CREATED_DATE DATE,
  7      CREATED_BY VARCHAR2(50),
  8      LAST_MODIFIED_DATE DATE,
  9      LAST_MODIFIED_BY VARCHAR2(50),
 10      COST NUMBER,
 11      INJECTED_DATE DATE
 12  );

Table created.

SQL> 
SQL> -- Inserting Sample Data
SQL> INSERT INTO JOB VALUES (1, 'Acad', 'Associate Professor', 95000, 4000);

1 row created.

SQL> INSERT INTO JOB VALUES (2, 'Acad', 'Associate Professor', 70000, 3000);

1 row created.

SQL> INSERT INTO JOB VALUES (3, 'Admin', 'Lecturer', 78000, 5000);

1 row created.

SQL> INSERT INTO JOB VALUES (4, 'Res', 'Professor', 110000, 10000);

1 row created.

SQL> INSERT INTO PRODUCT VALUES (101, 'Widget A', 'Alpha Widget', 'Active', SYSDATE, 'Indiana D', SYSDATE, 'Admin', 50, SYSDATE);

1 row created.

SQL> INSERT INTO PRODUCT VALUES (102, 'Widget B', 'Beta Widget', 'Active', SYSDATE, 'Ohio D', SYSDATE, 'Admin', 60, SYSDATE);

1 row created.

SQL> INSERT INTO PRODUCT VALUES (103, 'Widget C', 'Gamma Widget', 'Inactive', SYSDATE, 'Texas T', SYSDATE, 'Admin', 70, SYSDATE);

1 row created.

SQL> 
SQL> -- 3.2. Retrieve the row count in "Associate Professor" title.
SQL> SELECT COUNT(*) FROM JOB WHERE TITLE = 'Associate Professor';

  COUNT(*)
----------
         2

SQL> 
SQL> -- 3.3. Retrieve the row count in "Associate Professor" title whose salary is between 80,000 and 100,000.
SQL> SELECT COUNT(*) FROM JOB WHERE TITLE = 'Associate Professor' AND SALARY BETWEEN 80000 AND 100000;

  COUNT(*)
----------
         1

SQL> 
SQL> -- 3.4. Retrieve the details of jobs whose sum of salary and bonus is falling in the range 80,000 and 100,000.
SQL> SELECT * FROM JOB WHERE (SALARY + BONUS) BETWEEN 80000 AND 100000;

        ID NAME                 TITLE                  SALARY      BONUS
---------- -------------------- ------------------ ---------- ----------
         1 Acad                 Associate Professor     95000       4000
         3 Admin                Lecturer                78000       5000

SQL> 
SQL> -- 3.5. What is the average salary?
SQL> SELECT AVG(SALARY) FROM JOB;

AVG(SALARY)
-----------
      88250

SQL> 
SQL> -- 3.6. What is the maximum bonus?
SQL> SELECT MAX(BONUS) FROM JOB;

MAX(BONUS)
----------
     10000

SQL> 
SQL> -- 3.7. Write a SELECT statement that returns product IDs and description (alpha order) for the product, 
SQL> -- created by Indiana D or Ohio D or Michigan R, or Illinois M.
SQL> SELECT ID, "DESC" FROM PRODUCT 
  2  WHERE CREATED_BY IN ('Indiana D', 'Ohio D', 'Michigan R', 'Illinois M') 
  3  ORDER BY "DESC";

        ID DESC
---------- --------------------------------------------------
       101 Alpha Widget
       102 Beta Widget

SQL> spool off