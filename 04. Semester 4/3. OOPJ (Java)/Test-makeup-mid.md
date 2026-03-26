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

*   **Final Variables:** When applied to a data member, it creates a constant whose value cannot be reinitialized or changed once assigned[cite: 4, 6, 7].
*   **Final Methods:** A method declared as final cannot be overridden by any child classes, ensuring the implementation remains unchanged[cite: 4, 6, 7].
*   **Final Classes:** A class declared as final cannot be extended or inherited by another class[cite: 4, 6, 7].

### 4. Checked vs. Unchecked Exceptions
Questions asking to differentiate between these two types of exceptions, or to draw the `Throwable` hierarchy, are very common.

*   **Checked Exceptions:** These are checked at compile-time[cite: 3, 7]. The compiler ensures that these exceptions are either handled using a `try-catch` block or declared using the `throws` keyword[cite: 5, 7]. Examples include `IOException`, `SQLException`, and `ClassNotFoundException`[cite: 5, 7].
*   **Unchecked Exceptions:** These occur at runtime and are not checked by the compiler[cite: 3, 7]. They usually result from programming logic errors and do not require the JVM to catch or handle them at compile time[cite: 5, 7]. Examples include `ArithmeticException`, `NullPointerException`, and `ArrayIndexOutOfBoundsException`[cite: 5, 7].

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

Would you like me to write out the full Java code for any of the frequently repeated programming assignments, such as the Dynamic Method Dispatch programs (e.g., the Bank Interest Rate or Apple/Banana/Cherry examples)?