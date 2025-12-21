
## **Program 1: Student with Highest Average Marks**

```java
import java.util.Scanner;

class Student {
    String studentName;
    int rollNumber;
    double subject1;
    double subject2;
    double subject3;
}

public class Program1 {
    public static void main(String[] args) {
        Scanner abc = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int xyz = abc.nextInt();
        
        Student[] arr = new Student[xyz];
        
        for (int i = 0; i < xyz; i++) {
            arr[i] = new Student();
            abc.nextLine();
            
            System.out.println("Enter name for student " + (i+1) + ": ");
            arr[i].studentName = abc.nextLine();
            
            System.out.println("Enter roll number: ");
            arr[i].rollNumber = abc.nextInt();
            
            System.out.println("Enter marks for 3 subjects: ");
            arr[i].subject1 = abc.nextDouble();
            arr[i].subject2 = abc.nextDouble();
            arr[i].subject3 = abc.nextDouble();
        }
        
        double maxAvg = 0;
        int index = 0;
        
        for (int i = 0; i < xyz; i++) {
            double avg = (arr[i].subject1 + arr[i].subject2 + arr[i].subject3) / 3;
            if (avg > maxAvg) {
                maxAvg = avg;
                index = i;
            }
        }
        
        System.out.println("\nStudent with highest average marks:");
        System.out.println("Name: " + arr[index].studentName);
        System.out.println("Roll Number: " + arr[index].rollNumber);
        System.out.println("Average Marks: " + maxAvg);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        abc.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
3
Enter name for student 1: 
Raj
Enter roll number: 
101
Enter marks for 3 subjects: 
85 90 88
Enter name for student 2: 
Priya
Enter roll number: 
102
Enter marks for 3 subjects: 
92 89 94
Enter name for student 3: 
Amit
Enter roll number: 
103
Enter marks for 3 subjects: 
78 85 80

Student with highest average marks:
Name: Priya
Roll Number: 102
Average Marks: 91.66666666666667

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 2: Sort Employees by Salary**

```java
import java.util.Scanner;

class Employee {
    String name;
    int id;
    double salary;
}

