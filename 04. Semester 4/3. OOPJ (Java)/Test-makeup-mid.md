### 1. Object-Oriented Programming (OOP) Principles
Questions asking to define OOP concepts, classes, and objects, or to explain the four pillars of OOP with examples, appear in almost every semester's paper.

*   **Class and Object:** A class is a user-defined blueprint or prototype from which objects are created, sharing common characteristics and attributes. An object is a basic unit of OOP that represents real-life entities and is an instance of a class.
*   **Encapsulation:** This is the bundling of data (variables) and methods (functions) into a single unit or class, often restricting direct access by making variables private and using public getters/setters.
*   **Abstraction:** Hiding internal implementation details and exposing only the necessary functionality to the user.
*   **Inheritance:** A mechanism where one object or class acquires the properties and behaviors of a parent class, promoting code reusability.
*   **Polymorphism:** The ability to perform a single action in different ways, typically implemented via method overloading (compile-time) or method overriding (run-time).

### 2. Method Overloading vs. Method Overriding & Dynamic Method Dispatch
The difference between overloading and overriding, and the application of Dynamic Method Dispatch (DMD), is a highly repeated practical and theoretical question.

*   **Method Overloading:** Performed within the same class where multiple methods have the same name but different parameter lists (different numbers or types of parameters)[cite: 4, 5]. It is resolved at compile-time[cite: 4].
*   **Method Overriding:** Occurs between a superclass and a subclass where the subclass redefines a method with the exact same name, return type, and parameter list[cite: 4, 5]. It is resolved at run-time[cite: 4].
*   **Dynamic Method Dispatch:** This is a mechanism by which a call to an overridden method is resolved at runtime rather than compile time[cite: 4]. A superclass reference variable can refer to a subclass object, and the JVM determines which version of the method to call based on the actual object type during execution[cite: 3, 4].

### 3. The `final` Keyword
Examiners frequently ask for the uses or characteristics of the `final` keyword in Java.

*   **Final Variables:** When applied to a data member, it creates a constant whose value cannot be reinitialized or changed once assigned.
*   **Final Methods:** A method declared as final cannot be overridden by any child classes, ensuring the implementation remains unchanged.
*   **Final Classes:** A class declared as final cannot be extended or inherited by another class.

### 4. Checked vs. Unchecked Exceptions
Questions asking to differentiate between these two types of exceptions, or to draw the `Throwable` hierarchy, are very common.

*   **Checked Exceptions:** These are checked at compile-time. The compiler ensures that these exceptions are either handled using a `try-catch` block or declared using the `throws` keyword. Examples include `IOException`, `SQLException`, and `ClassNotFoundException`.
*   **Unchecked Exceptions:** These occur at runtime and are not checked by the compiler. They usually result from programming logic errors and do not require the JVM to catch or handle them at compile time. Examples include `ArithmeticException`, `NullPointerException`, and `ArrayIndexOutOfBoundsException`.

### 5. Abstract Classes vs. Interfaces & Multiple Inheritance
The differences between abstract classes and interfaces, specifically regarding multiple inheritance, are standard exam topics.

*   **Methods:** Abstract classes can contain both abstract and non-abstract methods, whereas interfaces traditionally contain only abstract methods (though default/static methods are now allowed)[cite: 5].
*   **Inheritance Keywords:** An abstract class is extended using the `extends` keyword, while an interface is implemented using the `implements` keyword[cite: 5].
*   **Multiple Inheritance:** Java classes do not support multiple inheritance due to ambiguity issues (the "diamond problem"), meaning an abstract class can only extend one class[cite: 5, 6]. However, multiple inheritance is supported through interfaces, as a single class can implement multiple interfaces without ambiguity since the implementation is provided by the implementing class itself[cite: 5, 6].

### 6. Web Technology Specifics: CSS and HTML Forms
For the Web Technology specific exams, creating forms and understanding CSS integration are the most repeated concepts.

*   **CSS Integration:** CSS can be applied in three ways: **Inline** (using the `style` attribute inside HTML elements), **Internal** (using the `<style>` tag in the `<head>` section), and **External** (using the `<link>` element to attach an external `.css` file)[cite: 1, 3].
*   **CSS Selectors:** Common selectors include the **Element Selector** (selects by HTML tag name), **Id Selector** (uses `#` to select a unique element), and **Class Selector** (uses a period `.` to select elements with a specific class attribute)[cite: 3].

***
### 1. Dynamic Method Dispatch (Method Overriding)

This is a classic question used to test your understanding of runtime polymorphism. The prompt usually asks you to create a base class and derived classes with an overridden method.

**The Prompt:** Write a program having three classes `Apple`, `Banana`, and `Cherry`. `Banana` and `Cherry` inherit from `Apple`. Each class has its own `show()` method. Use Dynamic Method Dispatch to display the `show()` method of each class.

