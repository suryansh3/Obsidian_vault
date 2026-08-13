# Name : Aryan Veer
# Roll : 24052554

### 1. Child class calls parameterized parent constructor using super()


```java
class A {
    A(int x) {
        System.out.println("Parent val: " + x);
    }
}

class B extends A {
    B() {
        super(100);
        System.out.println("Child constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Parent val: 100
Child constructor

Process finished with exit code 0
```

---

### 2. Demonstrate accessing a hidden parent class variable using super

```java
class A {
    int x = 10;
}

class B extends A {
    int x = 20;
    void show() {
        System.out.println("Child x: " + x);
        System.out.println("Parent x: " + super.x);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B().show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Child x: 20
Parent x: 10

Process finished with exit code 0
```

---

### 3. Override a method in a child class and invoke the parent version

```java
class A {
    void msg() {
        System.out.println("Parent message");
    }
}

class B extends A {
    void msg() {
        super.msg();
        System.out.println("Child message");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B().msg();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Parent message
Child message

Process finished with exit code 0
```

---

### 4. Show that super() must be the first statement in a constructor

```java
class A {
    A() {
        System.out.println("A");
    }
}

class B extends A {
    B() {
        System.out.println("B");
        super();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B();
    }
}
```

**Output:**
```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question4.java:11: error
call to super must be first statement in constructor
        super();     ^
```


### 5. Demonstrate constructor execution order using super

```java
class A {
    A() {
        System.out.println("Constructor A");
    }
}

class B extends A {
    B() {
        super();
        System.out.println("Constructor B");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Constructor A
Constructor B

Process finished with exit code 0
```

---

### 6. Program where omission of super() causes a compilation error

```java
class A {
    A(int x) {}
}

class B extends A {
    B() {
        
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B();
    }
}
```

