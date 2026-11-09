---
course: "OOPJ (Java)"
semester: 4
tags:
  - course/oopj-java
up: "[[OOPJ (Java)]]"
---
# Assignment - 3
## Name : Roushan Kumar
## Roll : 24156086


**Program 1: Using Constructor**
```java
import java.util.Scanner;

class Rectangle {
    double length, breadth;
    
    Rectangle(double l, double b) {
        length = l;
        breadth = b;
    }
    
    double area() {
        return length * breadth;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Name : Roushan Kumar");
        System.out.println("Roll : 24156086");
        System.out.println();
        
        System.out.println("Enter length and breadth for first rectangle:");
        double l1 = sc.nextDouble();
        double b1 = sc.nextDouble();
        Rectangle obj1 = new Rectangle(l1, b1);
        
        System.out.println("Enter length and breadth for second rectangle:");
        double l2 = sc.nextDouble();
        double b2 = sc.nextDouble();
        Rectangle obj2 = new Rectangle(l2, b2);
        
        System.out.println("Area of first rectangle: " + obj1.area());
        System.out.println("Area of second rectangle: " + obj2.area());
    }
}
```

**Program 1 Output:**
```
Name : Roushan Kumar
Roll : 24156086

Enter length and breadth for first rectangle:
8.5
4.2
Enter length and breadth for second rectangle:
12.3
7.6
Area of first rectangle: 35.7
Area of second rectangle: 93.48
```

**Program 2: Using Method**
```java
import java.util.Scanner;

class Rectangle {
    double length, breadth;
    
    void setDimensions(double l, double b) {
        length = l;
        breadth = b;
    }
    
    double area() {
        return length * breadth;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Name : Roushan Kumar");
        System.out.println("Roll : 24156086");
        System.out.println();
        
        Rectangle obj1 = new Rectangle();
        Rectangle obj2 = new Rectangle();
        
        System.out.println("Enter length and breadth for first rectangle:");
        double l1 = sc.nextDouble();
        double b1 = sc.nextDouble();
        obj1.setDimensions(l1, b1);
        
        System.out.println("Enter length and breadth for second rectangle:");
        double l2 = sc.nextDouble();
        double b2 = sc.nextDouble();
        obj2.setDimensions(l2, b2);
        
        System.out.println("Area of first rectangle: " + obj1.area());
        System.out.println("Area of second rectangle: " + obj2.area());
    }
}
```

**Program 2 Output:**
```
Name : Roushan Kumar
Roll : 24156086

Enter length and breadth for first rectangle:
6.8
3.5
Enter length and breadth for second rectangle:
10.2
5.9
Area of first rectangle: 23.8
Area of second rectangle: 60.18
```

**Program 3: Counting Objects Using Static**
```java
class Counter {
    static int count = 0;
    
    Counter() {
        count++;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Roushan Kumar");
        System.out.println("Roll : 24156086");
        System.out.println();
        
        System.out.println("Initial count: " + Counter.count);
        Counter obj1 = new Counter();
        Counter obj2 = new Counter();
        Counter obj3 = new Counter();
        
        System.out.println("Number of objects created: " + Counter.count);
    }
}
```
**Program 3 Output:**
```
Name : Roushan Kumar
Roll : 24156086

Initial count: 0
Number of objects created: 3
```

**Program 4: Box Volume Calculation**
```java
import java.util.Scanner;

class Box {
    double length, width, height;
    
    Box(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }
    
    double volume() {
        return length * width * height;
    }
}

public class Demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Name : Roushan Kumar");
        System.out.println("Roll : 24156086");
        System.out.println();
        
        System.out.println("Enter length, width and height of box:");
        double l = sc.nextDouble();
        double w = sc.nextDouble();
        double h = sc.nextDouble();
        
        Box box = new Box(l, w, h);
        System.out.println("Volume of box: " + box.volume());
    }
}
```

**Program 4 Output:**
```
Name : Roushan Kumar
Roll : 24156086

Enter length, width and height of box:
9.5
6.2
3.8
Volume of box: 224.42
```

**Program 5: Rectangle with Read, Calculate, Display**
```java
import java.util.Scanner;

class Rectangle {
    double length, breadth;
    
    void read(double l, double b) {
        length = l;
        breadth = b;
    }
    
    double calculateArea() {
        return length * breadth;
    }
    
    double calculatePerimeter() {
        return 2 * (length + breadth);
    }
    
    void display() {
        System.out.println("Area: " + calculateArea());
        System.out.println("Perimeter: " + calculatePerimeter());
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Name : Roushan Kumar");
        System.out.println("Roll : 24156086");
        System.out.println();
        
        Rectangle rect = new Rectangle();
        
        System.out.println("Enter length and breadth of rectangle:");
        double l = sc.nextDouble();
        double b = sc.nextDouble();
        
        rect.read(l, b);
        rect.display();
    }
}
```

**Program 5 Output:**
```
Name : Roushan Kumar
Roll : 24156086

Enter length and breadth of rectangle:
14.6
8.4
Area: 122.64
Perimeter: 46.0
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[OOPJ (Java)]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Assignment-12|Assignment-12]] · **Next:** [[04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/OOPJ Theory - Join, Daemon, Priority|OOPJ Theory - Join, Daemon, Priority]]
> **Related:** [[Data Structures]] · [[Operating Systems]] · [[DBMS]]
<!-- connections:end -->