Java

```
class Apple {
    void show() {
        System.out.println("Inside Apple's show method");
    }
}

class Banana extends Apple {
    @Override
    void show() {
        System.out.println("Inside Banana's show method");
    }
}

class Cherry extends Apple {
    @Override
    void show() {
        System.out.println("Inside Cherry's show method");
    }
}

public class DynamicDispatchDemo {
    public static void main(String args[]) {
        // Creating objects of each class
        Apple a = new Apple();
        Banana b = new Banana();
        Cherry c = new Cherry();
        
        // Superclass reference variable
        Apple ref; 
        
        ref = a; // refers to Apple object
        ref.show(); // Calls Apple's version of show()
        
        ref = b; // refers to Banana object
        ref.show(); // Calls Banana's version of show()
        
        ref = c; // refers to Cherry object
        ref.show(); // Calls Cherry's version of show()
    }
}
```

---

### 2. Abstract Classes
```java
abstract class Figure {
    abstract void area();
}
class Circle extends Figure {
    private double radius;
    public Circle(double radius) {
        this.radius = radius;}
    @Override
    public void area() {
        System.out.println("Area of Circle: " + (Math.PI * radius * radius));}}
class Square extends Figure {
    private double side;   
    public Square(double side) {
        this.side = side;}
    @Override
    public void area() {
        System.out.println("Area of Square: " + (side * side));}}
public class AbstractClassDemo {
    public static void main(String[] args) {
        Figure fig; 
        fig = new Circle(5);
        fig.area();
        fig = new Square(4);
        fig.area();}}
```

---

### 3. 

This assignment tests your ability to create user-defined exceptions, use `throw` and `throws`, and handle multithreading basics (`Thread.sleep`).

**The Prompt:** Create a user-defined exception called `IllegalArgsException`. Throw the exception if a negative timeout value is passed to `Thread.sleep()`. Otherwise, sleep for the given time and display "KIIT University" five times.


Custom Exception Handling & Threads

``` Java
class IllegalArgsException extends Exception {
    public IllegalArgsException(String str) {
        super(str);}}
public class CustomExceptionDemo {
    public static void main(String args[]) throws IllegalArgsException {
        int sleepTime = 500; 
        if (sleepTime < 0) {
            throw new IllegalArgsException("Value should be greater than or equal to zero");
        } else {
            for (int i = 0; i < 5; i++) {
                try {
                    Thread.sleep(sleepTime);
                } catch (InterruptedException e) {
                    System.out.println("Thread interrupted");
                }
                System.out.println("KIIT University");
            }
        }
    }
}
```

---

### 4. Inner Classes

Understanding how to nest classes and access their properties is another staple of these exams.

**The Prompt:** Design a `Student` class with private attributes `name` and `rollNo`. Inside it, implement an inner class `Exam` with attributes `subject` and `marks`. Provide methods to set/get marks and display details. Create a driver class to test it.

Java

```
class Student {
    private String name;
    private int rollNo;
    
    public Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }
    
    public void displayStudentDetails() {
        System.out.println("Student Name: " + name);
        System.out.println("Roll Number: " + rollNo);
    }
    
    // Inner class
    class Exam {
        private String subject;
        private double marks;
        
        public Exam(String subject) {
            this.subject = subject;
        }
        
        public void setMarks(double marks) {
            this.marks = marks;
        }
        
        public double getMarks() {
            return marks;
        }
        
        public void displayExamDetails() {
            System.out.println("Subject: " + subject);
            System.out.println("Marks Obtained: " + marks);
        }
    }
}

public class InnerClassDemo {
    public static void main(String[] args) {
        // Create an object of the outer class
        Student student = new Student("John Doe", 101);
        
        // Create an object of the inner class using the outer class instance
        Student.Exam exam = student.new Exam("Mathematics");
        exam.setMarks(85.5);
        
        // Display details
        student.displayStudentDetails();
        exam.displayExamDetails();
    }
}
```

######  Student class with private attributes name and rollNo to store the student's details.
``` java 
class Student {
private String name;
private int rollNo;
public Student(String name, int rollNo) {
this.name = name;
this.rollNo = rollNo;
}}
public void displayStudentDetails() {
System.out.println("Student Name: " + name);
System.out.println("Roll Number: " + rollNo);}
class Exam {
public double getMarks() 
private String subject;
private double marks;
public Exam(String subject) {
this.subject = subject;}
public void setMarks(double marks) {
this.marks = marks;}
return marks;}
public void displayExamDetails() {
System.out.println("Subject: " + subject);
public class Main {
System.out.println("Marks Obtained: " + marks);}}}
public static void main(String[] args) {
Student student = new Student("John Doe", 101);
Student.Exam exam = student.new Exam("Mathematics");
exam.setMarks(85.5);
student.displayStudentDetails();
exam.displayExamDetails();}}
```