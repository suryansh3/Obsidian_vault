# Name : Shivam Raj

# Roll : 24052323

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
shivam@ShivamKIIT:~/JAVA/Theory$ nano Simple.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . Simple.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.Simple
Welcome to package
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ mkdir pack mypack
shivam@ShivamKIIT:~/JAVA/Theory$ nano pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ nano mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.B
Hello
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.B
Hello
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.B
Hello
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ nano Simple.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . Simple.java
shivam@ShivamKIIT:~/JAVA/Theory$ tree com
com
└── javatpoint
    └── core
        └── Simple.class

shivam@ShivamKIIT:~/JAVA/Theory$ java com.javatpoint.core.Simple
Hello subpackage
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac Simple.java
Simple.java:8: error: data has private access in A
        System.out.println(obj.data);
                              ^
Simple.java:9: error: msg() has private access in A
        obj.msg();
           ^
2 errors
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
mypack/B.java:5: error: A is not public in pack; cannot be accessed from outside package
        A obj = new A();
        ^
mypack/B.java:5: error: A is not public in pack; cannot be accessed from outside package
        A obj = new A();
                    ^
2 errors
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.B
Hello
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . pack/A.java
shivam@ShivamKIIT:~/JAVA/Theory$ javac -d . mypack/B.java
shivam@ShivamKIIT:~/JAVA/Theory$ java mypack.B
Hello
shivam@ShivamKIIT:~/JAVA/Theory$
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
shivam@ShivamKIIT:~/JAVA/Theory$ javac Simple.java
Simple.java:6: error: msg() in Simple cannot override msg() in A
    void msg() { System.out.println("Hello java"); }
         ^
  attempting to assign weaker access privileges; was protected
1 error
shivam@ShivamKIIT:~/JAVA/Theory$
```