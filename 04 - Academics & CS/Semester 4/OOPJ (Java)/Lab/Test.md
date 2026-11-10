---
course: "OOPJ (Java)"
semester: 4
tags:
  - course/oopj-java
up: "[[OOPJ (Java)]]"
---

### **SET - A**

**1. Paragraph Comparator & Custom Exception**
```
import java.util.Scanner;
class TooLargeStringException extends Exception {
    public TooLargeStringException(String message) {
        super(message);
    }
}
public class ParagraphCompare {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Paragraph 1:");
        String p1 = sc.nextLine();
        System.out.println("Enter Paragraph 2:");
        String p2 = sc.nextLine();
        try {
            if (p1.length() > 10000 || p2.length() > 10000) {
                throw new TooLargeStringException("Text exceeds 10,000 characters!");
            }
            String[] words1 = p1.split("\\s+");
            String[] words2 = p2.split("\\s+");
            StringBuffer differences = new StringBuffer("Different words: \n");
            int maxLength = Math.max(words1.length, words2.length);
            for (int i = 0; i < maxLength; i++) {
                String w1 = (i < words1.length) ? words1[i] : "";
                String w2 = (i < words2.length) ? words2[i] : "";
                if (!w1.equals(w2)) {
                    differences.append(w1).append(" vs ").append(w2).append("\n");
                }
            }
            System.out.println(differences.toString());
        } catch (TooLargeStringException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
**2. Modular File Compression Tool**

```
package compression;
interface Compressor {
    void compress();
    void decompress();
}
class ZipCompressor implements Compressor {
    public void compress() { System.out.println("Compressing ZIP..."); }
    public void decompress() { System.out.println("Decompressing ZIP..."); }
}
class RarCompressor implements Compressor {
    public void compress() { System.out.println("Compressing RAR..."); }
    public void decompress() { System.out.println("Decompressing RAR..."); }
}
public class CompressionApp {
    public static void main(String[] args) {
        // C. Anonymous inner class
        Compressor tarCompressor = new Compressor() {
            public void compress() { System.out.println("Compressing TAR..."); }
            public void decompress() { System.out.println("Decompressing TAR..."); }
        };
        // D. Dynamic method lookup
        Compressor[] tools = { new ZipCompressor(), new RarCompressor(), tarCompressor };
            for (Compressor tool : tools) {
            tool.compress(); 
            tool.decompress();
            System.out.println("---");
        }
    }
}
```
---
### **SET - B**

**1. Multi-threaded Ticket Booking System**
```
class TicketPool {
    private int seats = 100;
    public synchronized void bookTicket(int seatsNeeded, String user) {
        System.out.println(user + " is trying to book " + seatsNeeded + " seats.");
        while (seats < seatsNeeded) {
            try {
                System.out.println(user + " is waiting for cancellations...");
                wait(); // Wait for canceled tickets
            } catch (InterruptedException e) { }
        }
        seats -= seatsNeeded;
        System.out.println(user + " successfully booked! Seats left: " + seats);
    }
    public synchronized void cancelTicket(int seatsCanceled) {
        seats += seatsCanceled;
        System.out.println(seatsCanceled + " seats canceled. Total seats: " + seats);
        notifyAll(); // Notify waiting users
    }
}
public class TicketSystem {
    public static void main(String[] args) {
        TicketPool pool = new TicketPool();

        Thread t1 = new Thread(() -> pool.bookTicket(80, "User A"));
        Thread t2 = new Thread(() -> pool.bookTicket(40, "User B"));
        Thread t3 = new Thread(() -> {
            try { Thread.sleep(1000); } catch (Exception e) {}
            pool.cancelTicket(30);
        });
        // Priority-based allocation
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);
        t1.start(); t2.start(); t3.start();
    }
}
```

**2. File Search and Modification**
```
import java.io.*;
import java.util.Scanner;
public class FileModifier {
    public static void main(String[] args) {
        String filename = "sample.txt";
        // Create a dummy file for testing
        try (FileWriter fw = new FileWriter(filename)) {
            fw.write("Java is fun. Let us learn java programming.");
        } catch (IOException e) {}
        try (Scanner sc = new Scanner(System.in);
             BufferedReader br = new BufferedReader(new FileReader(filename))) {
            System.out.print("Enter keyword to capitalize: ");
            String keyword = sc.nextLine();
            StringBuilder modifiedText = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                // Modify text
                modifiedText.append(line.replaceAll("(?i)" + keyword, keyword.toUpperCase())).append("\n");
            }
            // Using valueOf() and toString()
            String result = String.valueOf(modifiedText);
            System.out.println("\nModified Content:\n" + result.toString());
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
```
---
### **SET - C**

**1. Basic Swing Text Editor**
```
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
public class TextEditor {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Basic Editor");
        JTextArea textArea = new JTextArea();
        JButton saveBtn = new JButton("Save"), loadBtn = new JButton("Load"), clearBtn = new JButton("Clear");
        // ActionListeners
        saveBtn.addActionListener(e -> {
            try (FileWriter fw = new FileWriter("editor_data.txt")) {
                fw.write(textArea.getText());
            } catch (IOException ex) { }
        });
        loadBtn.addActionListener(e -> {
            try (BufferedReader br = new BufferedReader(new FileReader("editor_data.txt"))) {
                textArea.read(br, null);
            } catch (IOException ex) { }
        });
        clearBtn.addActionListener(e -> textArea.setText(""));
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(saveBtn); buttonPanel.add(loadBtn); buttonPanel.add(clearBtn);
        frame.add(new JScrollPane(textArea), BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);
        // Adapter class for window closing
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.out.println("Closing Editor...");
                System.exit(0);
            }
        });
        frame.setSize(500, 400);
        frame.setVisible(true);
    }
}
```
**2. Exception Handling & Stream Operations**
```
import java.io.*;
class InvalidNumberException extends Exception {
    public InvalidNumberException(String msg) { super(msg); }
}
public class StreamOperations {
    public static void main(String[] args) {
        String file = "data.bin";
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             DataOutputStream dos = new DataOutputStream(new FileOutputStream(file))) {
            System.out.print("Enter an integer: ");
            int num = Integer.parseInt(br.readLine());
            if (num < 0) {
                throw new InvalidNumberException("Negative numbers are not allowed!");
            }
            dos.writeInt(num);
            System.out.println("Number saved to file.");
        } catch (InvalidNumberException | NumberFormatException | IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        try (DataInputStream dis = new DataInputStream(new FileInputStream(file))) {
            int readNum = dis.readInt();
            System.out.println("Read from file: " + readNum);
        } catch (IOException e) {
        }
    }
}
```
---
### **SET - D**

**1. Multilevel Inheritance Hierarchy**
```
class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    void displayDetails() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
class Faculty extends Person {
    String department;
    double salary;
    Faculty(String name, int age, String department, double salary) {
        super(name, age); 
        this.department = department;
        this.salary = salary;
    }
    @Override
    void displayDetails() {
        super.displayDetails(); 
        System.out.println("Dept: " + department + ", Salary: $" + salary);
    }
}
class Professor extends Faculty {
    String researchArea;
    int numberOfPublications;
    Professor(String name, int age, String dept, double sal, String research, int pubs) {
        super(name, age, dept, sal); 
        this.researchArea = research;
        this.numberOfPublications = pubs;
    }
    @Override
    void displayDetails() {
        super.displayDetails(); // Method overriding using super
        System.out.println("Research Area: " + researchArea + ", Publications: " + numberOfPublications);
    }
}
public class UniversitySystem {
    public static void main(String[] args) {
        Person p = new Professor("Alice Smith", 45, "Computer Science", 120000, "AI & ML", 32);       
        // Calls the overridden method in Professor dynamically
        p.displayDetails(); 
    }
}
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[OOPJ (Java)]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/OOPJ (Java)/Lab/Test -LAB|Test -LAB]] · **Next:** -
> **Related:** [[Data Structures]] · [[Operating Systems]] · [[DBMS]]
<!-- connections:end -->
