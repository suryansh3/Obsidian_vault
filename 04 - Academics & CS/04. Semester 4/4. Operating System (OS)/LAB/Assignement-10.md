# Name : Nitish Misra
## Roll : 24158115
### 1. 

```java
class EvenOdd {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t1 = new Thread(() -> {
            for (int i = 2; i <= 6; i += 2) System.out.println("Even: " + i);
        });
        Thread t2 = new Thread(() -> {
            for (int i = 1; i <= 5; i += 2) System.out.println("Odd: " + i);
        });
        t1.start();
        t2.start();
    }
}
```

**Output:**
```
Name : Nitish Misra
Roll : 24158115
Even: 2
Odd: 1
Even: 4
Odd: 3
Even: 6
Odd: 5
```

### 2. 

```java
class ThreadEx extends Thread {
    public void run() { System.out.println("From Thread class"); }
}
class RunnableEx implements Runnable {
    public void run() { System.out.println("From Runnable interface"); }
}
class Q2 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        new ThreadEx().start();
        new Thread(new RunnableEx()).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
From Thread class
From Runnable interface
```

### 3. 

```java
class Q3 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        new Thread(() -> printMsg("T1", 100)).start();
        new Thread(() -> printMsg("T2", 200)).start();
        new Thread(() -> printMsg("T3", 300)).start();
    }
    static void printMsg(String name, int delay) {
        try {
            Thread.sleep(delay);
            System.out.println(name + " executed");
        } catch (InterruptedException e) {}
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1 executed
T2 executed
T3 executed
```

### 4. 

```java
class Q4 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        for (int i = 1; i <= 5; i++) {
            new Thread(() -> {
                Thread c = Thread.currentThread();
                System.out.println("Name: " + c.getName() + " | ID: " + c.getId() + " | Priority: " + c.getPriority());
            }).start();
        }
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Name: Thread-0 | ID: 20 | Priority: 5
Name: Thread-2 | ID: 22 | Priority: 5
Name: Thread-1 | ID: 21 | Priority: 5
Name: Thread-4 | ID: 24 | Priority: 5
Name: Thread-3 | ID: 23 | Priority: 5
```

### 5. 

```java
import .util.Scanner;
class Q5 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        int n = 3; 
        for (int i = 1; i <= n; i++) {
            int taskNum = i;
            new Thread(() -> System.out.println("Executing Task " + taskNum)).start();
        }
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Executing Task 1
Executing Task 3
Executing Task 2
```

### 6. 

```java
class Q6 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> {
            try { Thread.sleep(50); } catch (Exception e) {}
        });
        System.out.println(t.getState());
        t.start();
        System.out.println(t.getState());
        t.join();
        System.out.println(t.getState());
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
NEW
RUNNABLE
TERMINATED
```

### 7. 
```java
class Q7 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread target = new Thread(() -> {
            try { Thread.sleep(100); } catch (Exception e) {}
        });
        Thread monitor = new Thread(() -> {
            Thread.State state = target.getState();
            System.out.println("State: " + state);
            while (state != Thread.State.TERMINATED) {
                Thread.State newState = target.getState();
                if (newState != state) {
                    System.out.println("State changed to: " + newState);
                    state = newState;
                }
            }
        });
        monitor.start();
        target.start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
State: NEW
State changed to: RUNNABLE
State changed to: TIMED_WAITING
State changed to: TERMINATED
```
### 8. 

```java
class Q8 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> System.out.println("Running..."));
        System.out.println("1: " + t.getState());
        t.start();
        System.out.println("2: " + t.getState());
        t.join();
        System.out.println("3: " + t.getState());
    }
}
```

**Output:**
```
Name : Nitish Misra
Roll : 24158115
1: NEW
2: RUNNABLE
Running...
3: TERMINATED
```

### 9. Priority Scheduling
```java
class Q9 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t1 = new Thread(() -> System.out.println("Low priority"));
        Thread t2 = new Thread(() -> System.out.println("Norm priority"));
        Thread t3 = new Thread(() -> System.out.println("Max priority"));
        t1.setPriority(Thread.MIN_PRIORITY);
        t2.setPriority(Thread.NORM_PRIORITY);
        t3.setPriority(Thread.MAX_PRIORITY);
        t1.start();
        t2.start();
        t3.start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Max priority
Norm priority
Low priority
```

### 10. 

```java
class Q10 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        for (int i = 1; i <= 3; i++) {
            int task = i;
            System.out.println("Task " + task + " arrived.");
            new Thread(() -> System.out.println("Task " + task + " executed.")).start();
            Thread.sleep(100);
        }
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Task 1 arrived.
Task 1 executed.
Task 2 arrived.
Task 2 executed.
Task 3 arrived.
Task 3 executed.
```

