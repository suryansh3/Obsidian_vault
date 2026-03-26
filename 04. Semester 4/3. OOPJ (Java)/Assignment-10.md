# Name : Utkarsh Dwivedi
## Roll : 24051673
### Program 1 – FileCopy.java

```java
import java.io.*;

public class FileCopy {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter the source file name - ");
            String src = br.readLine();
            System.out.print("Enter the destination file name - ");
            String dest = br.readLine();

            FileReader fr = new FileReader(src);
            FileWriter fw = new FileWriter(dest);
            int ch;
            while ((ch = fr.read()) != -1) {
                fw.write(ch);
            }
            fr.close();
            fw.close();
            System.out.println("File Copied using character stream");

            FileInputStream fis = new FileInputStream(src);
            FileOutputStream fos = new FileOutputStream(dest + "_byte");
            int b;
            while ((b = fis.read()) != -1) {
                fos.write(b);
            }
            fis.close();
            fos.close();
            System.out.println("File Copied using byte stream to " + dest + "_byte");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

**Output:**

```
Enter the source file name - sourcefile.txt
Enter the destination file name - destinationfile.txt
File Copied using character stream
File Copied using byte stream to destinationfile.txt_byte
```

---

### Program 2 – CircleArea.java

```java
import java.io.*;

public class CircleArea {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the radius of circle: ");
        double radius = Double.parseDouble(br.readLine());
        double area = Math.PI * radius * radius;
        System.out.println("Area of circle = " + area);
    }
}
```

**Output:**

```
Enter the radius of circle: 7.5
Area of circle = 176.71458676442586
```

---

### Program 3 – FileStats.java

```java
import java.io.*;

public class FileStats {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the file name: ");
        String fileName = br.readLine();

        FileReader fr = new FileReader(fileName);
        BufferedReader fileBr = new BufferedReader(fr);

        int charCount = 0, lineCount = 0, wordCount = 0;
        String line;
        while ((line = fileBr.readLine()) != null) {
            lineCount++;
            charCount += line.length();
            String[] words = line.trim().split("\\s+");
            if (line.trim().length() > 0) {
                wordCount += words.length;
            }
        }
        fileBr.close();

        System.out.println("No. of characters: " + charCount);
        System.out.println("No. of lines: " + lineCount);
        System.out.println("No. of words: " + wordCount);
    }
}
```

**Output: 

```
Enter the file name: sample.txt
No. of characters: 87
No. of lines: 3
No. of words: 15
```

---

### Program 4 – InterThreadCommunication.java

```java
class SharedResource {
    private int data;
    private boolean available = false;

    public synchronized void produce(int value) throws InterruptedException {
        while (available) {
            wait();
        }
        data = value;
        available = true;
        System.out.println("Produced: " + data);
        notify();
    }

    public synchronized void consume() throws InterruptedException {
        while (!available) {
            wait();
        }
        System.out.println("Consumed: " + data);
        available = false;
        notify();
    }
}

public class InterThreadCommunication {
    public static void main(String[] args) {
        SharedResource resource = new SharedResource();

        Thread producer = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                try {
                    resource.produce(i);
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread consumer = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                try {
                    resource.consume();
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        producer.start();
        consumer.start();
    }
}
```

**Output:**

```
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4
Produced: 5
Consumed: 5
```