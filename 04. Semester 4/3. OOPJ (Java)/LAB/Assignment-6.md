# Name : Vivek Singh
# Roll : 24155220
### **Part 1: Abstract Classes**

**1. Abstract Class with Abstract and Non-Abstract Methods**

```java
abstract class Shape {
    abstract void draw(); // Abstract method
    void display() { // Non-abstract method
        System.out.println("Displaying Shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing Circle");
    }
}

public class Main1 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Circle c = new Circle();
        c.draw();
        c.display();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Drawing Circle
Displaying Shape
```

---

**2. Abstract Class with Constructor**

```java
abstract class Animal {
    Animal() {
        System.out.println("Animal Constructor Invoked");
    }
}

class Dog extends Animal {
    Dog() {
        super(); // Implicitly calls parent constructor
        System.out.println("Dog Constructor Invoked");
    }
}

public class Main2 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        new Dog();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Animal Constructor Invoked
Dog Constructor Invoked
```

---

**3. Instance Variables and Final Methods**

```java
abstract class Device {
    String brand = "TechCorp"; // Instance variable

    final void showBrand() { // Final method
        System.out.println("Brand: " + brand);
    }
}

class Phone extends Device {
    // Cannot override showBrand() here
}

public class Main3 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Phone p = new Phone();
        p.showBrand();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Brand: TechCorp
```

---

**4. Partial Abstraction**

```java
abstract class Demo {
    abstract void abstractMethod();
    void concreteMethod() {
        System.out.println("Concrete Method");
    }
}
// Explanation: Complete abstraction is not possible in abstract classes because 
// they are designed to provide common default behavior (code reuse) via non-abstract methods.

class Impl extends Demo {
    void abstractMethod() { System.out.println("Implemented Abstract Method"); }
}

public class Main4 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Impl i = new Impl();
        i.concreteMethod();
        i.abstractMethod();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Concrete Method
Implemented Abstract Method
```

---

**5. Static Methods and Static Blocks in Abstract Class**

```java
abstract class Statics {
    static {
        System.out.println("Static Block Executed");
    }
    static void staticMethod() {
        System.out.println("Static Method Executed");
    }
}

public class Main5 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Statics.staticMethod();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Static Block Executed
Static Method Executed
```

---

**6. Template Method Pattern**

```java
abstract class Game {
    abstract void initialize();
    abstract void startPlay();
    abstract void endPlay();

    // Template method
    public final void play() {
        initialize();
        startPlay();
        endPlay();
    }
}

class Cricket extends Game {
    void initialize() { System.out.println("Cricket Game Initialized"); }
    void startPlay() { System.out.println("Cricket Game Started"); }
    void endPlay() { System.out.println("Cricket Game Finished"); }
}

public class Main6 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Game game = new Cricket();
        game.play();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Cricket Game Initialized
Cricket Game Started
Cricket Game Finished
```

---

**7. Runtime Polymorphism with Abstract Class Reference**

```java
abstract class Bank {
    abstract int getRateOfInterest();
}

class SBI extends Bank {
    int getRateOfInterest() { return 7; }
}

class PNB extends Bank {
    int getRateOfInterest() { return 5; }
}

public class Main7 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Bank b;
        b = new SBI();
        System.out.println("SBI Rate: " + b.getRateOfInterest() + "%");
        b = new PNB();
        System.out.println("PNB Rate: " + b.getRateOfInterest() + "%");
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
SBI Rate: 7%
PNB Rate: 5%
```

---

**8. Abstract Class Cannot be Instantiated**

```java
abstract class Base {}

class Derived extends Base {}

public class Main8 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        
        // Base b = new Base(); // This would cause a compile-time error
        Base b = new Derived(); // Reference usage is allowed
        System.out.println("Reference created successfully: " + b.getClass().getName());
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Reference created successfully: Derived
```

---

**9. Abstract Class Implementing Interface**

```java
interface M {
    void a();
    void b();
}

abstract class B implements M {
    public void a() { System.out.println("I am a"); }
}

class C extends B {
    public void b() { System.out.println("I am b"); }
}

public class Main9 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        C obj = new C();
        obj.a();
        obj.b();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
I am a
I am b
```

---

**10. Avoiding Code Duplication**