### 11. 

```java
class Q11 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t1 = new Thread(() -> System.out.println("Thread name: " + Thread.currentThread().getName()));
        t1.run();
        t1.start();
    }
}
```

**Output:**
```
Name : Nitish Misra
Roll : 24158115
Thread name: main
Thread name: Thread-0
```

### 12. 

```java
class Q12 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Runnable r = () -> {
            for (int i = 1; i <= 2; i++) {
                System.out.println(Thread.currentThread().getName() + ": " + i);
                try { Thread.sleep(50); } catch (Exception e) {}
            }
        };
        new Thread(r, "T1").start();
        new Thread(r, "T2").start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1: 1
T2: 1
T2: 2
T1: 2
```

### 13. 

```java
class Q13 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> {
            try { Thread.sleep(100); } catch (Exception e) {}
            System.out.println("Child thread finished.");
        });
        t.start();
        t.join();
        System.out.println("Main thread proceeding.");
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Child thread finished.
Main thread proceeding.
```

### 14. 

```java
class Q14 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> {
            System.out.println("Initial: " + Thread.currentThread().getName());
            Thread.currentThread().setName("Worker-1");
            System.out.println("Changed: " + Thread.currentThread().getName());
        });
        t.start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Initial: Thread-0
Changed: Worker-1
```

### 15.

```java
class Q15 {
    static int count = 0;
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Runnable r = () -> { for (int i = 0; i < 10000; i++) count++; };
        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Total count: " + count);
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Total count: 13421
```

### 16. 

```java
class Q16 {
    static int count = 0;
    static synchronized void increment() { count++; }
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Runnable r = () -> { for (int i = 0; i < 10000; i++) increment(); };
        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Total count: " + count);
    }
}
```

**Output:**
```
Name : Nitish Misra
Roll : 24158115
Total count: 20000
```

### 17. 

```java
class Q17 {
    static int count = 0;
    static final Object lock = new Object();
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Runnable r = () -> { 
            for (int i = 0; i < 10000; i++) {
                synchronized(lock) { count++; }
            }
        };
        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Total count: " + count);
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Total count: 20000
```

### 18. 

```java
class Bank {
    int balance = 100;
    synchronized void withdraw(int amt, String user) {
        if (balance >= amt) {
            System.out.println(user + " withdrawing " + amt);
            balance -= amt;
            System.out.println(user + " success. Balance: " + balance);
        } else {
            System.out.println(user + " failed. Insufficient funds.");
        }
    }
}
class Q18 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Bank b = new Bank();
        new Thread(() -> b.withdraw(80, "User1")).start();
        new Thread(() -> b.withdraw(80, "User2")).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
User1 withdrawing 80
User1 success. Balance: 20
User2 failed. Insufficient funds.
```

### 19.

```java
class Shared {
    static synchronized void doTask(String name) {
        System.out.println(name + " executing");
        try { Thread.sleep(100); } catch (Exception e) {}
    }
}
class Q19 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Shared obj1 = new Shared();
        Shared obj2 = new Shared();
        new Thread(() -> obj1.doTask("T1")).start();
        new Thread(() -> obj2.doTask("T2")).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1 executing
T2 executing
```

### 20.

```java
class SyncDemo {
    synchronized void objectSync() {
        System.out.println("Object sync: " + Thread.currentThread().getName());
        try { Thread.sleep(100); } catch (Exception e) {}
    }
    static synchronized void classSync() {
        System.out.println("Class sync: " + Thread.currentThread().getName());
        try { Thread.sleep(100); } catch (Exception e) {}
    }
}
class Q20 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        SyncDemo obj = new SyncDemo();
        new Thread(() -> obj.objectSync(), "T1").start();
        new Thread(() -> SyncDemo.classSync(), "T2").start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Object sync: T1
Class sync: T2
```

### 21. 

```java
class Q21 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Object lock1 = new Object();
        Object lock2 = new Object();
        new Thread(() -> {
            synchronized(lock1) {
                System.out.println("T1 holding Lock1");
                try { Thread.sleep(50); } catch (Exception e) {}
                synchronized(lock2) { System.out.println("T1 holding Lock2"); }
            }
        }).start();
        new Thread(() -> {
            synchronized(lock2) {
                System.out.println("T2 holding Lock2");
                try { Thread.sleep(50); } catch (Exception e) {}
                synchronized(lock1) { System.out.println("T2 holding Lock1"); }
            }
        }).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1 holding Lock1
T2 holding Lock2
```
### 22. 

