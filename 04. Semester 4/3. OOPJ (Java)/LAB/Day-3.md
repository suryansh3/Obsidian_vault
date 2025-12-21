
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
