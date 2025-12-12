# 1.
``` Java
import java.util.Scanner;
public class ReadusingMethod {
    public static void readRecord() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== Enter Student Details ===");
        System.out.print("Enter Student ID: ");
        String studentId = scanner.nextLine();
        System.out.print("Enter Student Name: ");
        String name = scanner.nextLine();
        displayStudentRecord(studentId, name);
        scanner.close();
    }
    public static void displayRecord(String id, String name) {
        System.out.println("\n=== Student Record ===");
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
    }
    public static void main(String[] args) {
        readRecord();
    }
}
```

# OUTPUT
![[Pasted image 20251208184108.png]]
Enter Student ID: 24052323
Enter Student Name: Shivam Raj

Student Record 
ID: 24052323
Name: Shivam Raj

---
# 2. 

``` jAVA
import java.util.*;
class Student {
    String studentId;
    String name;
    public void inputStudentDetails() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Student ID: ");
        this.studentId = scanner.nextLine();
        System.out.print("Enter Full Name: ");
        this.name = scanner.nextLine();
    }
    public void displayStudentDetails() {
        System.out.println("\n----- Student Record -----");
        System.out.println("ID: " + studentId);
        System.out.println("Name: " + name);
    }
    public String getStudentId() {
        return studentId;
    }
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
public class StudentRecordWithClass {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many students do you want to enter? ");
        int numStudents = scanner.nextInt();
        scanner.nextLine();
        Student[] students = new Student[numStudents];
    for (int i = 0; i < numStudents; i++) {
    System.out.println("\n  Enter details for Student " + (i + 1) + "    ");
    students[i] = new Student();
    students[i].inputStudentDetails();
		}
        System.out.println("\n--- All Student Records ----2");
        for (int i = 0; i < numStudents; i++) {
            students[i].displayStudentDetails();
        }
    }
}
```

# OUTPUT
How many students do you want to enter? 10

  Enter details for Student 1
Enter Student ID: 24042323
Enter Full Name: Shivam Raj

  Enter details for Student 2
Enter Student ID: 24155220
Enter Full Name: Vivek Singh

  Enter details for Student 3
Enter Student ID: 24155060
Enter Full Name: Suryansh

  Enter details for Student 4
Enter Student ID: 24052324
Enter Full Name: Shreyash

  Enter details for Student 5
Enter Student ID: 24052339
Enter Full Name: Aditya Pranjal

  Enter details for Student 6
Enter Student ID: 24054823
Enter Full Name: Keshav

  Enter details for Student 7
Enter Student ID: 24155006
Enter Full Name: Aditya Raj

  Enter details for Student 8
Enter Student ID: 24055004
Enter Full Name: Aditya Kumar

  Enter details for Student 9
Enter Student ID: 2405005
Enter Full Name: Shreyash Raj

  Enter details for Student 10
Enter Student ID: 24155059
Enter Full Name: Suryakant 

--- All Student Records ----2

Student Record 
ID: 24052323
Name: Shivam Raj

 Student Record 
ID: 24155220
Name: Vivek Singh

Student Record 
ID: 24155060
Name:  Suryansh

Student Record 
ID: 24052324
Name: Shreyash

Student Record 
ID: 24052339
Name: Aditya Pranjal

Student Record 
ID: 24054823
Name: Keshav

 Student Record 
ID: 24155006
Name: Aditya Raj

 Student Record 
ID: 24055004
Name: Aditya Kumar

 Student Record 
ID: 2405005
Name: Shreyash Raj

Student Record 
ID: 24155059
Name: Suryakant 
