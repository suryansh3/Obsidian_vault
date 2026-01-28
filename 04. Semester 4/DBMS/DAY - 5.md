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
     PHONE VARCHAR2(15),
      PAGER VARCHAR2(15)
   );

Table created.

SQL> CREATE TABLE SCHOOL (
      ID NUMBER PRIMARY KEY,
       NAME VARCHAR2(100)
   );

Table created.

SQL> CREATE TABLE EMPLOYEE_ALIGNMENT (
    EMPLOYEE_ID NUMBER,
      SCHOOL_ID NUMBER
   );

Table created.

SQL> CREATE TABLE JOB (
     ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
     TITLE VARCHAR2(50),
     SALARY NUMBER,
     BONUS NUMBER
 );

Table created.

SQL> CREATE TABLE EMPLOYEE_PAY (
   EMPLOYEE_ID NUMBER,
   JOB_ID NUMBER
   );

Table created.

SQL> CREATE TABLE PRODUCT (
       ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
      "DESC" VARCHAR2(100),
        STATUS VARCHAR2(20),
       CREATED_DATE DATE,
       CREATED_BY VARCHAR2(50),
        LAST_MODIFIED_DATE DATE,
       LAST_MODIFIED_BY VARCHAR2(50),
      COST NUMBER,
       INJECTED_DATE DATE
  );

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



SQL> -- Adding 5 more rows to all tables in a single command using INSERT ALL
SQL> INSERT ALL

    INTO EMPLOYEE VALUES (1, 'S', 'John', 'A', 'Robert', 'Mary', 'M', '10-JAN-23', '123 Maple St', 'New York', 'NY', '10001', '555-1234', '1001')
  4    INTO EMPLOYEE VALUES (2, 'Doe', 'Jane', 'B', 'Michael', 'Susan', 'F', '15-FEB-23', '456 Oak Ave', 'Chicago', 'IL', '60601', '555-5678', '1002')
  5    INTO EMPLOYEE VALUES (3, 'Brown', 'Charlie', 'C', 'David', 'Linda', 'M', '20-MAR-23', '789 Pine Rd', 'Houston', 'TX', '77001', '555-9012', '1003')
  6    INTO EMPLOYEE VALUES (4, 'Wilson', 'Emily', 'D', 'James', 'Patricia', 'F', '25-APR-23', '101 Elm Blvd', 'Phoenix', 'AZ', '85001', '555-3456', '1004')
  7    INTO EMPLOYEE VALUES (5, 'Davis', 'Frank', 'E', 'William', 'Barbara', 'M', '30-MAY-23', '202 Cedar Ln', 'Philadelphia', 'PA', '19101', '555-7890', '1005')
  8    -- Inserting 5 rows into SCHOOL
  9    INTO SCHOOL VALUES (10, 'School of Engineering')
 10    INTO SCHOOL VALUES (20, 'School of Business')
 11    INTO SCHOOL VALUES (30, 'School of Arts')
 12    INTO SCHOOL VALUES (40, 'School of Science')
 13    INTO SCHOOL VALUES (50, 'School of Medicine')
 14    -- Inserting 5 rows into EMPLOYEE_ALIGNMENT
 15    INTO EMPLOYEE_ALIGNMENT VALUES (1, 10)
 16    INTO EMPLOYEE_ALIGNMENT VALUES (2, 20)
 17    INTO EMPLOYEE_ALIGNMENT VALUES (3, 30)
 18    INTO EMPLOYEE_ALIGNMENT VALUES (4, 40)
 19    INTO EMPLOYEE_ALIGNMENT VALUES (5, 50)
 20    -- Inserting 5 rows into JOB (IDs continuing from previous 4)
 21    INTO JOB VALUES (5, 'Admin', 'Clerk', 40000, 1000)
 22    INTO JOB VALUES (6, 'Acad', 'Assistant Professor', 65000, 2500)
 23    INTO JOB VALUES (7, 'Maint', 'Technician', 45000, 1500)
 24    INTO JOB VALUES (8, 'IT', 'Developer', 75000, 3500)
 25    INTO JOB VALUES (9, 'HR', 'Manager', 85000, 4500)
 26    -- Inserting 5 rows into EMPLOYEE_PAY
 27    INTO EMPLOYEE_PAY VALUES (1, 5)
 28    INTO EMPLOYEE_PAY VALUES (2, 6)
 29    INTO EMPLOYEE_PAY VALUES (3, 7)
 30    INTO EMPLOYEE_PAY VALUES (4, 8)
 31    INTO EMPLOYEE_PAY VALUES (5, 9)
 32    -- Inserting 5 rows into PRODUCT (IDs continuing from previous 103)
 33    INTO PRODUCT VALUES (104, 'Widget D', 'Delta Widget', 'Active', SYSDATE, 'Michigan R', SYSDATE, 'Admin', 55, SYSDATE)
 34    INTO PRODUCT VALUES (105, 'Widget E', 'Epsilon Widget', 'Inactive', SYSDATE, 'Illinois M', SYSDATE, 'Admin', 65, SYSDATE)
 35    INTO PRODUCT VALUES (106, 'Widget F', 'Zeta Widget', 'Active', SYSDATE, 'Indiana D', SYSDATE, 'Admin', 75, SYSDATE)
 36    INTO PRODUCT VALUES (107, 'Widget G', 'Eta Widget', 'Active', SYSDATE, 'Ohio D', SYSDATE, 'Admin', 85, SYSDATE)
 37    INTO PRODUCT VALUES (108, 'Widget H', 'Theta Widget', 'Active', SYSDATE, 'Michigan R', SYSDATE, 'Admin', 95, SYSDATE)
 38