
### 1. Child class calls a parameterized parent constructor using `super()`

Java

```
class A {
    A(int x) {
        System.out.println(x);
    }
}

class B extends A {
    B() {
        super(5);
    }
    public static void main(String[] args) {
        new B();
    }
}
```

### 2. Accessing a hidden parent class variable using `super`

Java

```
class A {
    int x = 10;
}

class B extends A {
    int x = 20;
    void m() {
        System.out.println(super.x);
    }
    public static void main(String[] args) {
        new B().m();
    }
}
```

### 3. Override a method and invoke the parent version using `super.method()`

Java

```
class A {
    void m() {
        System.out.println("A");
    }
}

class B extends A {
    void m() {
        super.m();
        System.out.println("B");
    }
    public static void main(String[] args) {
        new B().m();
    }
}
```

### 4. Show that `super()` must be the first statement in a constructor

_(Note: Designed to show compilation logic)_

Java

```
class A {}

class B extends A {
    B() {
        // System.out.println("X");
        super();
    }
}
```

### 5. Constructor execution order using `super`

Java

```
class A {
    A() {
        System.out.println("A");
    }
}

class B extends A {
    B() {
        super();
        System.out.println("B");
    }
    public static void main(String[] args) {
        new B();
    }
}
```

### 6. Program where omission of `super()` causes a compilation error

_(Note: Fails because Parent has no default constructor)_

Java

```
class A {
    A(int x) {}
}

class B extends A {
    B() {
        super(1);
    }
}
```

### 7. Use `super` in multilevel inheritance

Java

```
class A {
    int x = 1;
}

class B extends A {}

class C extends B {
    void m() {
        System.out.println(super.x);
    }
    public static void main(String[] args) {
        new C().m();
    }
}
```

### 8. Variable shadowing and resolution using `super`

Java

```
class A {
    int x = 5;
}

class B extends A {
    int x = 10;
    void m() {
        System.out.println(x);
        System.out.println(super.x);
    }
    public static void main(String[] args) {
        new B().m();
    }
}
```

### 9. Method and variable name conflict resolution using `super`

Java

```
class A {
    int x = 1;
    void x() { System.out.println("M"); }
}

class B extends A {
    void m() {
        System.out.println(super.x);
        super.x();
    }
    public static void main(String[] args) {
        new B().m();
    }
}
```

### 10. Distinguish between `this` and `super`

Java

```
class A {
    int x = 1;
}

class B extends A {
    int x = 2;
    void m() {
        System.out.println(this.x);
        System.out.println(super.x);
    }
    public static void main(String[] args) {
        new B().m();
    }
}
```

### 11. Demonstrate that a `final` variable cannot be modified

Java

```
class A {
    final int x = 1;
    void m() {
        // x = 2;
    }
}
```

### 12. Initialize a `final` variable using a constructor

Java

```
class A {
    final int x;
    A() {
        x = 5;
    }
    public static void main(String[] args) {
        System.out.println(new A().x);
    }
}
```

### 13. Show that a `final` method cannot be overridden

Java

```
class A {
    final void m() {}
}

class B extends A {
    // void m() {}
}
```

### 14. Demonstrate that a `final` class cannot be inherited

Java

```
final class A {}
// class B extends A {}
```

### 15. Show behavior of a `final` reference variable

Java

```
class A {
    int x = 1;
}

class B {
    public static void main(String[] args) {
        final A a = new A();
        a.x = 2;
        // a = new A();
    }
}
```

### 16. Use `final` keyword with constructor parameters

Java

```
class A {
    A(final int x) {
        System.out.println(x);
    }
    public static void main(String[] args) {
        new A(5);
    }
}
```

### 17. Demonstrate how `final` restricts runtime polymorphism

Java

```
class A {
    final void m() { System.out.println("A"); }
}

class B extends A {
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 18. Show compile-time error when overriding a `final` method

Java

```
class A {
    final void m() {}
}

class B extends A {
    // void m() {}
}
```

### 19. Initialize a `final` variable inside an instance initializer block

Java

```
class A {
    final int x;
    {
        x = 10;
    }
    public static void main(String[] args) {
        System.out.println(new A().x);
    }
}
```

### 20. Demonstrate execution of an instance initializer block

Java

```
class A {
    {
        System.out.println("B");
    }
    public static void main(String[] args) {
        new A();
    }
}
```

### 21. Show execution order of instance initializer block and constructor

Java

```
class A {
    A() {
        System.out.println("C");
    }
    {
        System.out.println("B");
    }
    public static void main(String[] args) {
        new A();
    }
}
```

### 22. Demonstrate multiple instance initializer blocks and their execution order

Java

```
class A {
    { System.out.println("1"); }
    { System.out.println("2"); }
    public static void main(String[] args) {
        new A();
    }
}
```

### 23. Show instance initializer block execution in inheritance

Java

```
class A {
    { System.out.println("A"); }
}