```java
abstract class Employee {
    String name;
    Employee(String n) { name = n; }
    void commonDetails() { System.out.println("Employee Name: " + name); } // Duplication avoided here
}

class Developer extends Employee {
    Developer(String n) { super(n); }
}

public class Main10 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Developer d = new Developer("Suryansh");
        d.commonDetails();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Employee Name: Suryansh
```

---

### **Part 2: Interfaces**

**11. Multiple Inheritance and Conflict Resolution**

```java
interface Alpha {
    default void show() { System.out.println("Alpha Show"); }
}

interface Beta {
    default void show() { System.out.println("Beta Show"); }
}

class Child implements Alpha, Beta {
    public void show() {
        Alpha.super.show(); // Resolving conflict
        Beta.super.show();
    }
}

public class Main11 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        new Child().show();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Alpha Show
Beta Show
```

---

**12. Interface Constants and Abstract Methods**

```java
interface Constants {
    double PI = 3.14159; // Constant
    void area(); // Abstract method
}

class CircleArea implements Constants {
    public void area() {
        System.out.println("Area Approx: " + (PI * 10 * 10));
    }
}

public class Main12 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        new CircleArea().area();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Area Approx: 314.159
```

---

**13. Functional Interface and Lambda**

```java
@FunctionalInterface
interface MathOp {
    int operate(int a, int b);
}

public class Main13 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        MathOp add = (a, b) -> a + b;
        System.out.println("Sum: " + add.operate(5, 10));
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Sum: 15
```

---

**14. Interface Reference and Dynamic Method Dispatch**

```java
interface AnimalSound {
    void sound();
}

class Cat implements AnimalSound {
    public void sound() { System.out.println("Meow"); }
}

public class Main14 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        AnimalSound a = new Cat();
        a.sound();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Meow
```

---

**15. Marker Interface**

```java
interface Permissible {} // Marker Interface (Empty)

class Document implements Permissible {}

public class Main15 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Document d = new Document();
        if (d instanceof Permissible) {
            System.out.println("Permission Granted");
        }
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Permission Granted
```

---

**16. Implementing Two Interfaces with Same Method Signature**

```java
interface I1 { void print(); }
interface I2 { void print(); }

class Printer implements I1, I2 {
    // One implementation satisfies both interfaces
    public void print() { System.out.println("Printing..."); }
}

public class Main16 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        new Printer().print();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Printing...
```

---

**17. Default and Static Methods in Interfaces**

```java
interface ModernInterface {
    default void defMethod() { System.out.println("Default Method"); }
    static void statMethod() { System.out.println("Static Method"); }
}

class ImplModern implements ModernInterface {}

public class Main17 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        ImplModern obj = new ImplModern();
        obj.defMethod();
        ModernInterface.statMethod();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Default Method
Static Method
```

---

**18. Interface Extending Interface**

```java
interface A { void methodA(); }
interface B extends A { void methodB(); }

class MyClass implements B {
    public void methodA() { System.out.println("Method A"); }
    public void methodB() { System.out.println("Method B"); }
}

public class Main18 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        MyClass obj = new MyClass();
        obj.methodA();
        obj.methodB();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Method A
Method B
```

---

**19. Interface vs Abstract Class**

```java
abstract class Abs {
    abstract void run();
    public Abs() { System.out.println("Abstract Constructor"); }
}

interface Intr {
    void walk();
    // No constructor allowed
}

class Human extends Abs implements Intr {
    void run() { System.out.println("Running"); }
    public void walk() { System.out.println("Walking"); }
}

public class Main19 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Human h = new Human();
        h.run();
        h.walk();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Abstract Constructor
Running
Walking
```

---

**20. Tight vs Loose Coupling**

```java
interface Engine { void start(); }

class PetrolEngine implements Engine {
    public void start() { System.out.println("Petrol Engine Started"); }
}

class Car {
    Engine e; // Loose Coupling via Interface
    Car(Engine e) { this.e = e; }
    void move() { e.start(); }
}

public class Main20 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Engine pe = new PetrolEngine();
        Car c = new Car(pe);
        c.move();
    }
}
```

**Sample Output:**

```
Name : Vivek Singh
Roll : 24155220
Petrol Engine Started
```

---

### **Part 3: Packages**

**21. Creating and Accessing Packages**

