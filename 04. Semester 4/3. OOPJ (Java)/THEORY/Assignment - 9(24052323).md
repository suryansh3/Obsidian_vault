# Name : Pranav Sarangi

# Roll : 24052309

### 1.


```java
package mypack;
public class Simple{
    public static void main(String args[]){
        System.out.println("Welcome to package");
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ nano Simple.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . Simple.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.Simple
Welcome to package
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

---

# 2.


```java
package pack;
public class A {
    public void msg() { System.out.println("Hello"); }
}
```


```java
package mypack;
import pack.*;
class B {
    public static void main(String args[]){
        A obj = new A();
        obj.msg();
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ mkdir pack mypack
pranav@PranavKIIT:~/JAVA/Theory/day9$ nano pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ nano mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.B
Hello
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

``` java
package mypack;
import pack.A; // Specific import
class B {
    public static void main(String args[]){
        A obj = new A();
        obj.msg();
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.B
Hello
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

```java
package mypack;
class B {
    public static void main(String args[]){
        pack.A obj = new pack.A(); // Fully qualified name
        obj.msg();
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.B
Hello
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

---

### 3. Subpackages



```java
package com.javatpoint.core;
class Simple{
    public static void main(String args[]){
        System.out.println("Hello subpackage");
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ nano Simple.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . Simple.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ tree com
com
└── javatpoint
    └── core
        └── Simple.class

pranav@PranavKIIT:~/JAVA/Theory/day9$ java com.javatpoint.core.Simple
Hello subpackage
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

---

### 4.

```java
class A {
    private int data = 40;
    private void msg() { System.out.println("Hello java"); }
}
public class Simple {
    public static void main(String args[]) {
        A obj = new A();
        System.out.println(obj.data); // Error
        obj.msg(); // Error
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac Simple.java
Simple.java:8: error: data has private access in A
        System.out.println(obj.data);
                              ^
Simple.java:9: error: msg() has private access in A
        obj.msg();
           ^
2 errors
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

#### B. Default Access Modifier

```java
package pack;
class A { // Default access (not public)
    void msg() { System.out.println("Hello"); }
}
```

```java
package mypack;
import pack.*;
class B {
    public static void main(String args[]){
        A obj = new A(); // Error: A is not public
        obj.msg();
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
mypack/B.java:5: error: A is not public in pack; cannot be accessed from outside package
        A obj = new A();
        ^
mypack/B.java:5: error: A is not public in pack; cannot be accessed from outside package
        A obj = new A();
                    ^
2 errors
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

#### C. Protected Access Modifier

```java
package pack;
public class A {
    protected void msg() { System.out.println("Hello"); }
}
```

```java
package mypack;
import pack.*;
class B extends A { // Inheriting A
    public static void main(String args[]){
        B obj = new B();
        obj.msg(); // Accessing protected method via inheritance
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.B
Hello
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

#### D. Public Access Modifier

```java
package pack;
public class A {
    public void msg() { System.out.println("Hello"); }
}
```

```java
package mypack;
import pack.*;
class B {
    public static void main(String args[]){
        A obj = new A();
        obj.msg();
    }
}
```

``` 
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . pack/A.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac -d . mypack/B.java
pranav@PranavKIIT:~/JAVA/Theory/day9$ java mypack.B
Hello
pranav@PranavKIIT:~/JAVA/Theory/day9$
```

---

### 5. Access Modifiers with Method Overriding


``` java
class A {
    protected void msg() { System.out.println("Hello java"); }
}
public class Simple extends A {
    // Attempting to assign weaker access (default) to a protected method
    void msg() { System.out.println("Hello java"); } 
    
    public static void main(String args[]){
        Simple obj = new Simple();
        obj.msg();
    }
}
```

```
pranav@PranavKIIT:~/JAVA/Theory/day9$ javac Simple.java
Simple.java:6: error: msg() in Simple cannot override msg() in A
    void msg() { System.out.println("Hello java"); }
         ^
  attempting to assign weaker access privileges; was protected
1 error
pranav@PranavKIIT:~/JAVA/Theory/day9$
```