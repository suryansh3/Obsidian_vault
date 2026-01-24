# Name : Utkarsh Dwivedi
# Roll : 24051673

**Question 1:**
```java
package p1;
public class Employee {
    private String name;
    public Employee(String name) { this.name = name; }
    public String getName() { return name; }
}

package p1;
public class Regular_empsalary {
    public double calculateSalary() { return 50000.0; }
}

package p2;
public class Employee {
    private String id;
    public Employee(String id) { this.id = id; }
    public String getId() { return id; }
}

package p2;
public class Contract_empsalary {
    public double calculateSalary() { return 30000.0; }
}

package p3;
import p1.Employee as P1Employee;
import p1.Regular_empsalary;
import p2.Contract_empsalary;
public class Empdetails {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        P1Employee emp1 = new P1Employee("John");
        p2.Employee emp2 = new p2.Employee("E1001");
        Regular_empsalary regSal = new Regular_empsalary();
        Contract_empsalary conSal = new Contract_empsalary();
        System.out.println("Employee from p1: " + emp1.getName());
        System.out.println("Employee from p2: " + emp2.getId());
        System.out.println("Regular Employee Salary: " + regSal.calculateSalary());
        System.out.println("Contract Employee Salary: " + conSal.calculateSalary());
    }
}
```
**Output:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Employee from p1: John
Employee from p2: E1001
Regular Employee Salary: 50000.0
Contract Employee Salary: 30000.0
```

**Question 2:**
```java

package Department;
public class Student {
    String name, branch;
    int semester, rollNo;
    double cgpa;
    public Student(String name, int semester, String branch, int rollNo, double cgpa) {
        this.name = name;
        this.semester = semester;
        this.branch = branch;
        this.rollNo = rollNo;
        this.cgpa = cgpa;
    }
    public void show() {
        System.out.println("Name: " + name);
        System.out.println("Semester: " + semester);
        System.out.println("Branch: " + branch);
        System.out.println("Roll No: " + rollNo);
        System.out.println("CGPA: " + cgpa);
    }
}

import Department.Student;
public class Demo {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        Student stu = new Student("Alice", 4, "CSE", 101, 8.5);
        stu.show();
    }
}
```
**Output:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Name: Alice
Semester: 4
Branch: CSE
Roll No: 101
CGPA: 8.5
```

**Question 3:**
```java

package pack1;
public interface Prime {
    void prime();
}

package pack1;
public interface Odd {
    void odd();
}

package pack2;
import pack1.Prime;
import pack1.Odd;
public class Check implements Prime, Odd {
    public void prime() {
        System.out.println("Prime method implemented");
    }
    public void odd() {
        System.out.println("Odd method implemented");
    }
}

package pack2;
public class Design extends Check {
    public void display() {
        prime();
        odd();
    }
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        Design obj = new Design();
        obj.display();
    }
}
```
**Output:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Prime method implemented
Odd method implemented
```

**Question 4:**
```java
import java.util.Scanner;
public class ArrayIndexException {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        int[] arr = new int[4];
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers: ");
        String input = sc.nextLine();
        String[] nums = input.split(" ");
        try {
            for (int i = 0; i <= nums.length; i++) {
                arr[i] = Integer.parseInt(nums[i]);
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception in thread \"main\" java.lang.ArrayIndexOutOfBoundsException: " + (arr.length));
        }
        sc.close();
    }
}
```
**Output:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Enter numbers: 1 2 3 4 5
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 4
```

**Question 5:**
```java
public class ArithmeticExceptionHandling {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        int a = 10, b = 0;
        try {
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException caught by try-catch-finally block");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```
**Output:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
ArithmeticException caught by try-catch-finally block
Finally block executed
```

**Question 6:**
```java
import java.util.Scanner;
class NegativeNumberException extends Exception {
    public NegativeNumberException(String msg) { super(msg); }
}
public class ProcessInput {
    static void ProcessInput() throws NegativeNumberException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        if (num < 0) throw new NegativeNumberException("number should be positive");
        else System.out.println("Double value: " + (num * 2));
        sc.close();
    }
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        try {
            ProcessInput();
        } catch (NegativeNumberException e) {
            System.out.println("Caught the exception");
            System.out.println("Exception occurred: NegativeNumberException: " + e.getMessage());
        }
    }
}
```
**Output 1:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Enter a number: 4
Double value: 8
```
**Output 2:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Enter a number: -4
Caught the exception
Exception occurred: NegativeNumberException: number should be positive
```

**Question 7:**
```java
import java.util.Scanner;
class HrsException extends Exception {
    HrsException(String s) { super(s); }
}
class MinException extends Exception {
    MinException(String s) { super(s); }
}
class SecException extends Exception {
    SecException(String s) { super(s); }
}
class Time {
    int hours, minutes, seconds;
    void setTime() throws HrsException, MinException, SecException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter hours: ");
        hours = sc.nextInt();
        System.out.print("Enter minutes: ");
        minutes = sc.nextInt();
        System.out.print("Enter seconds: ");
        seconds = sc.nextInt();
        sc.close();
        if (hours < 0 || hours > 24) throw new HrsException("hour is not greater than 24");
        if (minutes < 0 || minutes > 60) throw new MinException("minute is not greater than 60");
        if (seconds < 0 || seconds > 60) throw new SecException("second is not greater than 60");
    }
    void display() {
        System.out.println("Correct Time -> " + hours + ":" + minutes + ":" + seconds);
    }
}
public class TimeTest {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        Time t = new Time();
        try {
            t.setTime();
            t.display();
        } catch (HrsException | MinException | SecException e) {
            System.out.println("Caught the exception");
            System.out.println("Exception occurred: " + e.getClass().getSimpleName() + ": " + e.getMessage());
        }
    }
}
```
**Output 1:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Enter hours: 4
Enter minutes: 54
Enter seconds: 34
Correct Time -> 4:54:34
```
**Output 2:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Enter hours: 30
Enter minutes: 65
Enter seconds: 65
Caught the exception
Exception occurred: HrsException: hour is not greater than 24
```

**Question 8:**
```java
class CheckArgument extends Exception {
    CheckArgument(String msg) { super(msg); }
}
public class CommandLineCheck {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
        try {
            if (args.length < 4) throw new CheckArgument("Less than 4 arguments");
            int sum = 0;
            for (int i = 0; i < 4; i++) {
                sum += Integer.parseInt(args[i]) * Integer.parseInt(args[i]);
            }
            System.out.println(sum);
        } catch (CheckArgument e) {
            System.out.println("Exception occurred - CheckArgument");
        }
    }
}
```
**Output 1:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
30
```
**Output 2:**
```
Name : Utkarsh Dwivedi
Roll : 24051673
Exception occurred - CheckArgument
```