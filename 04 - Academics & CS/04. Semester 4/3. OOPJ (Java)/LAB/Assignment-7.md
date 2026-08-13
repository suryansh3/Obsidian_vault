# Name : Mehrav Lalotra
# Roll : 24052582

## **1. ArithmeticException Handling**
```java
import java.util.Scanner;

public class ArithmeticExceptionDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter numerator: ");
        int numerator = scanner.nextInt();
        System.out.print("Enter denominator: ");
        int denominator = scanner.nextInt();
        
        try {
            int result = numerator / denominator;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed");
        }
        
        scanner.close();
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Enter numerator: 10
Enter denominator: 0
Error: Division by zero is not allowed
Name : Mehrav Lalotra
Roll : 24052582
```

## **2. ArrayIndexOutOfBoundsException**
```java
public class ArrayIndexExceptionDemo {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        
        try {
            System.out.println("Accessing element at index 10: " + numbers[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Array index is out of bounds");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Error: Array index is out of bounds
Name : Mehrav Lalotra
Roll : 24052582
```

## **3. NumberFormatException**
```java
public class NumberFormatExceptionDemo {
    public static void main(String[] args) {
        String str1 = "123";
        String str2 = "abc";
        
        try {
            int num1 = Integer.parseInt(str1);
            System.out.println("First number: " + num1);
            int num2 = Integer.parseInt(str2);
            System.out.println("Second number: " + num2);
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format in string");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
First number: 123
Error: Invalid number format in string
Name : Mehrav Lalotra
Roll : 24052582
```

## **4. NullPointerException**
```java
public class NullPointerExceptionDemo {
    public static void main(String[] args) {
        String text = null;
        
        try {
            int length = text.length();
            System.out.println("Length: " + length);
        } catch (NullPointerException e) {
            System.out.println("Error: Object reference is null");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Error: Object reference is null
Name : Mehrav Lalotra
Roll : 24052582
```

## **5. InputMismatchException**
```java
import java.util.InputMismatchException;
import java.util.Scanner;

public class InputMismatchExceptionDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Enter an integer: ");
            int number = scanner.nextInt();
            System.out.println("You entered: " + number);
        } catch (InputMismatchException e) {
            System.out.println("Error: Please enter a valid integer");
        }
        
        scanner.close();
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Enter an integer: abc
Error: Please enter a valid integer
Name : Mehrav Lalotra
Roll : 24052582
```

## **6. Multiple Catch Blocks**
```java
public class MultipleCatchDemo {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3};
        String str = "abc";
        
        try {
            System.out.println(numbers[5]);
            int num = Integer.parseInt(str);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught ArrayIndexOutOfBoundsException");
        } catch (NumberFormatException e) {
            System.out.println("Caught NumberFormatException");
        } catch (Exception e) {
            System.out.println("Caught general Exception");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught ArrayIndexOutOfBoundsException
Name : Mehrav Lalotra
Roll : 24052582
```

## **7. Catch Block Order Importance**
```java
public class CatchOrderDemo {
    public static void main(String[] args) {
        try {
            int[] arr = new int[5];
            arr[10] = 50;
        } catch (Exception e) {
            System.out.println("General Exception caught");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
General Exception caught
Name : Mehrav Lalotra
Roll : 24052582
```

## **8. Parent Exception Catch**
```java
public class ParentExceptionDemo {
    public static void main(String[] args) {
        try {
            String str = null;
            System.out.println(str.length());
        } catch (Exception e) {
            System.out.println("Parent Exception caught all child exceptions");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Parent Exception caught all child exceptions
Name : Mehrav Lalotra
Roll : 24052582
```

## **9. Exception Hierarchy**
```java
public class ExceptionHierarchyDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException caught");
        } catch (RuntimeException e) {
            System.out.println("RuntimeException caught");
        } catch (Exception e) {
            System.out.println("Exception caught");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
ArithmeticException caught
Name : Mehrav Lalotra
Roll : 24052582
```

## **10. Multi-Catch Block**
```java
public class MultiCatchDemo {
    public static void main(String[] args) {
        try {
            String str = null;
            int num = Integer.parseInt(str);
        } catch (NullPointerException | NumberFormatException e) {
            System.out.println("Caught multiple exceptions: " + e.getClass().getSimpleName());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught multiple exceptions: NullPointerException
Name : Mehrav Lalotra
Roll : 24052582
```

## **11. Finally Block with Exception**
```java
public class FinallyWithExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Exception occurred: Division by zero");
        } finally {
            System.out.println("Finally block executed");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Exception occurred: Division by zero
Finally block executed
Name : Mehrav Lalotra
Roll : 24052582
```

## **12. Finally with Return Statement**
```java
public class FinallyWithReturnDemo {
    public static int divide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException e) {
            System.out.println("Exception caught");
            return -1;
        } finally {
            System.out.println("Finally block executes before return");
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Result: " + divide(10, 0));
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Exception caught
Finally block executes before return
Result: -1
Name : Mehrav Lalotra
Roll : 24052582
```

