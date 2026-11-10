---
course: "DBMS"
semester: 4
tags:
  - course/dbms
up: "[[DBMS]]"
---
SET ECHO ON;
SET FEEDBACK ON;
SPOOL assignment_output.txt;

-- ==========================================================
-- 3.1. Create Tables and Insert Rows
-- ==========================================================

CREATE TABLE EMPLOYEE (
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

CREATE TABLE SCHOOL (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(100)
);

CREATE TABLE EMPLOYEE_ALIGNMENT (
    EMPLOYEE_ID NUMBER REFERENCES EMPLOYEE(ID),
    SCHOOL_ID NUMBER REFERENCES SCHOOL(ID)
);

CREATE TABLE JOB (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
    TITLE VARCHAR2(50),
    SALARY NUMBER(10,2),
    BONUS NUMBER(10,2)
);

CREATE TABLE EMPLOYEE_PAY (
    EMPLOYEE_ID NUMBER REFERENCES EMPLOYEE(ID),
    JOB_ID NUMBER REFERENCES JOB(ID)
);

CREATE TABLE PRODUCT (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
    DESCRIPTION VARCHAR2(200),
    STATUS VARCHAR2(20),
    CREATED_DATE DATE,
    CREATED_BY VARCHAR2(50),
    LAST_MODIFIED_DATE DATE,
    LAST_MODIFIED_BY VARCHAR2(50),
    COST NUMBER(10,2),
    INJECTED_DATE DATE
);

-- Inserting 5 Rows for each table (Indian Context)
INSERT ALL
INTO EMPLOYEE VALUES (1, 'Sharma', 'Rajesh', 'Kumar', 'Suresh Sharma', 'Anita Sharma', 'M', '10-JAN-2020', 'Sector 15', 'Gurgaon', 'Haryana', '122001', '9876543210', 'N/A')
INTO EMPLOYEE VALUES (2, 'Iyer', 'Meenakshi', NULL, 'Sundar Iyer', 'Lakshmi Iyer', 'F', '15-MAR-2018', 'Adyar', 'Chennai', 'Tamil Nadu', '600020', '9876543211', 'N/A')
INTO EMPLOYEE VALUES (3, 'Banerjee', 'Amit', 'Pratim', 'Sajal Banerjee', 'Rina Banerjee', 'M', '22-JUN-2015', 'Salt Lake', 'Kolkata', 'West Bengal', '700091', '9876543212', 'N/A')
INTO EMPLOYEE VALUES (4, 'Patel', 'Hardik', NULL, 'Mahesh Patel', 'Geeta Patel', 'M', '05-FEB-2021', 'Navrangpura', 'Ahmedabad', 'Gujarat', '380009', '9876543213', 'N/A')
INTO EMPLOYEE VALUES (5, 'Reddy', 'Priyanka', NULL, 'Venkat Reddy', 'Kavitha Reddy', 'F', '12-DEC-2019', 'Banjara Hills', 'Hyderabad', 'Telangana', '500034', '9876543214', 'N/A')
SELECT * FROM DUAL;

INSERT ALL
INTO SCHOOL VALUES (101, 'IIT Kharagpur')
INTO SCHOOL VALUES (102, 'Delhi University')
INTO SCHOOL VALUES (103, 'Jadavpur University')
INTO SCHOOL VALUES (104, 'Anna University')
INTO SCHOOL VALUES (105, 'BITS Pilani')
SELECT * FROM DUAL;

INSERT ALL
INTO EMPLOYEE_ALIGNMENT VALUES (1, 101)
INTO EMPLOYEE_ALIGNMENT VALUES (2, 104)
INTO EMPLOYEE_ALIGNMENT VALUES (3, 103)
INTO EMPLOYEE_ALIGNMENT VALUES (4, 105)
INTO EMPLOYEE_ALIGNMENT VALUES (5, 102)
SELECT  * FROM DUAL;

INSERT ALL
INTO JOB VALUES (501, 'Teaching', 'Associate Professor', 85000, 5000)
INTO JOB VALUES (502, 'Research', 'Scientist', 95000, 10000)
INTO JOB VALUES (503, 'Teaching', 'Associate Professor', 110000, 8000)
INTO JOB VALUES (504, 'Admin', 'Registrar', 75000, 2000)
INTO JOB VALUES (505, 'Teaching', 'Assistant Professor', 60000, 3000)
SELECT * FROM DUAL;

INSERT ALL
INTO EMPLOYEE_PAY VALUES (1, 501)
INTO EMPLOYEE_PAY VALUES (2, 502)
INTO EMPLOYEE_PAY VALUES (3, 503)
INTO EMPLOYEE_PAY VALUES (4, 504)
INTO EMPLOYEE_PAY VALUES (5, 505)
SELECT * FROM DUAL;

INSERT ALL
INTO PRODUCT VALUES (1, 'Textbook', 'Advanced DBMS', 'Active', '01-JAN-2024', 'Indiana D', '05-JAN-2024', 'Admin', 500, '01-JAN-2024')
INTO PRODUCT VALUES (2, 'Lab Kit', 'Networking Basics', 'Active', '02-JAN-2024', 'Ohio D', '06-JAN-2024', 'Admin', 1500, '02-JAN-2024')
INTO PRODUCT VALUES (3, 'Software', 'Query Optimizer', 'Pending', '03-JAN-2024', 'Michigan R', '07-JAN-2024', 'Admin', 25000, '03-JAN-2024')
INTO PRODUCT VALUES (4, 'Tablet', 'Educational Tablet', 'Active', '04-JAN-2024', 'Illinois M', '08-JAN-2024', 'Admin', 12000, '04-JAN-2024')
INTO PRODUCT VALUES (5, 'License', 'Oracle Cloud', 'Active', '05-JAN-2024', 'Indiana D', '09-JAN-2024', 'Admin', 50000, '05-JAN-2024')
SELECT * FROM DUAL;

COMMIT;

-- ==========================================================
-- 3.2. Retrieve row count in “Associate Professor” title
-- ==========================================================
SELECT COUNT(*) AS ASSOC_PROF_COUNT FROM JOB WHERE TITLE = 'Associate Professor';

-- ==========================================================
-- 3.3. Row count in “Associate Professor” with salary 80k-100k
-- ==========================================================
SELECT COUNT(*) AS FILTERED_PROF_COUNT FROM JOB 
WHERE TITLE = 'Associate Professor' AND SALARY BETWEEN 80000 AND 100000;

-- ==========================================================
-- 3.4. Jobs where (Salary + Bonus) is between 80,000 and 100,000
-- ==========================================================
SELECT * FROM JOB WHERE (SALARY + BONUS) BETWEEN 80000 AND 100000;

-- ==========================================================
-- 3.5. Average Salary
-- ==========================================================
SELECT AVG(SALARY) AS AVERAGE_SALARY FROM JOB;

-- ==========================================================
-- 3.6. Maximum Bonus
-- ==========================================================
SELECT MAX(BONUS) AS MAX_BONUS FROM JOB;

-- ==========================================================
-- 3.7. Product IDs/Desc for specific creators (Alpha order)
-- ==========================================================
SELECT ID, DESCRIPTION 
FROM PRODUCT 
WHERE CREATED_BY IN ('Indiana D', 'Ohio D', 'Michigan R', 'Illinois M')
ORDER BY DESCRIPTION ASC;

SPOOL OFF;

SET ECHO ON;
SET FEEDBACK ON;

-- ==========================================================
-- 4.2. Max and Min cost by each Product Creator
-- ==========================================================
SELECT CREATED_BY, MAX(COST) AS MAX_COST, MIN(COST) AS MIN_COST 
FROM PRODUCT 
GROUP BY CREATED_BY;

-- ==========================================================
-- 4.3. Sum and Average cost by each Last Modifier
-- ==========================================================
SELECT LAST_MODIFIED_BY, SUM(COST) AS TOTAL_COST, AVG(COST) AS AVG_COST 
FROM PRODUCT 
GROUP BY LAST_MODIFIED_BY;

-- ==========================================================
-- 4.4. Number of products created by Indiana D or Ohio D
-- ==========================================================
SELECT COUNT(*) AS PRODUCT_COUNT 
FROM PRODUCT 
WHERE CREATED_BY IN ('Indiana D', 'Ohio D');

-- ==========================================================
-- 4.5. Number of products updated by Michigan R or Illinois M
-- ==========================================================
SELECT COUNT(*) AS UPDATE_COUNT 
FROM PRODUCT 
WHERE LAST_MODIFIED_BY IN ('Michigan R', 'Illinois M');

-- ==========================================================
-- 4.6. Sum of all salary
-- ==========================================================
SELECT SUM(SALARY) AS TOTAL_SALARY_EXPENDITURE FROM JOB;

-- ==========================================================
-- 4.7. Average salary across all non-null bonus values
-- ==========================================================
SELECT AVG(SALARY) AS AVG_SALARY_WITH_BONUS 
FROM JOB 
WHERE BONUS IS NOT NULL;

-- ==========================================================
-- 4.8. Average, highest and lowest cost for the products
-- ==========================================================
SELECT AVG(COST) AS AVG_COST, MAX(COST) AS MAX_COST, MIN(COST) AS MIN_COST 
FROM PRODUCT;

-- ==========================================================
-- 4.9. Total number of jobs for null bonus values
-- ==========================================================
SELECT COUNT(*) AS NULL_BONUS_JOB_COUNT 
FROM JOB 
WHERE BONUS IS NULL;

-- ==========================================================
-- 4.10. Year and Month of created and last modified dates
-- ==========================================================
SELECT NAME, 
       EXTRACT(YEAR FROM CREATED_DATE) AS CREATED_YEAR, 
       EXTRACT(MONTH FROM CREATED_DATE) AS CREATED_MONTH,
       EXTRACT(YEAR FROM LAST_MODIFIED_DATE) AS MODIFIED_YEAR,
       EXTRACT(MONTH FROM LAST_MODIFIED_DATE) AS MODIFIED_MONTH
FROM PRODUCT;

-- ==========================================================
-- 4.11. Job Title with Salary Category (High, Medium, Low)
-- ==========================================================
SELECT NAME, TITLE, 
       CASE 
          WHEN SALARY > 100000 THEN 'High'
          WHEN SALARY BETWEEN 50000 AND 100000 THEN 'Medium'
          ELSE 'Low'
       END AS SALARY_LEVEL
FROM JOB;

-- ==========================================================
-- 4.12. Concatenation of Product details for Active products
-- ==========================================================
-- Note: TO_CHAR is used to ensure dates are converted to string for concatenation
SELECT NAME || ' - ' || DESCRIPTION || ' (Created: ' || TO_CHAR(CREATED_DATE, 'DD-MON-YYYY') || 
       ', Updated: ' || TO_CHAR(LAST_MODIFIED_DATE, 'DD-MON-YYYY') || ')' AS PRODUCT_DETAILS
FROM PRODUCT 
WHERE STATUS = 'Active';

COMMIT;

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DBMS]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** - · **Next:** [[04 - Academics & CS/Semester 4/DBMS/DBMS - SQL Views|DBMS - SQL Views]]
> **Related:** [[OOPJ (Java)]] · [[DAWR]] · [[Projects]]
<!-- connections:end -->