public class Program2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("How many employees? ");
        int count = input.nextInt();
        input.nextLine();
        
        Employee[] emp = new Employee[count];
        
        for (int i = 0; i < count; i++) {
            emp[i] = new Employee();
            
            System.out.println("Enter name: ");
            emp[i].name = input.nextLine();
            
            System.out.println("Enter ID: ");
            emp[i].id = input.nextInt();
            
            System.out.println("Enter salary: ");
            emp[i].salary = input.nextDouble();
            input.nextLine();
        }
        
        for (int i = 0; i < count - 1; i++) {
            for (int j = 0; j < count - i - 1; j++) {
                if (emp[j].salary > emp[j + 1].salary) {
                    Employee temp = emp[j];
                    emp[j] = emp[j + 1];
                    emp[j + 1] = temp;
                }
            }
        }
        
        System.out.println("\nEmployees sorted by salary:");
        for (int i = 0; i < count; i++) {
            System.out.println(emp[i].name + " - " + emp[i].salary);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
How many employees? 
4
Enter name: 
Rahul
Enter ID: 
101
Enter salary: 
45000
Enter name: 
Sneha
Enter ID: 
102
Enter salary: 
38000
Enter name: 
Arun
Enter ID: 
103
Enter salary: 
52000
Enter name: 
Meera
Enter ID: 
104
Enter salary: 
41000

Employees sorted by salary:
Sneha - 38000.0
Meera - 41000.0
Rahul - 45000.0
Arun - 52000.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 3: BankAccount Total Balance**

```java
import java.util.Scanner;

class BankAccount {
    String accNumber;
    String accType;
    double balance;
}

public class Program3 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of accounts: ");
        int num = scan.nextInt();
        scan.nextLine();
        
        BankAccount[] accounts = new BankAccount[num];
        
        for (int i = 0; i < num; i++) {
            accounts[i] = new BankAccount();
            
            System.out.println("Enter account number: ");
            accounts[i].accNumber = scan.nextLine();
            
            System.out.println("Enter account type (savings/current): ");
            accounts[i].accType = scan.nextLine();
            
            System.out.println("Enter balance: ");
            accounts[i].balance = scan.nextDouble();
            scan.nextLine();
        }
        
        double total = 0;
        for (int i = 0; i < num; i++) {
            if (accounts[i].accType.equalsIgnoreCase("savings")) {
                total += accounts[i].balance;
            }
        }
        
        System.out.println("\nTotal balance of all savings accounts: " + total);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of accounts: 
5
Enter account number: 
SB1001
Enter account type (savings/current): 
savings
Enter balance: 
50000
Enter account number: 
CU2001
Enter account type (savings/current): 
current
Enter balance: 
100000
Enter account number: 
SB1002
Enter account type (savings/current): 
savings
Enter balance: 
75000
Enter account number: 
SB1003
Enter account type (savings/current): 
savings
Enter balance: 
30000
Enter account number: 
CU2002
Enter account type (savings/current): 
current
Enter balance: 
80000

Total balance of all savings accounts: 155000.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 4: Books Published After Year**

```java
import java.util.Scanner;

class Book {
    String title;
    String author;
    int year;
}

public class Program4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of books: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        Book[] books = new Book[n];
        
        for (int i = 0; i < n; i++) {
            books[i] = new Book();
            
            System.out.println("Enter book title: ");
            books[i].title = sc.nextLine();
            
            System.out.println("Enter author: ");
            books[i].author = sc.nextLine();
            
            System.out.println("Enter publication year: ");
            books[i].year = sc.nextInt();
            sc.nextLine();
        }
        
        System.out.println("Enter year to filter books published after: ");
        int filterYear = sc.nextInt();
        
        System.out.println("\nBooks published after " + filterYear + ":");
        for (int i = 0; i < n; i++) {
            if (books[i].year > filterYear) {
                System.out.println(books[i].title + " by " + books[i].author + " (" + books[i].year + ")");
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of books: 
4
Enter book title: 
Java Basics
Enter author: 
John Doe
Enter publication year: 
2015
Enter book title: 
Python Guide
Enter author: 
Jane Smith
Enter publication year: 
2020
Enter book title: 
C++ Programming
Enter author: 
Mike Johnson
Enter publication year: 
2018
Enter book title: 
Web Development
Enter author: 
Sarah Lee
Enter publication year: 
2022
Enter year to filter books published after: 
2019

Books published after 2019:
Python Guide by Jane Smith (2020)
Web Development by Sarah Lee (2022)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 5: Count Cars by Brand**

```java
import java.util.Scanner;

class Car {
    String brand;
    String model;
    int year;
    double price;
}

public class Program5 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.println("Enter number of cars: ");
        int carCount = s.nextInt();
        s.nextLine();
        
        Car[] cars = new Car[carCount];
        
        for (int i = 0; i < carCount; i++) {
            cars[i] = new Car();
            
            System.out.println("Enter brand: ");
            cars[i].brand = s.nextLine();
            
            System.out.println("Enter model: ");
            cars[i].model = s.nextLine();
            
            System.out.println("Enter year: ");
            cars[i].year = s.nextInt();
            
            System.out.println("Enter price: ");
            cars[i].price = s.nextDouble();
            s.nextLine();
        }
        
        System.out.println("Enter brand to count: ");
        String searchBrand = s.nextLine();
        
        int count = 0;
        for (int i = 0; i < carCount; i++) {
            if (cars[i].brand.equalsIgnoreCase(searchBrand)) {
                count++;
            }
        }
        
        System.out.println("\nNumber of " + searchBrand + " cars: " + count);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        s.close();
    }
}
```

**Sample Output:**
```
Enter number of cars: 
5
Enter brand: 
Toyota
Enter model: 
Camry
Enter year: 
2020
Enter price: 
25000
Enter brand: 
Honda
Enter model: 
Civic
Enter year: 
2021
Enter price: 
22000
Enter brand: 
Toyota
Enter model: 
Corolla
Enter year: 
2019
Enter price: 
20000
Enter brand: 
Ford
Enter model: 
Focus
Enter year: 
2022
Enter price: 
23000
Enter brand: 
Toyota
Enter model: 
RAV4
Enter year: 
2023
Enter price: 
28000
Enter brand to count: 
Toyota

Number of Toyota cars: 3

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 6: Detect Duplicate Product IDs**

```java
import java.util.Scanner;

class Product {
    int id;
    String name;
    double price;
}

public class Program6 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        
        System.out.println("Enter number of products: ");
        int p = scnr.nextInt();
        scnr.nextLine();
        
        Product[] products = new Product[p];
        
        for (int i = 0; i < p; i++) {
            products[i] = new Product();
            
            System.out.println("Enter product ID: ");
            products[i].id = scnr.nextInt();
            scnr.nextLine();
            
            System.out.println("Enter product name: ");
            products[i].name = scnr.nextLine();
            
            System.out.println("Enter price: ");
            products[i].price = scnr.nextDouble();
            scnr.nextLine();
        }
        
        System.out.println("\nDuplicate Product IDs found:");
        boolean found = false;
        
        for (int i = 0; i < p; i++) {
            for (int j = i + 1; j < p; j++) {
                if (products[i].id == products[j].id) {
                    System.out.println("ID: " + products[i].id + " - " + products[i].name + " and " + products[j].name);
                    found = true;
                }
            }
        }
        
        if (!found) {
            System.out.println("No duplicate IDs found");
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scnr.close();
    }
}
```

**Sample Output:**
```
Enter number of products: 
5
Enter product ID: 
101
Enter product name: 
Laptop
Enter price: 
50000
Enter product ID: 
102
Enter product name: 
Mouse
Enter price: 
500
Enter product ID: 
101
Enter product name: 
Keyboard
Enter price: 
1500
Enter product ID: 
104
Enter product name: 
Monitor
Enter price: 
8000
Enter product ID: 
102
Enter product name: 
Speaker
Enter price: 
2000

Duplicate Product IDs found:
ID: 101 - Laptop and Keyboard
ID: 102 - Mouse and Speaker

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 7: Rectangle with Maximum Area**

```java
import java.util.Scanner;

class Rectangle {
    double length;
    double width;
}

public class Program7 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter number of rectangles: ");
        int r = in.nextInt();
        
        Rectangle[] rects = new Rectangle[r];
        
        for (int i = 0; i < r; i++) {
            rects[i] = new Rectangle();
            
            System.out.println("Enter length for rectangle " + (i+1) + ": ");
            rects[i].length = in.nextDouble();
            
            System.out.println("Enter width for rectangle " + (i+1) + ": ");
            rects[i].width = in.nextDouble();
        }
        
        double maxArea = 0;
        int maxIndex = 0;
        
        for (int i = 0; i < r; i++) {
            double area = rects[i].length * rects[i].width;
            if (area > maxArea) {
                maxArea = area;
                maxIndex = i;
            }
        }
        
        System.out.println("\nRectangle with maximum area:");
        System.out.println("Length: " + rects[maxIndex].length);
        System.out.println("Width: " + rects[maxIndex].width);
        System.out.println("Area: " + maxArea);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        in.close();
    }
}
```

**Sample Output:**
```
Enter number of rectangles: 
4
Enter length for rectangle 1: 
10
Enter width for rectangle 1: 
5
Enter length for rectangle 2: 
8
Enter width for rectangle 2: 
6
Enter length for rectangle 3: 
12
Enter width for rectangle 3: 
7
Enter length for rectangle 4: 
9
Enter width for rectangle 4: 
9

Rectangle with maximum area:
Length: 12.0
Width: 7.0
Area: 84.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 8: Remove Student by Roll Number**

```java
import java.util.Scanner;

class Student8 {
    String name;
    int roll;
    double marks;
}

public class Program8 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int n = scan.nextInt();
        scan.nextLine();
        
        Student8[] students = new Student8[n];
        
        for (int i = 0; i < n; i++) {
            students[i] = new Student8();
            
            System.out.println("Enter name: ");
            students[i].name = scan.nextLine();
            
            System.out.println("Enter roll number: ");
            students[i].roll = scan.nextInt();
            
            System.out.println("Enter marks: ");
            students[i].marks = scan.nextDouble();
            scan.nextLine();
        }
        
        System.out.println("Enter roll number to remove: ");
        int removeRoll = scan.nextInt();
        
        Student8[] newStudents = new Student8[n-1];
        int newIndex = 0;
        
        for (int i = 0; i < n; i++) {
            if (students[i].roll != removeRoll) {
                newStudents[newIndex] = students[i];
                newIndex++;
            }
        }
        
        System.out.println("\nStudents after removal:");
        for (int i = 0; i < newIndex; i++) {
            System.out.println(newStudents[i].name + " - Roll: " + newStudents[i].roll + " - Marks: " + newStudents[i].marks);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
4
Enter name: 
Rahul
Enter roll number: 
101
Enter marks: 
85
Enter name: 
Priya
Enter roll number: 
102
Enter marks: 
90
Enter name: 
Amit
Enter roll number: 
103
Enter marks: 
78
Enter name: 
Sneha
Enter roll number: 
104
Enter marks: 
92
Enter roll number to remove: 
103

Students after removal:
Rahul - Roll: 101 - Marks: 85.0
Priya - Roll: 102 - Marks: 90.0
Sneha - Roll: 104 - Marks: 92.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 9: Movies with Rating > 8.5**

```java
import java.util.Scanner;

class Movie {
    String title;
    String director;
    double rating;
    int year;
}

public class Program9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of movies: ");
        int m = sc.nextInt();
        sc.nextLine();
        
        Movie[] movies = new Movie[m];
        
        for (int i = 0; i < m; i++) {
            movies[i] = new Movie();
            
            System.out.println("Enter movie title: ");
            movies[i].title = sc.nextLine();
            
            System.out.println("Enter director: ");
            movies[i].director = sc.nextLine();
            
            System.out.println("Enter rating: ");
            movies[i].rating = sc.nextDouble();
            
            System.out.println("Enter year: ");
            movies[i].year = sc.nextInt();
            sc.nextLine();
        }
        
        System.out.println("\nMovies with rating greater than 8.5:");
        for (int i = 0; i < m; i++) {
            if (movies[i].rating > 8.5) {
                System.out.println(movies[i].title + " (" + movies[i].year + ") - Rating: " + movies[i].rating + " - Director: " + movies[i].director);
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of movies: 
5
Enter movie title: 
Inception
Enter director: 
Christopher Nolan
Enter rating: 
8.8
Enter year: 
2010
Enter movie title: 
Avengers
Enter director: 
Joss Whedon
Enter rating: 
8.0
Enter year: 
2012
Enter movie title: 
Parasite
Enter director: 
Bong Joon-ho
Enter rating: 
8.6
Enter year: 
2019
Enter movie title: 
Titanic
Enter director: 
James Cameron
Enter rating: 
7.9
Enter year: 
1997
Enter movie title: 
The Dark Knight
Enter director: 
Christopher Nolan
Enter rating: 
9.0
Enter year: 
2008

Movies with rating greater than 8.5:
Inception (2010) - Rating: 8.8 - Director: Christopher Nolan
Parasite (2019) - Rating: 8.6 - Director: Bong Joon-ho
The Dark Knight (2008) - Rating: 9.0 - Director: Christopher Nolan

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 10: Laptop with Min Price and Max RAM**

```java
import java.util.Scanner;

class Laptop {
    String brand;
    String model;
    double price;
    int ram;
    int storage;
}

public class Program10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of laptops: ");
        int l = input.nextInt();
        input.nextLine();
        
        Laptop[] laptops = new Laptop[l];
        
        for (int i = 0; i < l; i++) {
            laptops[i] = new Laptop();
            
            System.out.println("Enter brand: ");
            laptops[i].brand = input.nextLine();
            
            System.out.println("Enter model: ");
            laptops[i].model = input.nextLine();
            
            System.out.println("Enter price: ");
            laptops[i].price = input.nextDouble();
            
            System.out.println("Enter RAM (GB): ");
            laptops[i].ram = input.nextInt();
            
            System.out.println("Enter storage (GB): ");
            laptops[i].storage = input.nextInt();
            input.nextLine();
        }
        
        double minPrice = laptops[0].price;
        int minPriceIndex = 0;
        
        int maxRam = laptops[0].ram;
        int maxRamIndex = 0;
        
        for (int i = 1; i < l; i++) {
            if (laptops[i].price < minPrice) {
                minPrice = laptops[i].price;
                minPriceIndex = i;
            }
            
            if (laptops[i].ram > maxRam) {
                maxRam = laptops[i].ram;
                maxRamIndex = i;
            }
        }
        
        System.out.println("\nLaptop with minimum price:");
        System.out.println(laptops[minPriceIndex].brand + " " + laptops[minPriceIndex].model + " - Price: " + laptops[minPriceIndex].price);        
        System.out.println("\nLaptop with maximum RAM:");
        System.out.println(laptops[maxRamIndex].brand + " " + laptops[maxRamIndex].model + " - RAM: " + laptops[maxRamIndex].ram + "GB");
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
Enter number of laptops: 
4
Enter brand: 
Dell
Enter model: 
Inspiron
Enter price: 
45000
Enter RAM (GB): 
8
Enter storage (GB): 
512
Enter brand: 
HP
Enter model: 
Pavilion
Enter price: 
52000
Enter RAM (GB): 
16
Enter storage (GB): 
1024
Enter brand: 
Lenovo
Enter model: 
ThinkPad
Enter price: 
38000
Enter RAM (GB): 
8
Enter storage (GB): 
256
Enter brand: 
Apple
Enter model: 
MacBook Pro
Enter price: 
120000
Enter RAM (GB): 
32
Enter storage (GB): 
1024

Laptop with minimum price:
Lenovo ThinkPad - Price: 38000.0

Laptop with maximum RAM:
Apple MacBook Pro - RAM: 32GB

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 11: Oldest and Youngest Person**

```java
import java.util.Scanner;

class Person {
    String name;
    int age;
}

public class Program11 {
    public static void main(String[] args) {
        Scanner abc = new Scanner(System.in);
        
        System.out.println("Enter number of persons: ");
        int n = abc.nextInt();
        abc.nextLine();
        
        Person[] persons = new Person[n];
        
        for (int i = 0; i < n; i++) {
            persons[i] = new Person();
            
            System.out.println("Enter name: ");
            persons[i].name = abc.nextLine();
            
            System.out.println("Enter age: ");
            persons[i].age = abc.nextInt();
            abc.nextLine();
        }
        
        Person oldest = persons[0];
        Person youngest = persons[0];
        
        for (int i = 1; i < n; i++) {
            if (persons[i].age > oldest.age) {
                oldest = persons[i];
            }
            if (persons[i].age < youngest.age) {
                youngest = persons[i];
            }
        }
        
        System.out.println("\nOldest person: " + oldest.name + " (" + oldest.age + " years)");
        System.out.println("Youngest person: " + youngest.name + " (" + youngest.age + " years)");
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        abc.close();
    }
}
```

**Sample Output:**
```
Enter number of persons: 
5
Enter name: 
Rahul
Enter age: 
25
Enter name: 
Priya
Enter age: 
32
Enter name: 
Amit
Enter age: 
19
Enter name: 
Sneha
Enter age: 
28
Enter name: 
Raj
Enter age: 
45

Oldest person: Raj (45 years)
Youngest person: Amit (19 years)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 12: Search Customer by Email**

```java
import java.util.Scanner;

class Customer {
    String name;
    String email;
    String phone;
}

public class Program12 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of customers: ");
        int n = input.nextInt();
        input.nextLine();
        
        Customer[] customers = new Customer[n];
        
        for (int i = 0; i < n; i++) {
            customers[i] = new Customer();
            
            System.out.println("Enter name: ");
            customers[i].name = input.nextLine();
            
            System.out.println("Enter email: ");
            customers[i].email = input.nextLine();
            
            System.out.println("Enter phone: ");
            customers[i].phone = input.nextLine();
        }
        
        System.out.println("Enter email to search: ");
        String searchEmail = input.nextLine();
        
        boolean found = false;
        for (int i = 0; i < n; i++) {
            if (customers[i].email.equalsIgnoreCase(searchEmail)) {
                System.out.println("\nCustomer found:");
                System.out.println("Name: " + customers[i].name);
                System.out.println("Email: " + customers[i].email);
                System.out.println("Phone: " + customers[i].phone);
                found = true;
                break;
            }
        }
        
        if (!found) {
            System.out.println("Customer with email " + searchEmail + " not found");
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
Enter number of customers: 
4
Enter name: 
Rahul Sharma
Enter email: 
rahul@gmail.com
Enter phone: 
9876543210
Enter name: 
Priya Patel
Enter email: 
priya@yahoo.com
Enter phone: 
9876543211
Enter name: 
Amit Kumar
Enter email: 
amit@hotmail.com
Enter phone: 
9876543212
Enter name: 
Sneha Singh
Enter email: 
sneha@gmail.com
Enter phone: 
9876543213
Enter email to search: 
amit@hotmail.com

Customer found:
Name: Amit Kumar
Email: amit@hotmail.com
Phone: 9876543212

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 13: Class Average, Highest and Lowest Marks**

```java
import java.util.Scanner;

class Student13 {
    String name;
    double marks;
}

public class Program13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        Student13[] students = new Student13[n];
        
        for (int i = 0; i < n; i++) {
            students[i] = new Student13();
            
            System.out.println("Enter name: ");
            students[i].name = sc.nextLine();
            
            System.out.println("Enter marks: ");
            students[i].marks = sc.nextDouble();
            sc.nextLine();
        }
        
        double highest = students[0].marks;
        double lowest = students[0].marks;
        double total = 0;
        
        for (int i = 0; i < n; i++) {
            if (students[i].marks > highest) {
                highest = students[i].marks;
            }
            if (students[i].marks < lowest) {
                lowest = students[i].marks;
            }
            total += students[i].marks;
        }
        
        double average = total / n;
        
        System.out.println("\nClass Statistics:");
        System.out.println("Average marks: " + average);
        System.out.println("Highest marks: " + highest);
        System.out.println("Lowest marks: " + lowest);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
5
Enter name: 
Rahul
Enter marks: 
85
Enter name: 
Priya
Enter marks: 
92
Enter name: 
Amit
Enter marks: 
78
Enter name: 
Sneha
Enter marks: 
88
Enter name: 
Raj
Enter marks: 
65

Class Statistics:
Average marks: 81.6
Highest marks: 92.0
Lowest marks: 65.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 14: Trains Between Source and Destination**

```java
import java.util.Scanner;

class Train {
    String trainName;
    String source;
    String destination;
    int trainNumber;
}

public class Program14 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of trains: ");
        int n = scan.nextInt();
        scan.nextLine();
        
        Train[] trains = new Train[n];
        
        for (int i = 0; i < n; i++) {
            trains[i] = new Train();
            
            System.out.println("Enter train name: ");
            trains[i].trainName = scan.nextLine();
            
            System.out.println("Enter source: ");
            trains[i].source = scan.nextLine();
            
            System.out.println("Enter destination: ");
            trains[i].destination = scan.nextLine();
            
            System.out.println("Enter train number: ");
            trains[i].trainNumber = scan.nextInt();
            scan.nextLine();
        }
        
        System.out.println("Enter source to search: ");
        String searchSource = scan.nextLine();
        
        System.out.println("Enter destination to search: ");
        String searchDest = scan.nextLine();
        
        System.out.println("\nTrains from " + searchSource + " to " + searchDest + ":");
        boolean found = false;
        
        for (int i = 0; i < n; i++) {
            if (trains[i].source.equalsIgnoreCase(searchSource) && 
                trains[i].destination.equalsIgnoreCase(searchDest)) {
                System.out.println(trains[i].trainName + " (Train No: " + trains[i].trainNumber + ")");
                found = true;
            }
        }
        
        if (!found) {
            System.out.println("No trains found for this route");
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of trains: 
5
Enter train name: 
Rajdhani Express
Enter source: 
Delhi
Enter destination: 
Mumbai
Enter train number: 
12951
Enter train name: 
Shatabdi Express
Enter source: 
Delhi
Enter destination: 
Chennai
Enter train number: 
12001
Enter train name: 
Duronto Express
Enter source: 
Kolkata
Enter destination: 
Delhi
Enter train number: 
12259
Enter train name: 
Garib Rath
Enter source: 
Delhi
Enter destination: 
Mumbai
Enter train number: 
12213
Enter train name: 
Tejas Express
Enter source: 
Mumbai
Enter destination: 
Goa
Enter train number: 
22119
Enter source to search: 
Delhi
Enter destination to search: 
Mumbai

Trains from Delhi to Mumbai:
Rajdhani Express (Train No: 12951)
Garib Rath (Train No: 12213)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 15: Mobiles in Different Price Ranges**

```java
import java.util.Scanner;

class Mobile {
    String brand;
    String model;
    double price;
}

public class Program15 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.println("Enter number of mobiles: ");
        int n = s.nextInt();
        s.nextLine();
        
        Mobile[] mobiles = new Mobile[n];
        
        for (int i = 0; i < n; i++) {
            mobiles[i] = new Mobile();
            
            System.out.println("Enter brand: ");
            mobiles[i].brand = s.nextLine();
            
            System.out.println("Enter model: ");
            mobiles[i].model = s.nextLine();
            
            System.out.println("Enter price: ");
            mobiles[i].price = s.nextDouble();
            s.nextLine();
        }
        
        int range1 = 0; // < 10000
        int range2 = 0; // 10000 - 30000
        int range3 = 0; // > 30000
        
        for (int i = 0; i < n; i++) {
            if (mobiles[i].price < 10000) {
                range1++;
            } else if (mobiles[i].price >= 10000 && mobiles[i].price <= 30000) {
                range2++;
            } else {
                range3++;
            }
        }
        
        System.out.println("\nMobile count by price range:");
        System.out.println("Below ₹10,000: " + range1);
        System.out.println("₹10,000 - ₹30,000: " + range2);
        System.out.println("Above ₹30,000: " + range3);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        s.close();
    }
}
```

**Sample Output:**
```
Enter number of mobiles: 
6
Enter brand: 
Samsung
Enter model: 
Galaxy A14
Enter price: 
14999
Enter brand: 
Apple
Enter model: 
iPhone 14
Enter price: 
79999
Enter brand: 
Xiaomi
Enter model: 
Redmi Note 12
Enter price: 
17999
Enter brand: 
Nokia
Enter model: 
C12
Enter price: 
7999
Enter brand: 
OnePlus
Enter model: 
Nord CE 3
Enter price: 
24999
Enter brand: 
Google
Enter model: 
Pixel 7
Enter price: 
59999

Mobile count by price range:
Below ₹10,000: 1
₹10,000 - ₹30,000: 3
Above ₹30,000: 2

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 16: Top Scorer and Average Score**

```java
import java.util.Scanner;

class Player {
    String name;
    int score;
}

public class Program16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of players: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        Player[] players = new Player[n];
        
        for (int i = 0; i < n; i++) {
            players[i] = new Player();
            
            System.out.println("Enter player name: ");
            players[i].name = sc.nextLine();
            
            System.out.println("Enter score: ");
            players[i].score = sc.nextInt();
            sc.nextLine();
        }
        
        Player topScorer = players[0];
        int total = players[0].score;
        
        for (int i = 1; i < n; i++) {
            if (players[i].score > topScorer.score) {
                topScorer = players[i];
            }
            total += players[i].score;
        }
        
        double average = (double) total / n;
        
        System.out.println("\nTop Scorer: " + topScorer.name + " (" + topScorer.score + " runs)");
        System.out.println("Average Score: " + average);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of players: 
5
Enter player name: 
Virat
Enter score: 
85
Enter player name: 
Rohit
Enter score: 
92
Enter player name: 
Surya
Enter score: 
78
Enter player name: 
Hardik
Enter score: 
65
Enter player name: 
Rishabh
Enter score: 
88

Top Scorer: Rohit (92 runs)
Average Score: 81.6

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 17: Separate Two-Wheelers and Four-Wheelers**

```java
import java.util.Scanner;

class Vehicle {
    String type;
    String brand;
    String model;
}

public class Program17 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of vehicles: ");
        int n = input.nextInt();
        input.nextLine();
        
        Vehicle[] vehicles = new Vehicle[n];
        
        for (int i = 0; i < n; i++) {
            vehicles[i] = new Vehicle();
            
            System.out.println("Enter type (2-wheeler/4-wheeler): ");
            vehicles[i].type = input.nextLine();
            
            System.out.println("Enter brand: ");
            vehicles[i].brand = input.nextLine();
            
            System.out.println("Enter model: ");
            vehicles[i].model = input.nextLine();
        }
        
        System.out.println("\nTwo-Wheelers:");
        for (int i = 0; i < n; i++) {
            if (vehicles[i].type.equalsIgnoreCase("2-wheeler")) {
                System.out.println(vehicles[i].brand + " " + vehicles[i].model);
            }
        }
        
        System.out.println("\nFour-Wheelers:");
        for (int i = 0; i < n; i++) {
            if (vehicles[i].type.equalsIgnoreCase("4-wheeler")) {
                System.out.println(vehicles[i].brand + " " + vehicles[i].model);
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
Enter number of vehicles: 
6
Enter type (2-wheeler/4-wheeler): 
2-wheeler
Enter brand: 
Hero
Enter model: 
Splendor
Enter type (2-wheeler/4-wheeler): 
4-wheeler
Enter brand: 
Maruti
Enter model: 
Swift
Enter type (2-wheeler/4-wheeler): 
2-wheeler
Enter brand: 
Honda
Enter model: 
Activa
Enter type (2-wheeler/4-wheeler): 
4-wheeler
Enter brand: 
Hyundai
Enter model: 
Creta
Enter type (2-wheeler/4-wheeler): 
2-wheeler
Enter brand: 
Bajaj
Enter model: 
Pulsar
Enter type (2-wheeler/4-wheeler): 
4-wheeler
Enter brand: 
Tata
Enter model: 
Nexon

Two-Wheelers:
Hero Splendor
Honda Activa
Bajaj Pulsar

Four-Wheelers:
Maruti Swift
Hyundai Creta
Tata Nexon

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 18: Apply Discount to Products Above Price**

```java
import java.util.Scanner;

class Product18 {
    String name;
    double price;
    int id;
}

public class Program18 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        
        System.out.println("Enter number of products: ");
        int n = scnr.nextInt();
        scnr.nextLine();
        
        Product18[] products = new Product18[n];
        
        for (int i = 0; i < n; i++) {
            products[i] = new Product18();
            
            System.out.println("Enter product name: ");
            products[i].name = scnr.nextLine();
            
            System.out.println("Enter price: ");
            products[i].price = scnr.nextDouble();
            
            System.out.println("Enter ID: ");
            products[i].id = scnr.nextInt();
            scnr.nextLine();
        }
        
        System.out.println("Enter price threshold for discount: ");
        double threshold = scnr.nextDouble();
        
        System.out.println("Enter discount percentage: ");
        double discount = scnr.nextDouble();
        
        System.out.println("\nProducts after discount:");
        for (int i = 0; i < n; i++) {
            if (products[i].price > threshold) {
                double discountedPrice = products[i].price * (1 - discount/100);
                System.out.println(products[i].name + ": Original ₹" + products[i].price + 
                                 ", Discounted ₹" + discountedPrice);
            } else {
                System.out.println(products[i].name + ": ₹" + products[i].price + " (No discount)");
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scnr.close();
    }
}
```

**Sample Output:**
```
Enter number of products: 
4
Enter product name: 
Laptop
Enter price: 
50000
Enter ID: 
101
Enter product name: 
Mouse
Enter price: 
500
Enter ID: 
102
Enter product name: 
Keyboard
Enter price: 
1500
Enter ID: 
103
Enter product name: 
Monitor
Enter price: 
8000
Enter ID: 
104
Enter price threshold for discount: 
1000
Enter discount percentage: 
10

Products after discount:
Laptop: Original ₹50000.0, Discounted ₹45000.0
Mouse: ₹500.0 (No discount)
Keyboard: Original ₹1500.0, Discounted ₹1350.0
Monitor: Original ₹8000.0, Discounted ₹7200.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 19: Rank Students Based on Total Marks**

```java
import java.util.Scanner;

class Student19 {
    String name;
    int roll;
    double marks;
}

public class Program19 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int n = in.nextInt();
        in.nextLine();
        
        Student19[] students = new Student19[n];
        
        for (int i = 0; i < n; i++) {
            students[i] = new Student19();
            
            System.out.println("Enter name: ");
            students[i].name = in.nextLine();
            
            System.out.println("Enter roll number: ");
            students[i].roll = in.nextInt();
            
            System.out.println("Enter total marks: ");
            students[i].marks = in.nextDouble();
            in.nextLine();
        }
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (students[j].marks < students[j + 1].marks) {
                    Student19 temp = students[j];
                    students[j] = students[j + 1];
                    students[j + 1] = temp;
                }
            }
        }
        
        System.out.println("\nStudent Rankings:");
        for (int i = 0; i < n; i++) {
            System.out.println("Rank " + (i+1) + ": " + students[i].name + 
                             " (Roll: " + students[i].roll + ", Marks: " + students[i].marks + ")");
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        in.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
5
Enter name: 
Rahul
Enter roll number: 
101
Enter total marks: 
85
Enter name: 
Priya
Enter roll number: 
102
Enter total marks: 
92
Enter name: 
Amit
Enter roll number: 
103
Enter total marks: 
78
Enter name: 
Sneha
Enter roll number: 
104
Enter total marks: 
88
Enter name: 
Raj
Enter roll number: 
105
Enter total marks: 
65

Student Rankings:
Rank 1: Priya (Roll: 102, Marks: 92.0)
Rank 2: Sneha (Roll: 104, Marks: 88.0)
Rank 3: Rahul (Roll: 101, Marks: 85.0)
Rank 4: Amit (Roll: 103, Marks: 78.0)
Rank 5: Raj (Roll: 105, Marks: 65.0)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 20: Department-wise Highest Paid Employee**

```java
import java.util.Scanner;

class Employee20 {
    String name;
    String department;
    double salary;
}

public class Program20 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of employees: ");
        int n = scan.nextInt();
        scan.nextLine();
        
        Employee20[] employees = new Employee20[n];
        
        for (int i = 0; i < n; i++) {
            employees[i] = new Employee20();
            
            System.out.println("Enter name: ");
            employees[i].name = scan.nextLine();
            
            System.out.println("Enter department: ");
            employees[i].department = scan.nextLine();
            
            System.out.println("Enter salary: ");
            employees[i].salary = scan.nextDouble();
            scan.nextLine();
        }
        
        System.out.println("\nDepartment-wise highest paid employees:");
        
        for (int i = 0; i < n; i++) {
            boolean isHighest = true;
            for (int j = 0; j < n; j++) {
                if (employees[i].department.equals(employees[j].department) && 
                    employees[i].salary < employees[j].salary) {
                    isHighest = false;
                    break;
                }
            }
            
            if (isHighest) {
                boolean alreadyPrinted = false;
                for (int k = 0; k < i; k++) {
                    if (employees[i].department.equals(employees[k].department) && 
                        employees[i].name.equals(employees[k].name)) {
                        alreadyPrinted = true;
                        break;
                    }
                }
                
                if (!alreadyPrinted) {
                    System.out.println(employees[i].department + ": " + 
                                     employees[i].name + " (₹" + employees[i].salary + ")");
                }
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of employees: 
6
Enter name: 
Rahul
Enter department: 
IT
Enter salary: 
50000
Enter name: 
Priya
Enter department: 
HR
Enter salary: 
45000
Enter name: 
Amit
Enter department: 
IT
Enter salary: 
55000
Enter name: 
Sneha
Enter department: 
Finance
Enter salary: 
60000
Enter name: 
Raj
Enter department: 
HR
Enter salary: 
42000
Enter name: 
Meera
Enter department: 
Finance
Enter salary: 
58000

Department-wise highest paid employees:
IT: Amit (₹55000.0)
HR: Priya (₹45000.0)
Finance: Sneha (₹60000.0)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 21: Merge Two Book Arrays Without Duplicates**

```java
import java.util.Scanner;

class Book21 {
    int id;
    String title;
    String author;
}

public class Program21 {
    public static void main(String[] args) {
        Scanner abc = new Scanner(System.in);
        
        System.out.println("Enter number of books in first array: ");
        int n1 = abc.nextInt();
        abc.nextLine();
        
        Book21[] books1 = new Book21[n1];
        
        for (int i = 0; i < n1; i++) {
            books1[i] = new Book21();
            
            System.out.println("Enter book ID: ");
            books1[i].id = abc.nextInt();
            abc.nextLine();
            
            System.out.println("Enter title: ");
            books1[i].title = abc.nextLine();
            
            System.out.println("Enter author: ");
            books1[i].author = abc.nextLine();
        }
        
        System.out.println("Enter number of books in second array: ");
        int n2 = abc.nextInt();
        abc.nextLine();
        
        Book21[] books2 = new Book21[n2];
        
        for (int i = 0; i < n2; i++) {
            books2[i] = new Book21();
            
            System.out.println("Enter book ID: ");
            books2[i].id = abc.nextInt();
            abc.nextLine();
            
            System.out.println("Enter title: ");
            books2[i].title = abc.nextLine();
            
            System.out.println("Enter author: ");
            books2[i].author = abc.nextLine();
        }
        
        Book21[] merged = new Book21[n1 + n2];
        int mergedCount = 0;
        
        for (int i = 0; i < n1; i++) {
            boolean duplicate = false;
            for (int j = 0; j < mergedCount; j++) {
                if (books1[i].id == merged[j].id) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) {
                merged[mergedCount] = books1[i];
                mergedCount++;
            }
        }
        
        for (int i = 0; i < n2; i++) {
            boolean duplicate = false;
            for (int j = 0; j < mergedCount; j++) {
                if (books2[i].id == merged[j].id) {
                    duplicate = true;
                    break;
                }
            }
            if (!duplicate) {
                merged[mergedCount] = books2[i];
                mergedCount++;
            }
        }
        
        System.out.println("\nMerged books without duplicates:");
        for (int i = 0; i < mergedCount; i++) {
            System.out.println("ID: " + merged[i].id + ", Title: " + merged[i].title + ", Author: " + merged[i].author);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        abc.close();
    }
}
```

**Sample Output:**
```
Enter number of books in first array: 
3
Enter book ID: 
101
Enter title: 
Java Programming
Enter author: 
John Doe
Enter book ID: 
102
Enter title: 
Python Basics
Enter author: 
Jane Smith
Enter book ID: 
103
Enter title: 
C++ Guide
Enter author: 
Mike Johnson
Enter number of books in second array: 
3
Enter book ID: 
102
Enter title: 
Python Basics
Enter author: 
Jane Smith
Enter book ID: 
104
Enter title: 
Web Development
Enter author: 
Sarah Lee
Enter book ID: 
105
Enter title: 
Database Systems
Enter author: 
Robert Brown

Merged books without duplicates:
ID: 101, Title: Java Programming, Author: John Doe
ID: 102, Title: Python Basics, Author: Jane Smith
ID: 103, Title: C++ Guide, Author: Mike Johnson
ID: 104, Title: Web Development, Author: Sarah Lee
ID: 105, Title: Database Systems, Author: Robert Brown

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 22: Remove Zero-Balance Bank Accounts**

```java
import java.util.Scanner;

class BankAccount22 {
    String accNumber;
    String accHolder;
    double balance;
}

public class Program22 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of accounts: ");
        int n = input.nextInt();
        input.nextLine();
        
        BankAccount22[] accounts = new BankAccount22[n];
        
        for (int i = 0; i < n; i++) {
            accounts[i] = new BankAccount22();
            
            System.out.println("Enter account number: ");
            accounts[i].accNumber = input.nextLine();
            
            System.out.println("Enter account holder name: ");
            accounts[i].accHolder = input.nextLine();
            
            System.out.println("Enter balance: ");
            accounts[i].balance = input.nextDouble();
            input.nextLine();
        }
        
        int nonZeroCount = 0;
        for (int i = 0; i < n; i++) {
            if (accounts[i].balance > 0) {
                nonZeroCount++;
            }
        }
        
        BankAccount22[] filteredAccounts = new BankAccount22[nonZeroCount];
        int index = 0;
        
        for (int i = 0; i < n; i++) {
            if (accounts[i].balance > 0) {
                filteredAccounts[index] = accounts[i];
                index++;
            }
        }
        
        System.out.println("\nAccounts after removing zero-balance accounts:");
        for (int i = 0; i < nonZeroCount; i++) {
            System.out.println(filteredAccounts[i].accHolder + " - " + 
                             filteredAccounts[i].accNumber + " - Balance: " + 
                             filteredAccounts[i].balance);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
Enter number of accounts: 
5
Enter account number: 
SB1001
Enter account holder name: 
Rahul Sharma
Enter balance: 
5000
Enter account number: 
SB1002
Enter account holder name: 
Priya Patel
Enter balance: 
0
Enter account number: 
SB1003
Enter account holder name: 
Amit Kumar
Enter balance: 
10000
Enter account number: 
SB1004
Enter account holder name: 
Sneha Singh
Enter balance: 
0
Enter account number: 
SB1005
Enter account holder name: 
Raj Verma
Enter balance: 
7500

Accounts after removing zero-balance accounts:
Rahul Sharma - SB1001 - Balance: 5000.0
Amit Kumar - SB1003 - Balance: 10000.0
Raj Verma - SB1005 - Balance: 7500.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 23: Highest-Rated Hotel City-Wise**

```java
import java.util.Scanner;

class Hotel {
    String name;
    String city;
    double rating;
    double price;
}

public class Program23 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of hotels: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        Hotel[] hotels = new Hotel[n];
        
        for (int i = 0; i < n; i++) {
            hotels[i] = new Hotel();
            
            System.out.println("Enter hotel name: ");
            hotels[i].name = sc.nextLine();
            
            System.out.println("Enter city: ");
            hotels[i].city = sc.nextLine();
            
            System.out.println("Enter rating: ");
            hotels[i].rating = sc.nextDouble();
            
            System.out.println("Enter price per night: ");
            hotels[i].price = sc.nextDouble();
            sc.nextLine();
        }
        
        System.out.println("\nHighest rated hotel in each city:");
        
        for (int i = 0; i < n; i++) {
            boolean isHighest = true;
            for (int j = 0; j < n; j++) {
                if (hotels[i].city.equals(hotels[j].city) && 
                    hotels[i].rating < hotels[j].rating) {
                    isHighest = false;
                    break;
                }
            }
            
            if (isHighest) {
                boolean alreadyPrinted = false;
                for (int k = 0; k < i; k++) {
                    if (hotels[i].city.equals(hotels[k].city) && 
                        hotels[i].name.equals(hotels[k].name)) {
                        alreadyPrinted = true;
                        break;
                    }
                }
                
                if (!alreadyPrinted) {
                    System.out.println(hotels[i].city + ": " + 
                                     hotels[i].name + " (Rating: " + 
                                     hotels[i].rating + ", Price: " + 
                                     hotels[i].price + ")");
                }
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of hotels: 
6
Enter hotel name: 
Taj Palace
Enter city: 
Delhi
Enter rating: 
4.8
Enter price per night: 
12000
Enter hotel name: 
Oberoi
Enter city: 
Mumbai
Enter rating: 
4.9
Enter price per night: 
15000
Enter hotel name: 
Leela Palace
Enter city: 
Delhi
Enter rating: 
4.7
Enter price per night: 
11000
Enter hotel name: 
ITC Maratha
Enter city: 
Mumbai
Enter rating: 
4.6
Enter price per night: 
10000
Enter hotel name: 
Hyatt
Enter city: 
Bangalore
Enter rating: 
4.5
Enter price per night: 
8000
Enter hotel name: 
Radisson
Enter city: 
Bangalore
Enter rating: 
4.4
Enter price per night: 
7000

Highest rated hotel in each city:
Delhi: Taj Palace (Rating: 4.8, Price: 12000.0)
Mumbai: Oberoi (Rating: 4.9, Price: 15000.0)
Bangalore: Hyatt (Rating: 4.5, Price: 8000.0)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 24: Separate Pass and Fail Students**

```java
import java.util.Scanner;

class Student24 {
    String name;
    int roll;
    double marks;
}

public class Program24 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int n = scan.nextInt();
        scan.nextLine();
        
        Student24[] students = new Student24[n];
        
        for (int i = 0; i < n; i++) {
            students[i] = new Student24();
            
            System.out.println("Enter name: ");
            students[i].name = scan.nextLine();
            
            System.out.println("Enter roll number: ");
            students[i].roll = scan.nextInt();
            
            System.out.println("Enter marks: ");
            students[i].marks = scan.nextDouble();
            scan.nextLine();
        }
        
        System.out.println("Enter passing marks: ");
        double passingMarks = scan.nextDouble();
        
        System.out.println("\nPass Students:");
        for (int i = 0; i < n; i++) {
            if (students[i].marks >= passingMarks) {
                System.out.println(students[i].name + " (Roll: " + 
                                 students[i].roll + ", Marks: " + 
                                 students[i].marks + ")");
            }
        }
        
        System.out.println("\nFail Students:");
        for (int i = 0; i < n; i++) {
            if (students[i].marks < passingMarks) {
                System.out.println(students[i].name + " (Roll: " + 
                                 students[i].roll + ", Marks: " + 
                                 students[i].marks + ")");
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
5
Enter name: 
Rahul
Enter roll number: 
101
Enter marks: 
85
Enter name: 
Priya
Enter roll number: 
102
Enter marks: 
45
Enter name: 
Amit
Enter roll number: 
103
Enter marks: 
78
Enter name: 
Sneha
Enter roll number: 
104
Enter marks: 
32
Enter name: 
Raj
Enter roll number: 
105
Enter marks: 
90
Enter passing marks: 
40

Pass Students:
Rahul (Roll: 101, Marks: 85.0)
Priya (Roll: 102, Marks: 45.0)
Amit (Roll: 103, Marks: 78.0)
Raj (Roll: 105, Marks: 90.0)

Fail Students:
Sneha (Roll: 104, Marks: 32.0)

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 25: Most Expensive Item Using Object Comparison**

```java
import java.util.Scanner;

class Item {
    String name;
    double price;
    int id;
}

public class Program25 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.println("Enter number of items: ");
        int n = s.nextInt();
        s.nextLine();
        
        Item[] items = new Item[n];
        
        for (int i = 0; i < n; i++) {
            items[i] = new Item();
            
            System.out.println("Enter item name: ");
            items[i].name = s.nextLine();
            
            System.out.println("Enter price: ");
            items[i].price = s.nextDouble();
            
            System.out.println("Enter item ID: ");
            items[i].id = s.nextInt();
            s.nextLine();
        }
        
        Item mostExpensive = items[0];
        
        for (int i = 1; i < n; i++) {
            if (items[i].price > mostExpensive.price) {
                mostExpensive = items[i];
            }
        }
        
        System.out.println("\nMost Expensive Item:");
        System.out.println("Name: " + mostExpensive.name);
        System.out.println("Price: " + mostExpensive.price);
        System.out.println("ID: " + mostExpensive.id);
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        s.close();
    }
}
```

**Sample Output:**
```
Enter number of items: 
4
Enter item name: 
Laptop
Enter price: 
50000
Enter item ID: 
101
Enter item name: 
Smartphone
Enter price: 
25000
Enter item ID: 
102
Enter item name: 
Tablet
Enter price: 
15000
Enter item ID: 
103
Enter item name: 
Smart Watch
Enter price: 
8000
Enter item ID: 
104

Most Expensive Item:
Name: Laptop
Price: 50000.0
ID: 101

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 26: Update Salary Based on Experience**

```java
import java.util.Scanner;

class Employee26 {
    String name;
    int id;
    double salary;
    int experience;
}

public class Program26 {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        
        System.out.println("Enter number of employees: ");
        int n = scnr.nextInt();
        scnr.nextLine();
        
        Employee26[] employees = new Employee26[n];
        
        for (int i = 0; i < n; i++) {
            employees[i] = new Employee26();
            
            System.out.println("Enter name: ");
            employees[i].name = scnr.nextLine();
            
            System.out.println("Enter ID: ");
            employees[i].id = scnr.nextInt();
            
            System.out.println("Enter current salary: ");
            employees[i].salary = scnr.nextDouble();
            
            System.out.println("Enter years of experience: ");
            employees[i].experience = scnr.nextInt();
            scnr.nextLine();
        }
        
        System.out.println("\nUpdated Salaries:");
        for (int i = 0; i < n; i++) {
            double newSalary = employees[i].salary;
            
            if (employees[i].experience >= 10) {
                newSalary = employees[i].salary * 1.20;
            } else if (employees[i].experience >= 5) {
                newSalary = employees[i].salary * 1.15;
            } else if (employees[i].experience >= 2) {
                newSalary = employees[i].salary * 1.10;
            }
            
            System.out.println(employees[i].name + ": Old Salary = " + 
                             employees[i].salary + ", New Salary = " + newSalary);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scnr.close();
    }
}
```

**Sample Output:**
```
Enter number of employees: 
4
Enter name: 
Rahul
Enter ID: 
101
Enter current salary: 
40000
Enter years of experience: 
12
Enter name: 
Priya
Enter ID: 
102
Enter current salary: 
35000
Enter years of experience: 
7
Enter name: 
Amit
Enter ID: 
103
Enter current salary: 
30000
Enter years of experience: 
3
Enter name: 
Sneha
Enter ID: 
104
Enter current salary: 
28000
Enter years of experience: 
1

Updated Salaries:
Rahul: Old Salary = 40000.0, New Salary = 48000.0
Priya: Old Salary = 35000.0, New Salary = 40250.0
Amit: Old Salary = 30000.0, New Salary = 33000.0
Sneha: Old Salary = 28000.0, New Salary = 28000.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 27: Library Management System**

```java
import java.util.Scanner;

class Book27 {
    int id;
    String title;
    String author;
    boolean available;
}

public class Program27 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter number of books: ");
        int n = in.nextInt();
        in.nextLine();
        
        Book27[] library = new Book27[n];
        
        for (int i = 0; i < n; i++) {
            library[i] = new Book27();
            
            System.out.println("Enter book ID: ");
            library[i].id = in.nextInt();
            in.nextLine();
            
            System.out.println("Enter title: ");
            library[i].title = in.nextLine();
            
            System.out.println("Enter author: ");
            library[i].author = in.nextLine();
            
            library[i].available = true;
        }
        
        while (true) {
            System.out.println("\n1. Search Book");
            System.out.println("2. Issue Book");
            System.out.println("3. Return Book");
            System.out.println("4. Exit");
            System.out.println("Enter choice: ");
            int choice = in.nextInt();
            in.nextLine();
            
            if (choice == 1) {
                System.out.println("Enter book title to search: ");
                String searchTitle = in.nextLine();
                
                boolean found = false;
                for (int i = 0; i < n; i++) {
                    if (library[i].title.equalsIgnoreCase(searchTitle)) {
                        System.out.println("Book found:");
                        System.out.println("ID: " + library[i].id);
                        System.out.println("Title: " + library[i].title);
                        System.out.println("Author: " + library[i].author);
                        System.out.println("Available: " + library[i].available);
                        found = true;
                    }
                }
                if (!found) {
                    System.out.println("Book not found");
                }
            }
            else if (choice == 2) {
                System.out.println("Enter book ID to issue: ");
                int issueId = in.nextInt();
                
                boolean issued = false;
                for (int i = 0; i < n; i++) {
                    if (library[i].id == issueId) {
                        if (library[i].available) {
                            library[i].available = false;
                            System.out.println("Book issued successfully");
                            issued = true;
                        } else {
                            System.out.println("Book is already issued");
                        }
                    }
                }
                if (!issued) {
                    System.out.println("Book not found");
                }
            }
            else if (choice == 3) {
                System.out.println("Enter book ID to return: ");
                int returnId = in.nextInt();
                
                boolean returned = false;
                for (int i = 0; i < n; i++) {
                    if (library[i].id == returnId) {
                        if (!library[i].available) {
                            library[i].available = true;
                            System.out.println("Book returned successfully");
                            returned = true;
                        } else {
                            System.out.println("Book was not issued");
                        }
                    }
                }
                if (!returned) {
                    System.out.println("Book not found");
                }
            }
            else if (choice == 4) {
                break;
            }
            else {
                System.out.println("Invalid choice");
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        in.close();
    }
}
```

**Sample Output:**
```
Enter number of books: 
3
Enter book ID: 
101
Enter title: 
Java Programming
Enter author: 
John Doe
Enter book ID: 
102
Enter title: 
Python Basics
Enter author: 
Jane Smith
Enter book ID: 
103
Enter title: 
C++ Guide
Enter author: 
Mike Johnson

1. Search Book
2. Issue Book
3. Return Book
4. Exit
Enter choice: 
1
Enter book title to search: 
Java Programming
Book found:
ID: 101
Title: Java Programming
Author: John Doe
Available: true

5. Search Book
6. Issue Book
7. Return Book
8. Exit
Enter choice: 
2
Enter book ID to issue: 
101
Book issued successfully

9. Search Book
10. Issue Book
11. Return Book
12. Exit
Enter choice: 
2
Enter book ID to issue: 
101
Book is already issued

5. Search Book
6. Issue Book
7. Return Book
8. Exit
Enter choice: 
3
Enter book ID to return: 
101
Book returned successfully

9. Search Book
10. Issue Book
11. Return Book
12. Exit
Enter choice: 
4

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 28: Assign Grades Based on Marks**

```java
import java.util.Scanner;

class Student28 {
    String name;
    int roll;
    double marks;
    char grade;
}

public class Program28 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter number of students: ");
        int n = input.nextInt();
        input.nextLine();
        
        Student28[] students = new Student28[n];
        
        for (int i = 0; i < n; i++) {
            students[i] = new Student28();
            
            System.out.println("Enter name: ");
            students[i].name = input.nextLine();
            
            System.out.println("Enter roll number: ");
            students[i].roll = input.nextInt();
            
            System.out.println("Enter marks: ");
            students[i].marks = input.nextDouble();
            input.nextLine();
            
            if (students[i].marks >= 90) {
                students[i].grade = 'A';
            } else if (students[i].marks >= 75) {
                students[i].grade = 'B';
            } else if (students[i].marks >= 50) {
                students[i].grade = 'C';
            } else {
                students[i].grade = 'F';
            }
        }
        
        System.out.println("\nStudent Grades:");
        for (int i = 0; i < n; i++) {
            System.out.println(students[i].name + " (Roll: " + students[i].roll + 
                             ") - Marks: " + students[i].marks + " - Grade: " + 
                             students[i].grade);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        input.close();
    }
}
```

**Sample Output:**
```
Enter number of students: 
5
Enter name: 
Rahul
Enter roll number: 
101
Enter marks: 
92
Enter name: 
Priya
Enter roll number: 
102
Enter marks: 
78
Enter name: 
Amit
Enter roll number: 
103
Enter marks: 
65
Enter name: 
Sneha
Enter roll number: 
104
Enter marks: 
45
Enter name: 
Raj
Enter roll number: 
105
Enter marks: 
85

Student Grades:
Rahul (Roll: 101) - Marks: 92.0 - Grade: A
Priya (Roll: 102) - Marks: 78.0 - Grade: B
Amit (Roll: 103) - Marks: 65.0 - Grade: C
Sneha (Roll: 104) - Marks: 45.0 - Grade: F
Raj (Roll: 105) - Marks: 85.0 - Grade: B

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 29: Employees with Same Salary but Different Roles**

```java
import java.util.Scanner;

class Employee29 {
    String name;
    String role;
    double salary;
}

public class Program29 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter number of employees: ");
        int n = scan.nextInt();
        scan.nextLine();
        
        Employee29[] employees = new Employee29[n];
        
        for (int i = 0; i < n; i++) {
            employees[i] = new Employee29();
            
            System.out.println("Enter name: ");
            employees[i].name = scan.nextLine();
            
            System.out.println("Enter role: ");
            employees[i].role = scan.nextLine();
            
            System.out.println("Enter salary: ");
            employees[i].salary = scan.nextDouble();
            scan.nextLine();
        }
        
        System.out.println("\nEmployees with same salary but different roles:");
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (employees[i].salary == employees[j].salary && 
                    !employees[i].role.equals(employees[j].role)) {
                    System.out.println(employees[i].name + " (" + employees[i].role + 
                                     ") and " + employees[j].name + " (" + 
                                     employees[j].role + ") - Salary: " + 
                                     employees[i].salary);
                }
            }
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        scan.close();
    }
}
```

**Sample Output:**
```
Enter number of employees: 
5
Enter name: 
Rahul
Enter role: 
Developer
Enter salary: 
50000
Enter name: 
Priya
Enter role: 
Manager
Enter salary: 
70000
Enter name: 
Amit
Enter role: 
Tester
Enter salary: 
50000
Enter name: 
Sneha
Enter role: 
Analyst
Enter salary: 
60000
Enter name: 
Raj
Enter role: 
Designer
Enter salary: 
50000

Employees with same salary but different roles:
Rahul (Developer) and Amit (Tester) - Salary: 50000.0
Rahul (Developer) and Raj (Designer) - Salary: 50000.0
Amit (Tester) and Raj (Designer) - Salary: 50000.0

Name : Suryansh Mithu
Roll : 24155060
```

## **Program 30: Sort Hotels by Rating and Price**

```java
import java.util.Scanner;

class Hotel30 {
    String name;
    double rating;
    double price;
}

public class Program30 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of hotels: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        Hotel30[] hotels = new Hotel30[n];
        
        for (int i = 0; i < n; i++) {
            hotels[i] = new Hotel30();
            
            System.out.println("Enter hotel name: ");
            hotels[i].name = sc.nextLine();
            
            System.out.println("Enter rating: ");
            hotels[i].rating = sc.nextDouble();
            
            System.out.println("Enter price: ");
            hotels[i].price = sc.nextDouble();
            sc.nextLine();
        }
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (hotels[j].rating < hotels[j + 1].rating || 
                    (hotels[j].rating == hotels[j + 1].rating && 
                     hotels[j].price > hotels[j + 1].price)) {
                    Hotel30 temp = hotels[j];
                    hotels[j] = hotels[j + 1];
                    hotels[j + 1] = temp;
                }
            }
        }
        
        System.out.println("\nHotels sorted by rating (descending) and then price (ascending):");
        for (int i = 0; i < n; i++) {
            System.out.println(hotels[i].name + " - Rating: " + hotels[i].rating + 
                             ", Price: " + hotels[i].price);
        }
        
        System.out.println("\nName : Suryansh Mithu");
        System.out.println("Roll : 24155060");
        
        sc.close();
    }
}
```

**Sample Output:**
```
Enter number of hotels: 
5
Enter hotel name: 
Taj Palace
Enter rating: 
4.8
Enter price: 
12000
Enter hotel name: 
Oberoi
Enter rating: 
4.9
Enter price: 
15000
Enter hotel name: 
Leela Palace
Enter rating: 
4.8
Enter price: 
11000
Enter hotel name: 
ITC Maratha
Enter rating: 
4.7
Enter price: 
10000
Enter hotel name: 
Hyatt
Enter rating: 
4.7
Enter price: 
9500

Hotels sorted by rating (descending) and then price (ascending):
Oberoi - Rating: 4.9, Price: 15000.0
Leela Palace - Rating: 4.8, Price: 11000.0
Taj Palace - Rating: 4.8, Price: 12000.0
Hyatt - Rating: 4.7, Price: 9500.0
ITC Maratha - Rating: 4.7, Price: 10000.0

Name : Suryansh Mithu
Roll : 24155060