## **13. Finally Without Exception**
```java
public class FinallyNoExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 2;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Exception occurred");
        } finally {
            System.out.println("Finally block executed even without exception");
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Result: 5
Finally block executed even without exception
Name : Mehrav Lalotra
Roll : 24052582
```

## **14. Finally Not Executing**
```java
public class FinallyNotExecuteDemo {
    public static void main(String[] args) {
        try {
            System.out.println("Before System.exit()");
            System.exit(0);
        } finally {
            System.out.println("This will not execute");
        }
    }
}
```

**Output:**
```
Before System.exit()
```

**Reason:** Finally block doesn't execute when `System.exit(0)` is called because it terminates the JVM immediately.

## **15. Throw Keyword**
```java
public class ThrowDemo {
    public static void validateAge(int age) {
        if (age < 18) {
            throw new ArithmeticException("Age must be 18 or above");
        } else {
            System.out.println("Age is valid");
        }
    }
    
    public static void main(String[] args) {
        try {
            validateAge(15);
        } catch (ArithmeticException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught exception: Age must be 18 or above
Name : Mehrav Lalotra
Roll : 24052582
```

## **16. Throws Declaration**
```java
import java.io.IOException;

public class ThrowsDemo {
    public static void readFile() throws IOException {
        throw new IOException("File not found");
    }
    
    public static void main(String[] args) {
        try {
            readFile();
        } catch (IOException e) {
            System.out.println("Caught checked exception: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught checked exception: File not found
Name : Mehrav Lalotra
Roll : 24052582
```

## **17. Throw vs Throws**
```java
import java.io.IOException;

public class ThrowVsThrowsDemo {
    public static void methodWithThrow() {
        throw new ArithmeticException("Explicit throw");
    }
    
    public static void methodWithThrows() throws IOException {
        throw new IOException("IO Exception thrown");
    }
    
    public static void main(String[] args) {
        try {
            methodWithThrow();
        } catch (ArithmeticException e) {
            System.out.println("Caught: " + e.getMessage());
        }
        
        try {
            methodWithThrows();
        } catch (IOException e) {
            System.out.println("Caught: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught: Explicit throw
Caught: IO Exception thrown
Name : Mehrav Lalotra
Roll : 24052582
```

## **18. Multiple Throws**
```java
import java.io.IOException;

public class MultipleThrowsDemo {
    public static void processFile(int option) throws IOException, ArithmeticException {
        if (option == 1) {
            throw new IOException("File error");
        } else {
            throw new ArithmeticException("Math error");
        }
    }
    
    public static void main(String[] args) {
        try {
            processFile(1);
        } catch (IOException | ArithmeticException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught exception: File error
Name : Mehrav Lalotra
Roll : 24052582
```

## **19. Custom Checked Exception**
```java
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

public class CustomCheckedExceptionDemo {
    public static void validateVotingAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age " + age + " is not valid for voting");
        }
        System.out.println("Valid age for voting");
    }
    
    public static void main(String[] args) {
        try {
            validateVotingAge(16);
        } catch (InvalidAgeException e) {
            System.out.println("Custom exception caught: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Custom exception caught: Age 16 is not valid for voting
Name : Mehrav Lalotra
Roll : 24052582
```

## **20. Custom Unchecked Exception**
```java
class InsufficientBalanceException extends RuntimeException {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}

public class CustomUncheckedExceptionDemo {
    public static void withdrawAmount(double balance, double amount) {
        if (amount > balance) {
            throw new InsufficientBalanceException("Insufficient balance. Available: " + balance);
        }
        System.out.println("Withdrawal successful");
    }
    
    public static void main(String[] args) {
        try {
            withdrawAmount(5000, 10000);
        } catch (InsufficientBalanceException e) {
            System.out.println("Custom unchecked exception: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Custom unchecked exception: Insufficient balance. Available: 5000.0
Name : Mehrav Lalotra
Roll : 24052582
```

## **21. Message in User-Defined Exception**
```java
class InvalidInputException extends Exception {
    public InvalidInputException(String message) {
        super("Custom Error: " + message);
    }
}

public class ExceptionWithMessageDemo {
    public static void processInput(String input) throws InvalidInputException {
        if (input == null || input.isEmpty()) {
            throw new InvalidInputException("Input cannot be empty");
        }
        System.out.println("Processing: " + input);
    }
    
    public static void main(String[] args) {
        try {
            processInput("");
        } catch (InvalidInputException e) {
            System.out.println(e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Custom Error: Input cannot be empty
Name : Mehrav Lalotra
Roll : 24052582
```

## **22. Exception Propagation**
```java
public class ExceptionPropagationDemo {
    public static void method1() {
        method2();
    }
    
    public static void method2() {
        method3();
    }
    
    public static void method3() {
        int result = 10 / 0;
    }
    
    public static void main(String[] args) {
        try {
            method1();
        } catch (ArithmeticException e) {
            System.out.println("Exception handled in main: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Exception handled in main: / by zero
Name : Mehrav Lalotra
Roll : 24052582
```