**Output:**

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question6.java:9: error
constructor A in class A cannot be applied to given types
    B() {
    ^
```

---

### 7. Use super in multilevel inheritance

```java
class A {
    void show() { System.out.println("A"); }
}

class B extends A {
    void show() { super.show(); System.out.println("B"); }
}

class C extends B {
    void show() { super.show(); System.out.println("C"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new C().show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
A
B
C

Process finished with exit code 0
```

---

### 8. Demonstrate variable shadowing and resolution using super

```java
class A {
    String s = "Parent";
}

class B extends A {
    String s = "Child";
    void print() {
        System.out.println(s);
        System.out.println(super.s);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B().print();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Child
Parent

Process finished with exit code 0
```

---

### 9. Show method and variable name conflict resolution using super

```java
class A {
    int val = 5;
    void val() { System.out.println("Method A"); }
}

class B extends A {
    int val = 10;
    void val() {
        System.out.println("Var B: " + val);
        System.out.println("Var A: " + super.val);
        super.val();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B().val();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Var B: 10
Var A: 5
Method A

Process finished with exit code 0
```

---

### 10. Distinguish between this and super through a program

```java
class A {
    int x = 50;
}

class B extends A {
    int x = 100;
    void show() {
        int x = 150;
        System.out.println("Local: " + x);
        System.out.println("Instance: " + this.x);
        System.out.println("Parent: " + super.x);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B().show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Local: 150
Instance: 100
Parent: 50

Process finished with exit code 0
```

---

### 11. Demonstrate that a final variable cannot be modified

```java
public class Main {
    final int x = 10;
    
    void change() {
        x = 20;
    }

    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
    }
}
```

**Output:**

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question11.java:6: error
cannot assign a value to final variable number
        number = 200;
```

---

### 12. Initialize a final variable using a constructor

```
public class Main {
    final int x;

    Main() {
        x = 55;
    }

    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        System.out.println(new Main().x);
    }
}
```

**Output:**

Plaintext

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
55

Process finished with exit code 0
```

---

### 13. Show that a final method cannot be overridden

```java
class Parent13 {
    final void run() {}
}

class Child13 extends Parent13 {
    void run() {}
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
    }
}
```

**Output:**

Plaintext

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question13.java:8: error
method() in Child13 cannot override method() in Parent13
    void method() {
```

---

### 14. Demonstrate that a final class cannot be inherited

```java
final class Parent14 {}

class Child13 extends Parent14 {}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
    }
}
```

**Output:**

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question14.java:6: error
cannot inherit from final Parent14
class Child14 extends Parent14 {
```

---

### 15. Show behavior of a final reference variable

```
class A {
    int i = 10;
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        final A obj = new A();
        obj.i = 20; 
        System.out.println("Changed value: " + obj.i);
        // obj = new A(); 
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Changed value: 20

Process finished with exit code 0
```

---

### 16. Use final keyword with constructor parameters

```java
class A {
    A(final int x) {
        // x = 10; 
        System.out.println(x);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new A(5);
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
5

Process finished with exit code 0
```

---

### 17. Demonstrate how final restricts runtime polymorphism

```java
class Parent17 {
    final void show() { System.out.println("A"); }
}

class Child17 extends Parent17 {
     void show() { System.out.println("B"); } 
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.show(); 
    }
}
```

**Output:**

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question17.java:9: error
process() in Child17 cannot override process() in Parent17
    void process() {
         ^
```

---

### 18. Show compile-time error when overriding a final method

```java
class Parent18 {
    final void display() {}
}

class Child18 extends Parent18 {
    void display() {}
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
    }
}
```

**Output:**

Plaintext

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question18.java:8: error
demo() in Derived cannot override demo() in Base
    void demo() {
         ^
```

---

### 19. Initialize a final variable inside an instance initializer block

```java
class A {
    final int x;
    {
        x = 99;
    }
    void show() { System.out.println(x); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new A().show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
99

Process finished with exit code 0
```

---

### 20. Demonstrate execution of an instance initializer block

```java
class A {
    {
        System.out.println("Initializer Block");
    }
    A() {
        System.out.println("Constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new A();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Initializer Block
Constructor

Process finished with exit code 0
```

---

### 21. Show execution order of instance initializer block and constructor

```java
class A {
    A() { System.out.println("Constructor"); }
    { System.out.println("Block 1"); }
    { System.out.println("Block 2"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new A();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Block 1
Block 2
Constructor

Process finished with exit code 0
```

---

### 22. Demonstrate multiple instance initializer blocks and their execution order

```java
class A {
    { System.out.println("First"); }
    A() { System.out.println("Cons"); }
    { System.out.println("Second"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new A();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
First
Second
Cons

Process finished with exit code 0
```

---

### 23. Show instance initializer block execution in inheritance

```java
class A {
    { System.out.println("Block A"); }
    A() { System.out.println("Cons A"); }
}

class B extends A {
    { System.out.println("Block B"); }
    B() { System.out.println("Cons B"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        new B();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Block A
Cons A
Block B
Cons B

Process finished with exit code 0
```

---

### 24. Initialize instance variables using an instance initializer block

```java
class A {
    int x;
    {
        x = 42;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        System.out.println(new A().x);
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
42

Process finished with exit code 0
```

---

### 25. Demonstrate runtime polymorphism using method overriding

```java
class A {
    void play() { System.out.println("Playing A"); }
}

class B extends A {
    void play() { System.out.println("Playing B"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.play();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Playing B

Process finished with exit code 0
```

---

### 26. Demonstrate dynamic method dispatch using parent reference and child object

```
class Parent {
    void func() { System.out.println("Parent Func"); }
}
class Child extends Parent {
    void func() { System.out.println("Child Func"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        Parent ref = new Child();
        ref.func();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Child Func

Process finished with exit code 0
```

---

### 27. Show that runtime polymorphism does not apply to instance variables

```java
class A {
    int x = 1;
}

class B extends A {
    int x = 2;
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        System.out.println(obj.x);
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
1

Process finished with exit code 0
```

---

### 28. Demonstrate runtime polymorphism in multilevel inheritance

```java
class A { void eat() { System.out.println("A eats"); } }
class B extends A { void eat() { System.out.println("B eats"); } }
class C extends B { void eat() { System.out.println("C eats"); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A a = new C();
        a.eat();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
C eats

Process finished with exit code 0
```

---

### 29. Show that constructors do not support runtime polymorphism

```java
class A {
    A() { System.out.println("A"); }
}
class B extends A {
    B() { System.out.println("B"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
A
B

Process finished with exit code 0
```

---

### 30. Demonstrate that static methods are not polymorphic

```java
class A {
    static void show() { System.out.println("Static A"); }
}
class B extends A {
    static void show() { System.out.println("Static B"); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Static A

Process finished with exit code 0
```

---

### 31. Show effect of final method on runtime polymorphism

```java
class Parent31 {
    final void test() { System.out.println("Final A"); }
}
class Child31 extends Parent31{
     void test() { System.out.println("B"); } 
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.test();
    }
}
```

**Output:**

```
C:\Users\aryan\OneDrive\Documents\Java_OOPJ\Question31.java:8: error
action() in Child31 cannot override action() in Parent31
    void action() {
         ^
```

---

### 32. Demonstrate runtime binding of overridden methods

```java
class A { void f() { System.out.println("A"); } }
class B extends A { void f() { System.out.println("B"); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.f();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
B

Process finished with exit code 0
```

---

### 33. Parent reference invokes different child implementations

```java
class Shape { void draw() {} }
class Circle extends Shape { void draw() { System.out.println("Circle"); } }
class Box extends Shape { void draw() { System.out.println("Box"); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        Shape s;
        s = new Circle(); s.draw();
        s = new Box(); s.draw();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Circle
Box

Process finished with exit code 0
```

---

### 34. Demonstrate polymorphism using arrays of parent-class references

```java
class A { void go() { System.out.print("A "); } }
class B extends A { void go() { System.out.print("B "); } }
class C extends A { void go() { System.out.print("C "); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A[] arr = {new B(), new C(), new A()};
        for(A x : arr) x.go();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
B C A 
Process finished with exit code 0
```

---

### 35. Show method call resolution when overridden methods throw exceptions

```java
class A { void m() { System.out.println("A no exception"); } }
class B extends A { void m() throws RuntimeException { System.out.println("B exception"); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        try { obj.m(); } catch(Exception e) {}
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
B exception

Process finished with exit code 0
```

---

### 36. Demonstrate polymorphism with method parameters and return types

```java
class Parent31{}
class Child31extends Parent31 {}
class Test {
    A get() { return new B(); }
    void use(A a) { System.out.println("Used " + a.getClass().getSimpleName()); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        Test t = new Test();
        t.use(t.get());
    }
}
```

**Output:**

```
Name : Aryan Veer 
Roll : 24052554 
Child35 test
Exception in thread "main" java.lang.RuntimeException
    at Child35.test(Question35.java:10)
    at Question35.main(Question35.java:20)
```

---

### 37. Write a program showing upcasting and its role in polymorphism

```java
class Animal { void sound() { System.out.println("..."); } }
class Dog extends Animal { void sound() { System.out.println("Bark"); } }

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        Animal a = new Dog(); 
        a.sound();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Bark

Process finished with exit code 0
```

---

### 38. Demonstrate why downcasting can cause ClassCastException

```java
class A {}
class B extends A {}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new A();
        B b = (B) obj;
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
Exception in thread "main" java.lang.ClassCastException: class A cannot be cast to class B

Process finished with exit code 1
```

---

### 39. Single program combining super + final + runtime polymorphism

```java
class A {
    final int base = 10;
    void show() { System.out.println("A: " + base); }
}

class B extends A {
    void show() {
        super.show();
        System.out.println("B: " + (base + 5));
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Name : Aryan Veer ");
        System.out.println("Roll : 24052554 ");
        A obj = new B();
        obj.show();
    }
}
```

**Output:**

```
C:\Users\aryan\.jdks\openjdk-21\bin\java.exe -classpath C:\Users\aryan\OneDrive\Documents\Java_OOPJ\out\production\Java_OOPJ Main
Name : Aryan Veer 
Roll : 24052554 
A: 10
B: 15

Process finished with exit code 0
```

