Based on the detailed analysis of the **OOPJ (CS20004)** Syllabus and **Mid-Semester Question Papers (2023, 2024, 2025)**, here is the prioritized analysis.

### **Exam Pattern Insight**

- **Total Marks:** Typically **20 Marks** for Mid-Semester.
    
- **Structure:**
    
    - **Q1 (Compulsory):** 5 Short Questions (1 Mark each) – _Mostly output finding & theory._
        
    - **Q2 - Q5:** Subjective/Coding (Answer any 3 or 4) – _Usually 2.5 to 5 Marks each._
        

---

### **Priority-Wise Important Topics & Weightage Table**

|**Priority**|**Topic**|**Approx. Weightage**|**Important & Repeated Questions**|
|---|---|---|---|
|**1**|**Dynamic Method Dispatch (Polymorphism) & Abstraction**|**5 - 8 Marks** (High)|• **Coding:** Design an Abstract class `Figure` (or `Shape`) with `area()`. Derive `Circle` & `Triangle`. Call `area()` using parent reference.<br><br>  <br><br>• **Coding:** Design an Interface `Bank` (or `Transaction`) with `interest()`. Implement in `SBI`, `HDFC`.<br><br>  <br><br>• **Theory:** Differentiate between Abstract Class & Interface.<br><br>  <br><br>• **Theory:** Explain Dynamic Method Dispatch with example.|
|**2**|**Exception Handling**|**2.5 - 5 Marks** (High)|• **Theory:** Differentiate between Checked & Unchecked Exceptions.<br><br>  <br><br>• **Coding:** Write a program to throw a **User-Defined Exception** (e.g., `InvalidAgeException` or `InvalidSetException` if odd numbers > even numbers).<br><br>  <br><br>• **Theory:** Purpose of `try`, `catch`, `finally`, `throw`, and `throws`.|
|**3**|**Java Basics: Operators & Output Finding**|**3 - 5 Marks** (Medium)|• **Output:** Bitwise AND/OR (`&`, `|
|**4**|**Keywords: `static`, `final`, `this`, `super`**|**2 - 4 Marks** (Medium)|• **Theory:** Can a class be `abstract` and `final` at the same time? (**No** - _Most Repeated_).<br><br>  <br><br>• **Theory:** Can `this()` and `super()` be used together? (**No**).<br><br>  <br><br>• **Theory:** Uses of `final` keyword (variable, method, class).<br><br>  <br><br>• **Theory:** Static block vs Static method execution.|
|**5**|**Inheritance & Methods**|**2.5 Marks** (Low)|• **Theory:** Method Overloading vs Method Overriding (Rules & Differences).<br><br>  <br><br>• **Theory:** Types of Inheritance supported in Java.<br><br>  <br><br>• **Coding:** Constructor Overloading (e.g., `Complex` number class with different constructors).|
|**6**|**Inner Classes & Packages**|**2.5 Marks** (Low)|• **Theory:** Types of Inner Classes (Member, Static, Local, Anonymous).<br><br>  <br><br>• **Coding:** Create a Class `Student` with an Inner Class `Address`/`Exam`.<br><br>  <br><br>• **Coding:** Create a package `geometry`, import it in `Demo` class.|

---

### **List of Important Repeated Coding Questions**

These specific scenarios appear almost every year. If you code these, you cover 80% of the coding section.

#### **1. The "Shape" or "Bank" Problem (Polymorphism)**

- **Question:** Write a program to define an interface `Transaction` with methods `deposit()` and `withdraw()`. Implement this interface in classes `HDFC` and `ICICI`. Write a driver class to call these methods using the interface reference.
    
- _Variation:_ Abstract class `Figure` with abstract method `area()`. Subclasses `Rectangle` and `Triangle` calculate the area.
    

#### **2. User-Defined Exception**

- **Question:** Write a program to accept `N` integers. If a specific condition is met (e.g., "Number of even elements < Number of odd elements" or "Age < 18"), throw a custom exception named `InvalidSetException`. Otherwise, display the sum.
    

#### **3. Inner Class Implementation**

- **Question:** Design a class `Student` with private members (name, roll). Inside it, create an inner class `Exam` or `Address` that holds specific details (marks/city). Demonstrate how the outer class can access members of the inner class.
    

#### **4. Array Logic & Swapping**

- **Question:** Accept 10 numbers. Write a function to swap:
    
    - 1st element with Last
        
    - 2nd element with 2nd Last
        
    - (and so on...)
        
- **Question:** Generate an Arithmetic Sequence (AP) given the first term and difference, storing it in an array.
    

#### **5. Command Line Arguments**

- **Question:** Accept 3 numbers from Command Line Arguments and 2 from `Scanner`. Print only the repeated numbers or the sum.
    

---

### **Q1 "Output Finding" Cheat Sheet**

Memorize these behaviors for the 1-mark questions:

1. **Shift Operators:**
    
    - `x << n` $\rightarrow$ Multiplies `x` by $2^n$.
        
    - `x >> n` $\rightarrow$ Divides `x` by $2^n$ (Sign is preserved).
        
    - `x >>> n` $\rightarrow$ Divides by $2^n$ (Sign bit becomes 0, always positive).
        
2. **Abstract & Final:**
    
    - **Question:** "Can a class be abstract and final?"
        
    - **Answer:** **NO**. Abstract requires inheritance; Final prevents inheritance. They are opposites.
        
3. **This & Super:**
    
    - **Question:** "Can `this()` and `super()` be in the same constructor?"
        
    - **Answer:** **NO**. Both must be the _first_ statement, so they cannot coexist.