## **23. Intermediate Exception Handling**
```java
public class IntermediateExceptionHandling {
    public static void method1() {
        try {
            method2();
        } catch (ArithmeticException e) {
            System.out.println("Exception handled in method1: " + e.getMessage());
        }
    }
    
    public static void method2() {
        method3();
    }
    
    public static void method3() {
        int result = 10 / 0;
    }
    
    public static void main(String[] args) {
        method1();
        System.out.println("Program continues after handling");
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Exception handled in method1: / by zero
Program continues after handling
Name : Mehrav Lalotra
Roll : 24052582
```

## **24. Exception in Try and Finally**
```java
public class ExceptionInTryFinallyDemo {
    public static void main(String[] args) {
        try {
            System.out.println("In try block");
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Caught exception from try: " + e.getMessage());
        } finally {
            System.out.println("In finally block");
            String str = null;
            System.out.println(str.length());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
In try block
Caught exception from try: / by zero
In finally block
Exception in thread "main" java.lang.NullPointerException
```

## **25. Rethrowing Exception**
```java
public class RethrowExceptionDemo {
    public static void process() {
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Partially handled, now rethrowing");
            throw e;
        }
    }
    
    public static void main(String[] args) {
        try {
            process();
        } catch (ArithmeticException e) {
            System.out.println("Rethrown exception caught in main: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Partially handled, now rethrowing
Rethrown exception caught in main: / by zero
Name : Mehrav Lalotra
Roll : 24052582
```

## **26. Try-With-Resources**
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesDemo {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("IOException: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output (if file doesn't exist):**
```
IOException: test.txt (The system cannot find the file specified)
Name : Mehrav Lalotra
Roll : 24052582
```

## **27. Suppressed Exceptions**
```java
import java.io.FileInputStream;
import java.io.IOException;

class CustomResource implements AutoCloseable {
    public void use() {
        System.out.println("Using resource");
    }
    
    @Override
    public void close() throws IOException {
        System.out.println("Closing resource");
        throw new IOException("Exception during closing");
    }
}

public class SuppressedExceptionsDemo {
    public static void main(String[] args) {
        try (CustomResource resource = new CustomResource()) {
            resource.use();
            throw new ArithmeticException("Exception in try block");
        } catch (Exception e) {
            System.out.println("Primary exception: " + e.getMessage());
            Throwable[] suppressed = e.getSuppressed();
            for (Throwable t : suppressed) {
                System.out.println("Suppressed exception: " + t.getMessage());
            }
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Using resource
Closing resource
Primary exception: Exception in try block
Suppressed exception: Exception during closing
Name : Mehrav Lalotra
Roll : 24052582
```

## **28. Exception Chaining**
```java
public class ExceptionChainingDemo {
    public static void method1() {
        try {
            method2();
        } catch (ArithmeticException e) {
            RuntimeException re = new RuntimeException("Higher level exception");
            re.initCause(e);
            throw re;
        }
    }
    
    public static void method2() {
        throw new ArithmeticException("Original low level exception");
    }
    
    public static void main(String[] args) {
        try {
            method1();
        } catch (RuntimeException e) {
            System.out.println("Caught: " + e.getMessage());
            System.out.println("Original cause: " + e.getCause().getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught: Higher level exception
Original cause: Original low level exception
Name : Mehrav Lalotra
Roll : 24052582
```

## **29. Checked vs Unchecked Exceptions**
```java
import java.io.FileInputStream;
import java.io.IOException;

public class CheckedUncheckedDemo {
    public static void uncheckedExample() {
        int result = 10 / 0;
    }
    
    public static void checkedExample() throws IOException {
        FileInputStream fis = new FileInputStream("nonexistent.txt");
    }
    
    public static void main(String[] args) {
        try {
            uncheckedExample();
        } catch (ArithmeticException e) {
            System.out.println("Unchecked exception caught at runtime: " + e.getMessage());
        }
        
        try {
            checkedExample();
        } catch (IOException e) {
            System.out.println("Checked exception must be handled: " + e.getMessage());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Unchecked exception caught at runtime: / by zero
Checked exception must be handled: nonexistent.txt (The system cannot find the file specified)
Name : Mehrav Lalotra
Roll : 24052582
```

## **30. Catching Throwable**
```java
public class CatchThrowableDemo {
    public static void method1() {
        throw new OutOfMemoryError("Simulated JVM error");
    }
    
    public static void method2() {
        throw new RuntimeException("Runtime exception");
    }
    
    public static void main(String[] args) {
        try {
            method1();
        } catch (Throwable t) {
            System.out.println("Caught Throwable: " + t.getClass().getSimpleName());
        }
        
        try {
            method2();
        } catch (Throwable t) {
            System.out.println("Caught Throwable: " + t.getClass().getSimpleName());
        }
        
        System.out.println("Name : Mehrav Lalotra");
        System.out.println("Roll : 24052582");
    }
}
```

**Output:**
```
Caught Throwable: OutOfMemoryError
Caught Throwable: RuntimeException
Name : Mehrav Lalotra
Roll : 24052582
```