class B extends A {
    { System.out.println("B"); }
    public static void main(String[] args) {
        new B();
    }
}
```

### 24. Initialize instance variables using an instance initializer block

Java

```
class A {
    int x;
    {
        x = 5;
    }
    public static void main(String[] args) {
        System.out.println(new A().x);
    }
}
```

### 25. Demonstrate runtime polymorphism using method overriding

Java

```
class A {
    void m() { System.out.println("A"); }
}

class B extends A {
    void m() { System.out.println("B"); }
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 26. Demonstrate dynamic method dispatch using parent reference and child object

Java

```
class A {
    void m() { System.out.println("P"); }
}

class B extends A {
    void m() { System.out.println("C"); }
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 27. Show that runtime polymorphism does not apply to instance variables

Java

```
class A {
    int x = 1;
}

class B extends A {
    int x = 2;
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.x);
    }
}
```

### 28. Demonstrate runtime polymorphism in multilevel inheritance

Java

```
class A {
    void m() { System.out.println("A"); }
}

class B extends A {
    void m() { System.out.println("B"); }
}

class C extends B {
    void m() { System.out.println("C"); }
    public static void main(String[] args) {
        A a = new C();
        a.m();
    }
}
```

### 29. Show that constructors do not support runtime polymorphism

Java

```
class A {
    A() { System.out.println("A"); }
}

class B extends A {
    B() { System.out.println("B"); }
    public static void main(String[] args) {
        A a = new B();
    }
}
```

### 30. Demonstrate that static methods are not polymorphic

Java

```
class A {
    static void m() { System.out.println("A"); }
}

class B extends A {
    static void m() { System.out.println("B"); }
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 31. Show effect of `final` method on runtime polymorphism

Java

```
class A {
    final void m() { System.out.println("A"); }
}

class B extends A {
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 32. Demonstrate runtime binding of overridden methods

Java

```
class A {
    void m() { System.out.println("A"); }
}

class B extends A {
    void m() { System.out.println("B"); }
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 33. Program where a parent reference invokes different child implementations

Java

```
class A {
    void m() {}
}

class B extends A {
    void m() { System.out.println("B"); }
}

class C extends A {
    void m() { System.out.println("C"); }
    public static void main(String[] args) {
        A a;
        a = new B(); a.m();
        a = new C(); a.m();
    }
}
```

### 34. Demonstrate polymorphism using arrays of parent-class references

Java

```
class A {
    void m() {}
}

class B extends A {
    void m() { System.out.println("B"); }
}

class C extends A {
    void m() { System.out.println("C"); }
    public static void main(String[] args) {
        A[] x = { new B(), new C() };
        for (A a : x) a.m();
    }
}
```

### 35. Method call resolution when overridden methods throw exceptions

Java

```
class A {
    void m() {}
}

class B extends A {
    void m() throws RuntimeException {
        System.out.println("B");
    }
    public static void main(String[] args) {
        A a = new B();
        a.m();
    }
}
```

### 36. Demonstrate polymorphism with method parameters and return types

Java

```
class A {
    Number m() { return 1; }
}

class B extends A {
    Integer m() { return 2; }
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.m());
    }
}
```

### 37. Program showing upcasting and its role in polymorphism

Java

```
class A {
    void m() { System.out.println("A"); }
}

class B extends A {
    void m() { System.out.println("B"); }
    public static void main(String[] args) {
        A a = (A) new B();
        a.m();
    }
}
```

### 38. Demonstrate why downcasting can cause `ClassCastException`

Java

```
class A {}
class B extends A {}

class C {
    public static void main(String[] args) {
        A a = new A();
        // B b = (B) a;
    }
}
```

### 39. Single program combining `super` + `final` + runtime polymorphism

Java

```
class A {
    final void f() {
        System.out.println("F");
    }
    void m() {
        System.out.println("A");
    }
}

class B extends A {
    void m() {
        super.m();
        System.out.println("B");
    }
    public static void main(String[] args) {
        A a = new B();
        a.f();
        a.m();
    }
}
```