```java
class Q22 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Object lock1 = new Object();
        Object lock2 = new Object();
        new Thread(() -> {
            synchronized(lock1) {
                System.out.println("T1 holding Lock1");
                try { Thread.sleep(50); } catch (Exception e) {}
                synchronized(lock2) { System.out.println("T1 acquired Lock2"); }
            }
        }).start();
        new Thread(() -> {
            synchronized(lock1) {
                System.out.println("T2 holding Lock1");
                try { Thread.sleep(50); } catch (Exception e) {}
                synchronized(lock2) { System.out.println("T2 acquired Lock2"); }
            }
        }).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1 holding Lock1
T1 acquired Lock2
T2 holding Lock1
T2 acquired Lock2
```

### 23. 

```java
class Q23 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        int[] buffer = new int[1];
        Object lock = new Object();
        new Thread(() -> {
            synchronized(lock) {
                buffer[0] = 100;
                System.out.println("Produced: 100");
                lock.notify();
            }
        }).start();
        new Thread(() -> {
            synchronized(lock) {
                try { if (buffer[0] == 0) lock.wait(); } catch (Exception e) {}
                System.out.println("Consumed: " + buffer[0]);
            }
        }).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Produced: 100
Consumed: 100
```

### 24. 

```java
class Account {
    int balance = 0;
    synchronized void withdraw(int amt) {
        System.out.println("Attempting withdraw.");
        while (balance < amt) {
            try { wait(); } catch (Exception e) {}
        }
        balance -= amt;
        System.out.println("Withdrawal successful.");
    }
    synchronized void deposit(int amt) {
        balance += amt;
        System.out.println("Deposited: " + amt);
        notify();
    }
}
class Q24 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Account acc = new Account();
        new Thread(() -> acc.withdraw(100)).start();
        new Thread(() -> {
            try { Thread.sleep(100); } catch (Exception e) {}
            acc.deposit(100);
        }).start();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Attempting withdraw.
Deposited: 100
Withdrawal successful.
```

### 25. 

```java
class Q25 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Object lock = new Object();
        Runnable r = () -> {
            synchronized(lock) {
                try {
                    System.out.println(Thread.currentThread().getName() + " waiting.");
                    lock.wait();
                    System.out.println(Thread.currentThread().getName() + " resumed.");
                } catch (Exception e) {}
            }
        };
        new Thread(r, "T1").start();
        new Thread(r, "T2").start();
        Thread.sleep(100);
        synchronized(lock) {
            System.out.println("Notifying all...");
            lock.notifyAll();
        }
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
T1 waiting.
T2 waiting.
Notifying all...
T2 resumed.
T1 resumed.
```

### 26. 

```java
class Q26 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread daemon = new Thread(() -> {
            while (true) {
                System.out.println("Daemon running...");
                try { Thread.sleep(50); } catch (Exception e) {}
            }
        });
        daemon.setDaemon(true);
        daemon.start();
        try { Thread.sleep(120); } catch (Exception e) {}
        System.out.println("Main terminating.");
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Daemon running...
Daemon running...
Daemon running...
Main terminating.
```

### 27. 

```java
class Q27 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                System.out.println("Thread was interrupted!");
            }
        });
        t.start();
        Thread.sleep(100);
        t.interrupt();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Thread was interrupted!
```
### 28. 

```java
class Q28 {
    public static void main(String[] args) throws Exception {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        Thread t = new Thread(() -> {
            while (!Thread.currentThread().isInterrupted()) {}
            System.out.println("Loop broken by interrupt.");
        });
        t.start();
        Thread.sleep(50);
        t.interrupt();
    }
}
```

**Output:**
```
Name : Nitish Misra
Roll : 24158115
Loop broken by interrupt.
```

### 29. 

```java
class Reentrant {
    synchronized void methodA() {
        System.out.println("Inside Method A");
        methodB();
    }
    synchronized void methodB() {
        System.out.println("Inside Method B");
    }
}
class Q29 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        new Reentrant().methodA();
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Inside Method A
Inside Method B
```

### 30. 

```java
class Q30 {
    public static void main(String[] args) {
        System.out.println("Name : Nitish Misra\nRoll : 24158115");
        for (int i = 1; i <= 3; i++) {
            int part = i;
            new Thread(() -> {
                System.out.println("Downloading part " + part + "...");
                try { Thread.sleep((int)(Math.random() * 100)); } catch (Exception e) {}
                System.out.println("Part " + part + " complete.");
            }).start();
        }
    }
}
```

**Output:**

```
Name : Nitish Misra
Roll : 24158115
Downloading part 1...
Downloading part 2...
Downloading part 3...
Part 2 complete.
Part 1 complete.
Part 3 complete.
```
