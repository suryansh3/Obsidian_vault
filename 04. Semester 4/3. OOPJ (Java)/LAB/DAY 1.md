
---

##  Java Programs

### 1. Print name, university, branch

```java
class Main {
    public static void main(String[] args) {
        System.out.println("Name: Suryansh Mithu");
        System.out.println("ROll: 24155060")
        System.out.println("University: KIIT University");
        System.out.println("Branch: CSE AIML");
    }
}
```

---

### 2. Print pattern

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

---

### 3. Arithmetic operations

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        int a = 10, b = 5;
        System.out.println("Sum: " + (a + b));
        System.out.println("Difference: " + (a - b));
        System.out.println("Product: " + (a * b));
        System.out.println("Quotient: " + (a / b));
    }
}
```

---

### 4. Display output

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");    
        System.out.println("\"Hello Java\"");
        System.out.println("Welcome to Programming");
    }
}
```

---

### 5. ASCII value

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
    char ch = 'A';
    int ascii = (int) ch;
    System.out.println("ASCII value of " + ch + " is " + ascii);
    }
}
```

---

### 6. Input name and age

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
	System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine(); //next scans till you get the next white      space meaning if you write "Suryansh Mithu" it will show error but in         nextLine is use to scan till \n hence used nextLine instead of next in        scanner.
        int age = sc.nextInt();
        System.out.println("Hello " + name + ", your age is " + age + ".");
    }
}
```

---

### 7. Area of circle

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        double r = sc.nextDouble();
        double area = Math.PI * r * r;
        System.out.println("Area of circle: " + area);
    }
}
```

---

### 8. Celsius to Fahrenheit

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        double c = sc.nextDouble();
        double f = (c * 9/5) + 32;
        System.out.println("Fahrenheit: " + f);
    }
}
```

---

### 9. Swap using third variable

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        int a = 10, b = 20, temp;
        temp = a;
        a = b;
        b = temp;
        System.out.println("a = " + a + ", b = " + b);
    }
}
```

---

### 10. Swap without third variable

```java
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        int a = 10, b = 20;
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("a = " + a + ", b = " + b);
    }
}
```

---

### 11. Even or odd

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n % 2 == 0)
            System.out.println("Even");
        else
            System.out.println("Odd");
    }
}
```

---

### 12. Larger of two numbers

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        if (a > b)
            System.out.println(a + " is larger");
        else
            System.out.println(b + " is larger");
    }
}
```

---

### 13. Divisible by 3 and 5

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n % 3 == 0 && n % 5 == 0)
            System.out.println("Divisible by both 3 and 5");
        else
            System.out.println("Not divisible by both");
    }
}
```

---

### 14. Simple interest

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        double p = sc.nextDouble(), r = sc.nextDouble(), t = sc.nextDouble();
        double si = (p * r * t) / 100;
        System.out.println("Simple Interest: " + si);
    }
}
```

---

### 15. Marks of 5 subjects

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int total = 0;
        for (int i = 0; i < 5; i++) {
            total += sc.nextInt();
        }
        double percentage = total / 5.0;
        System.out.println("Total: " + total);
        System.out.println("Percentage: " + percentage);
    }
}
```

---

### 16. Leap year

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
            System.out.println("Leap Year");
        else
            System.out.println("Not a Leap Year");
    }
}
```

---

### 17. Factorial using loop

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        System.out.println("Factorial: " + fact);
    }
}
```

---

### 18. Numbers divisible by 7

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 1; i <= N; i++) {
            if (i % 7 == 0)
                System.out.println(i);
        }
    }
}
```

---

### 19. Reverse integer

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), rev = 0;
        while (n != 0) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        System.out.println("Reversed: " + rev);
    }
}
```

---

### 20. Largest among three numbers

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
    System.out.println("Name: Suryansh Mithu");
    System.out.println("ROll: 24155060");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        if (a >= b && a >= c)
            System.out.println("Largest: " + a);
        else if (b >= a && b >= c)
            System.out.println("Largest: " + b);
        else
            System.out.println("Largest: " + c);
    }
}
```

