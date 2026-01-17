# Name : Utkarsh Dwivedi
# Roll : 24051673

## Program 1: 

```java
import java.util.*;

class A {
    double a, b;
    A() {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter length: ");
        a = s.nextDouble();
        System.out.print("Enter width: ");
        b = s.nextDouble();
    }
}

class B extends A {
    double c;
    B() {
        super();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter height: ");
        c = s.nextDouble();
    }
}

class C extends B {
    double d;
    C() {
        super();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter thick: ");
        d = s.nextDouble();
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
    }
}

public class Main {
    public static void main(String[] args) {
        C obj = new C();
        System.out.println("Length: " + obj.a);
        System.out.println("Width: " + obj.b);
        System.out.println("Height: " + obj.c);
        System.out.println("Thick: " + obj.d);
    }
}
```

~={red} Name : Utkarsh Dwivedi =~

```
Enter length: 10
Enter width: 20
Enter height: 30
Enter thick: 5
~={red} Name : Utkarsh Dwivedi =~
Roll : 24051673
Length: 10.0
Width: 20.0
Height: 30.0
Thick: 5.0
```

## **Program 2:**

```java
class Apple {
    void show() {
        System.out.println("Apple class show method");
    }
}

class Banana extends Apple {
    void show() {
        System.out.println("Banana class show method");
    }
}

class Cherry extends Apple {
    void show() {
        System.out.println("Cherry class show method");
    }
}

public class Main {
    public static void main(String[] args) {
        Apple a;
        
        a = new Apple();
        a.show();
        
        a = new Banana();
        a.show();
        
        a = new Cherry();
        a.show();
        
        System.out.println("Name : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
    }
}
```


```
Apple class show method
Banana class show method
Cherry class show method
Name : Utkarsh Dwivedi
Roll : 24051673
```

## **Program 3:**

```java
import java.util.*;

class Account {
    int acc;
    double bal;
    
    void input() {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter account number: ");
        acc = s.nextInt();
        System.out.print("Enter balance: ");
        bal = s.nextDouble();
    }
    
    void disp() {
        System.out.println("Account Number: " + acc);
        System.out.println("Balance: " + bal);
    }
}

class Person extends Account {
    String name;
    String aadhar;
    
    void input() {
        super.input();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = s.nextLine();
        System.out.print("Enter aadhar number: ");
        aadhar = s.nextLine();
    }
    
    void disp() {
        super.disp();
        System.out.println("Name: " + name);
        System.out.println("Aadhar Number: " + aadhar);
    }
}

public class Main {
    public static void main(String[] args) {
        Person[] p = new Person[3];
        
        for(int i = 0; i < 3; i++) {
            System.out.println("\nEnter details for person " + (i+1));
            p[i] = new Person();
            p[i].input();
        }
        
        System.out.println("\nDetails of all persons:");
        for(int i = 0; i < 3; i++) {
            System.out.println("\nPerson " + (i+1) + " details:");
            p[i].disp();
        }
        
        System.out.println("\nName : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
    }
}
```


```
Enter details for person 1
Enter account number: 101
Enter balance: 5000
Enter name: Rajesh
Enter aadhar number: 111122223333

Enter details for person 2
Enter account number: 102
Enter balance: 7000
Enter name: Priya
Enter aadhar number: 444455556666

Enter details for person 3
Enter account number: 103
Enter balance: 9000
Enter name: Amit
Enter aadhar number: 777788889999

Details of all persons:

Person 1 details:
Account Number: 101
Balance: 5000.0
Name: Rajesh
Aadhar Number: 111122223333

Person 2 details:
Account Number: 102
Balance: 7000.0
Name: Priya
Aadhar Number: 444455556666

Person 3 details:
Account Number: 103
Balance: 9000.0
Name: Amit
Aadhar Number: 777788889999

Name : Utkarsh Dwivedi
Roll : 24051673
```

## **Program 4:**

```java
abstract class Student {
    int roll;
    String name;
    
    Student(int r, String n) {
        roll = r;
        name = n;
    }
    
    abstract void marks();
}

class CIA extends Student {
    CIA(int r, String n) {
        super(r, n);
    }
    
    void marks() {
        System.out.println("CIA marks for " + name + " (Roll: " + roll + "): 85");
    }
}

class Semester extends Student {
    Semester(int r, String n) {
        super(r, n);
    }
    
    void marks() {
        System.out.println("Semester marks for " + name + " (Roll: " + roll + "): 90");
    }
}

public class Main {
    public static void main(String[] args) {
        CIA c = new CIA(1, "Utkarsh");
        Semester s = new Semester(2, "Rahul");
        
        c.marks();
        s.marks();
        
        System.out.println("\nName : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
    }
}
```


```
CIA marks for Utkarsh (Roll: 1): 85
Semester marks for Rahul (Roll: 2): 90

Name : Utkarsh Dwivedi
Roll : 24051673
```

## **Program 5:**

```java
interface Currency {
    void moneyconversion();
    void countrycurrency();
}

class CurrencyConversion implements Currency {
    public void moneyconversion() {
        System.out.println("Money conversion: 1 USD = 83 INR");
    }
    
    public void countrycurrency() {
        System.out.println("Country currency: India uses Rupee (INR)");
    }
}

public class Main {
    public static void main(String[] args) {
        CurrencyConversion obj = new CurrencyConversion();
        obj.moneyconversion();
        obj.countrycurrency();
        
        System.out.println("\nName : Utkarsh Dwivedi");
        System.out.println("Roll : 24051673");
    }
}
```


```
Money conversion: 1 USD = 83 INR
Country currency: India uses Rupee (INR)

Name : Utkarsh Dwivedi
Roll : 24051673
```