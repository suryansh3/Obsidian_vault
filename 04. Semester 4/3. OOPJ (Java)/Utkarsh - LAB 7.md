# Name : Utkarsh Dwivedi
# Roll : 24051673
## 1.

```java
class CheckArgument extends Exception {
    public CheckArgument(String msg) {
        super(msg);
    }
}

public class Question1 {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi | Roll : 24051673\n");
        try {
            if (args.length < 4) {
                [cite_start]throw new CheckArgument("CheckArgument"); [cite: 2]
            }
            int sum = 0;
            for (String arg : args) {
                int num = Integer.parseInt(arg);
                [cite_start]sum += (num * num); [cite: 2]
            }
            System.out.println("Output: " + sum);
        } catch (CheckArgument e) {
            [cite_start]System.out.println("Exception occurred - " + e.getMessage()); [cite: 5]
        }
    }
}

```

**Output :**

* **Command:** `java Question1 4 3 2 1`
```text
Name : Utkarsh Dwivedi | Roll : 24051673
Output: 30

```


* **Command:** `java Question1 4 3 2`
```text
Name : Utkarsh Dwivedi | Roll : 24051673
Exception occurred - CheckArgument

```



---

## 2. 

```java
interface Permutation {
    long calculateNPR(int n, int r);
}

interface Combination {
    long calculateNCR(int n, int r);
}

[cite_start]interface NPRnNCR extends Permutation, Combination {} [cite: 6]

[cite_start]class MathOperations implements NPRnNCR { [cite: 7]
    private long fact(int num) {
        long f = 1;
        for (int i = 1; i <= num; i++) f *= i;
        return f;
    }

    public long calculateNPR(int n, int r) {
        return fact(n) / fact(n - r);
    }

    public long calculateNCR(int n, int r) {
        return fact(n) / (fact(r) * fact(n - r));
    }
}

public class Question2 {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi | Roll : 24051673\n");
        [cite_start]MathOperations obj = new MathOperations(); [cite: 8]
        System.out.println("5P2 = " + obj.calculateNPR(5, 2));
        System.out.println("5C2 = " + obj.calculateNCR(5, 2));
    }
}

```

**Output:**

```text
Name : Utkarsh Dwivedi | Roll : 24051673

5P2 = 20
5C2 = 10

```

---

## 3. 

```java
class Time {
    [cite_start]int hr, min, sec; [cite: 9]

    Time() { hr = min = sec = 0; [cite_start]} [cite: 9]
    
    [cite_start]Time(int h, int m, int s) { [cite: 9]
        this.hr = h;
        this.min = m;
        this.sec = s;
    }

    [cite_start]Time add(Time t) { [cite: 10]
        Time res = new Time();
        int totalSec = this.sec + t.sec;
        res.sec = totalSec % 60;
        
        int totalMin = this.min + t.min + (totalSec / 60);
        res.min = totalMin % 60;
        
        res.hr = this.hr + t.hr + (totalMin / 60);
        return res;
    }

    [cite_start]void display() { [cite: 10]
        System.out.printf("%02d:%02d:%02d\n", hr, min, sec);
    }
}

public class Question3 {
    public static void main(String[] args) {
        System.out.println("Name : Utkarsh Dwivedi | Roll : 24051673\n");
        Time t1 = new Time(2, 45, 50);
        Time t2 = new Time(1, 20, 20);
        [cite_start]Time result = t1.add(t2); [cite: 11]
        
        System.out.print("Time 1: "); t1.display();
        System.out.print("Time 2: "); t2.display();
        System.out.print("Added Time: "); result.display();
    }
}

```

**Output:**

```text
Name : Utkarsh Dwivedi | Roll : 24051673

Time 1: 02:45:50
Time 2: 01:20:20
Added Time: 04:06:10

```

---

## 4. 

```java
class QUEUE {
    [cite_start]int[] arr; [cite: 14]
    [cite_start]int FRONT, REAR; [cite: 14]

    QUEUE() { this(5); [cite_start]} [cite: 16]

    [cite_start]QUEUE(int size) { [cite: 17]
        arr = new int[size];
        FRONT = REAR = -1;
    }

    boolean isFull() { return REAR == arr.length - 1; [cite_start]} [cite: 21]
    boolean isEmpty() { return FRONT == -1 || FRONT > REAR; [cite_start]} [cite: 20]

    [cite_start]void insert(int x) { [cite: 18]
        if (isFull()) {
            System.out.println("Queue Full");
            return;
        }
        if (FRONT == -1) FRONT = 0;
        arr[++REAR] = x;
    }

    [cite_start]int del() { [cite: 19]
        if (isEmpty()) {
            System.out.println("Queue Empty");
            return -1;
        }
        return arr[FRONT++];
    }
}

public class Question4 {
    [cite_start]public static void main(String[] args) { [cite: 22]
        System.out.println("Name : Utkarsh Dwivedi | Roll : 24051673\n");
        QUEUE q = new QUEUE(3);
        q.insert(10);
        q.insert(20);
        System.out.println("Deleted: " + q.del());
        System.out.println("Deleted: " + q.del());
    }
}

```

**Output:**

```text
Name : Utkarsh Dwivedi | Roll : 24051673

Deleted: 10
Deleted: 20

```

---

## 5. 

```java
class STACK {
    [cite_start]int[] arr; [cite: 25]
    [cite_start]int TOP; [cite: 25]

    STACK() { this(5); [cite_start]} [cite: 27]

    [cite_start]STACK(int size) { [cite: 28]
        arr = new int[size];
        TOP = -1;
    }

    boolean isFull() { return TOP == arr.length - 1; [cite_start]} [cite: 31]
    boolean isEmpty() { return TOP == -1; [cite_start]} [cite: 31]

    [cite_start]void insert(int x) { [cite: 29]
        if (isFull()) {
            System.out.println("Stack Full");
            return;
        }
        arr[++TOP] = x;
    }

    [cite_start]int del() { [cite: 30]
        if (isEmpty()) {
            System.out.println("Stack Empty");
            return -1;
        }
        return arr[TOP--];
    }
}

public class Question5 {
    [cite_start]public static void main(String[] args) { [cite: 33]
        System.out.println("Name : Utkarsh Dwivedi | Roll : 24051673\n");
        STACK s = new STACK(3);
        s.insert(50);
        s.insert(100);
        System.out.println("Popped: " + s.del());
        System.out.println("Popped: " + s.del());
    }
}

```

**Output:**

```text
Name : Utkarsh Dwivedi | Roll : 24051673

Popped: 100
Popped: 50

```
