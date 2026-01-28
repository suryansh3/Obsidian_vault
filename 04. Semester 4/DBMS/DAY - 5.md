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
SQL> INSERT INSERT INTO JOB VALUES (1, 'Acad', 'Associate Professor', 95000, 4000);

1 row created.

SQL> INSERT INSERT INTO JOB VALUES (2, 'Acad', 'Associate Professor', 70000, 3000);

1 row created.

SQL> INSERT INSERT INTO JOB VALUES (3, 'Admin', 'Lecturer', 78000, 5000);

1 row created.

SQL> INSERT INSERT INTO JOB VALUES (4, 'Res', 'Professor', 110000, 10000);

1 row created.

SQL> INSERT INSERT INTO PRODUCT VALUES (101, 'Widget A', 'Alpha Widget', 'Active', SYSDATE, 'Indiana D', SYSDATE, 'Admin', 50, SYSDATE);

1 row created.

SQL> INSERT INSERT INTO PRODUCT VALUES (102, 'Widget B', 'Beta Widget', 'Active', SYSDATE, 'Ohio D', SYSDATE, 'Admin', 60, SYSDATE);

1 row created.

SQL> INSERT INSERT INTO PRODUCT VALUES (103, 'Widget C', 'Gamma Widget', 'Inactive', SYSDATE, 'Texas T', SYSDATE, 'Admin', 70, SYSDATE);

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


INSERT ALL
  -- Inserting 5 rows INSERT INTO EMPLOYEE (IDs 3-7)
  INSERT INTO EMPLOYEE VALUES (3, 'Sharma', 'Rahul', 'Kumar', 'Rajesh', 'Suman', 'M', '12-JAN-24', 'Sector 62', 'Noida', 'UP', '201301', '9876543210', '2001')
  INSERT INTO EMPLOYEE VALUES (4, 'Verma', 'Aditi', NULL, 'Sanjay', 'Meena', 'F', '15-FEB-24', 'Koramangala', 'Bangalore', 'KA', '560034', '9876543211', '2002')
  INSERT INTO EMPLOYEE VALUES (5, 'Patel', 'Arjun', 'B', 'Hasmukh', 'Falguni', 'M', '20-MAR-24', 'Navrangpura', 'Ahmedabad', 'GJ', '380009', '9876543212', '2003')
  INSERT INTO EMPLOYEE VALUES (6, 'Mukherjee', 'Sneha', NULL, 'Pradip', 'Moushumi', 'F', '10-APR-24', 'Salt Lake', 'Kolkata', 'WB', '700091', '9876543213', '2004')
  INSERT INTO EMPLOYEE VALUES (7, 'Reddy', 'Karthik', 'S', 'Vasudev', 'Anjali', 'M', '05-MAY-24', 'Banjara Hills', 'Hyderabad', 'TS', '500034', '9876543214', '2005')

  -- Inserting 5 rows INSERT INTO SCHOOL (IDs 60-100)
  INSERT INTO SCHOOL VALUES (60, 'Indian Institute of Technology Bombay')
  INSERT INTO SCHOOL VALUES (70, 'Delhi University')
  INSERT INTO SCHOOL VALUES (80, 'National Institute of Technology Trichy')
  INSERT INTO SCHOOL VALUES (90, 'Jadavpur University')
  INSERT INTO SCHOOL VALUES (100, 'Anna University')

  -- Inserting 5 rows INSERT INTO EMPLOYEE_ALIGNMENT (Mapping Employees 6-10 to Schools 60-100)
  INSERT INTO EMPLOYEE_ALIGNMENT VALUES (3, 60)
  INSERT INTO EMPLOYEE_ALIGNMENT VALUES (4, 70)
  INSERT INTO EMPLOYEE_ALIGNMENT VALUES (5, 80)
  INSERT INTO EMPLOYEE_ALIGNMENT VALUES (6, 90)
  INSERT INTO EMPLOYEE_ALIGNMENT VALUES (7, 100)

  -- Inserting 5 rows INSERT INTO JOB (IDs 10-14)
  INSERT INTO JOB VALUES (10, 'Admin', 'Dean', 120000, 15000)
  INSERT INTO JOB VALUES (11, 'Acad', 'Senior Lecturer', 85000, 6000)
  INSERT INTO JOB VALUES (12, 'Res', 'Junior Scientist', 55000, 4000)
  INSERT INTO JOB VALUES (13, 'Tech', 'Lab Assistant', 35000, 2000)
  INSERT INTO JOB VALUES (14, 'Acct', 'Accountant', 48000, 3000)

  INSERT ALL
  INTO EMPLOYEE_PAY VALUES (3, 10)
  INTO EMPLOYEE_PAY VALUES (4, 11)
  INTO EMPLOYEE_PAY VALUES (5, 12)
  INTO EMPLOYEE_PAY VALUES (6, 13)
  INTO EMPLOYEE_PAY VALUES (7, 14)
  SELECT * FROM DUAL;

INSERT ALL
  INTO PRODUCT VALUES (109, 'EduTab', 'Student Tablet', 'Active', SYSDATE, 'Rahul Sharma', SYSDATE, 'Admin', 150, SYSDATE)
  INTO PRODUCT VALUES (110, 'SolarLamp', 'Study Light', 'Active', SYSDATE, 'Aditi Verma', SYSDATE, 'Admin', 40, SYSDATE)
  INTO PRODUCT VALUES (111, 'AgriSens', 'Soil Sensor', 'Inactive', SYSDATE, 'Arjun Patel', SYSDATE, 'Admin', 80, SYSDATE)
  INTO PRODUCT VALUES (112, 'WaterPurifier', 'Home Filter', 'Active', SYSDATE, 'Sneha M', SYSDATE, 'Admin', 90, SYSDATE)
  INTO PRODUCT VALUES (113, 'HealthKit', 'First Aid Box', 'Active', SYSDATE, 'Karthik Reddy', SYSDATE, 'Admin', 25, SYSDATE)
SELECT * FROM dual;