```java
// File: mypack/Simple.java
package mypack;
public class Simple {
    public void msg() { System.out.println("Message from mypack"); }
}

// File: Main21.java
import mypack.Simple;
public class Main21 {
    public static void main(String args[]) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Simple obj = new Simple();
        obj.msg();
    }
}
```

**22. Access Control Across Packages**

```java
// File: pack1/A.java
package pack1;
public class A {
    public void msg() { System.out.println("Public Access"); }
    protected void pro() { System.out.println("Protected Access"); }
}

// File: Main22.java
import pack1.A;
public class Main22 {
    public static void main(String args[]) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        A obj = new A();
        obj.msg(); // Allowed
        // obj.pro(); // Compilation Error (Protected not visible here)
    }
}
```

**23. Package with Interface and Abstract Class**

```java
// File: tools/Blueprint.java
package tools;
public interface Blueprint { void build(); }

// File: tools/Base.java
package tools;
public abstract class Base { public abstract void init(); }

// File: Main23.java
import tools.*;
class House extends Base implements Blueprint {
    public void build() { System.out.println("Building House"); }
    public void init() { System.out.println("Initializing Base"); }
}
public class Main23 {
    public static void main(String args[]){
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        House h = new House();
        h.init();
        h.build();
    }
}
```

**24. Protected Members in Inheritance Across Packages**

```java
// File: p1/Parent.java
package p1;
public class Parent {
    protected void show() { System.out.println("Protected Show"); }
}

// File: p2/Child.java
package p2;
import p1.Parent;
class Child extends Parent {
    public void access() { show(); } // Accessible via inheritance
}
public class Main24 { 
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        new p2.Child().access();
    }
}
```

**25. Name Conflict Resolution**

```java
// File: java/util/Date is built-in
// File: java/sql/Date is built-in

public class Main25 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        java.util.Date d1 = new java.util.Date(); // Fully qualified name
        java.sql.Date d2 = new java.sql.Date(System.currentTimeMillis());
        System.out.println("Util Date: " + d1.toString().substring(0,3));
        System.out.println("SQL Date: " + d2);
    }
}
```

**26. Project Organization Benefits**

```java
// File: com/app/model/User.java
package com.app.model;
public class User { public String name="User1"; }

// File: com/app/service/UserService.java
package com.app.service;
import com.app.model.User;
public class UserService {
    public void printUser(User u) { System.out.println("Service processing: " + u.name); }
}

// File: Main26.java
import com.app.model.User;
import com.app.service.UserService;
public class Main26 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        UserService svc = new UserService();
        svc.printUser(new User());
    }
}
```

**27. Static Import**

```java
import static java.lang.Math.*; // Static import

public class Main27 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        System.out.println("Square Root of 16 is: " + sqrt(16)); // No Math.sqrt needed
    }
}
```

**28. Jar Creation and Usage**

```java
// 1. Compile: javac -d . MyClass.java
// 2. Create Jar: jar cvf mylib.jar mypack/MyClass.class
// 3. Run: java -cp mylib.jar:. Main28

// Code logic for Main28
public class Main28 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        System.out.println("Simulating usage of external JAR library.");
    }
}
```

**29. Encapsulation and Modularity**

```java
// File: bank/Account.java
package bank;
public class Account {
    private double balance = 1000;
    public double getBalance() { return balance; } // Encapsulation
}

// File: Main29.java
import bank.Account;
public class Main29 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        Account acc = new Account();
        System.out.println("Balance: " + acc.getBalance());
        // acc.balance = 0; // Not allowed, field is private (Encapsulation)
    }
}
```

**30. Class Loading Behavior**

```java
// File: loader/LoadMe.java
package loader;
public class LoadMe {
    static { System.out.println("Class Loading: LoadMe is loaded into memory."); }
}

// File: Main30.java
import loader.LoadMe;
public class Main30 {
    public static void main(String[] args) {
        System.out.println("Name : Vivek Singh");
        System.out.println("Roll : 24155220");
        System.out.println("Before accessing LoadMe");
        new LoadMe();
        System.out.println("After accessing LoadMe");
    }
}
```

**Sample Output:**

Plaintext

```
Name : Vivek Singh
Roll : 24155220
Before accessing LoadMe
Class Loading: LoadMe is loaded into memory.
After accessing LoadMe
```