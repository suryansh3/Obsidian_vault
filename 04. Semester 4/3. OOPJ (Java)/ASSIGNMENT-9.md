# Name: Nitish Mishra
# Roll: 24158115

### 1. System.out, System.err, and System.in Demonstration

```java
public class StandardStreamsDemo {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        System.out.println("This is a message from System.out");
        System.err.println("This is an error message from System.err");
        
        System.out.print("Enter a single character for System.in: ");
        int input = System.in.read();
        System.out.println("You entered: " + (char) input);
    }
}
```

**Console Output:**


```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" StandardStreamsDemo
Name: Nitish Mishra
Roll: 24158115
This is a message from System.out
This is an error message from System.err
Enter a single character for System.in: X
You entered: X

Process finished with exit code 0
```

---

### 2. Read Single Character and Display ASCII

```Java

public class SingleCharReader {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        System.out.print("Enter a single character: ");
        int data = System.in.read();
        
        System.out.println("ASCII value: " + data);
        System.out.println("Character representation: " + (char) data);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" SingleCharReader
Name: Nitish Mishra
Roll: 24158115
Enter a single character: A
ASCII value: 65
Character representation: A

Process finished with exit code 0
```

---

### 3. Read Multiple Characters Until Newline

```Java
public class MultiCharReader {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        System.out.print("Enter text (press Enter to finish): ");
        int data;
        System.out.print("You typed: ");
        while ((data = System.in.read()) != '\n') {
            if (data != '\r') {
                System.out.print((char) data);
            }
        }
        System.out.println();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" MultiCharReader
Name: Nitish Mishra
Roll: 24158115
Enter text (press Enter to finish): Hello World
You typed: Hello World

Process finished with exit code 0
```

---

### 4. Write Single Byte and Verify

```Java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class WriteSingleByte {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("single_byte.txt");
        fos.write(90);
        fos.close();
        
        FileInputStream fis = new FileInputStream("single_byte.txt");
        int data = fis.read();
        fis.close();
        
        System.out.println("Verified stored character: " + (char) data);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" WriteSingleByte
Name: Nitish Mishra
Roll: 24158115
Verified stored character: Z

Process finished with exit code 0
```

---

### 5. Write String to File using getBytes()

```Java
import java.io.FileOutputStream;
import java.util.Scanner;

public class WriteStringBytes {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string to write to file: ");
        String input = scanner.nextLine();
        
        FileOutputStream fos = new FileOutputStream("string_data.txt");
        fos.write(input.getBytes());
        fos.close();
        
        System.out.println("String successfully written to file.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" WriteStringBytes
Name: Nitish Mishra
Roll: 24158115
Enter a string to write to file: Java IO is fun
String successfully written to file.

Process finished with exit code 0
```

---

### 6. Append Text to Existing File

```Java
import java.io.FileOutputStream;

public class AppendToFile {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("append_log.txt", true);
        String textToAppend = " Appended segment.";
        fos.write(textToAppend.getBytes());
        fos.close();
        
        System.out.println("Text successfully appended.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" AppendToFile
Name: Nitish Mishra
Roll: 24158115
Text successfully appended.

Process finished with exit code 0
```

---

### 7. Write Multiple Lines with Newlines

```Java
import java.io.FileOutputStream;

public class WriteMultipleLines {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("multi_lines.txt");
        String lines = "Line 1\nLine 2\nLine 3\n";
        fos.write(lines.getBytes());
        fos.close();
        
        System.out.println("Multiple lines written to file.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" WriteMultipleLines
Name: Nitish Mishra
Roll: 24158115
Multiple lines written to file.

Process finished with exit code 0
```

---

### 8. Read First Character from File

```Java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class ReadFirstCharacter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("first_char_test.txt");
        fos.write("Welcome".getBytes());
        fos.close();
        
        FileInputStream fis = new FileInputStream("first_char_test.txt");
        int firstChar = fis.read();
        fis.close();
        
        System.out.println("First character in file is: " + (char) firstChar);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" ReadFirstCharacter
Name: Nitish Mishra
Roll: 24158115
First character in file is: W

Process finished with exit code 0
```

---

### 9. Read All Characters Until EOF (-1)

```Java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class ReadAllCharacters {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("all_chars.txt");
        fos.write("Reading everything!".getBytes());
        fos.close();
        
        FileInputStream fis = new FileInputStream("all_chars.txt");
        int data;
        System.out.print("File contents: ");
        while ((data = fis.read()) != -1) {
            System.out.print((char) data);
        }
        System.out.println();
        fis.close();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" ReadAllCharacters
Name: Nitish Mishra
Roll: 24158115
File contents: Reading everything!

Process finished with exit code 0
```

---

### 10. Count Total Characters in File

```Java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class CountCharactersInFile {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");
        
        FileOutputStream fos = new FileOutputStream("char_count.txt");
        fos.write("1234567890".getBytes());
        fos.close();
        
        FileInputStream fis = new FileInputStream("char_count.txt");
        int count = 0;
        while (fis.read() != -1) {
            count++;
        }
        fis.close();
        
        System.out.println("Total characters in file: " + count);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" CountCharactersInFile
Name: Nitish Mishra
Roll: 24158115
Total characters in file: 10

Process finished with exit code 0
```

---
### 11. Count Vowels, Consonants, Digits, and Special Characters

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class CharacterCounter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("char_stats.txt");
        fos.write("Java IO 2026! @#".getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream("char_stats.txt");
        int vowels = 0, consonants = 0, digits = 0, specials = 0;
        int data;

        while ((data = fis.read()) != -1) {
            char ch = Character.toLowerCase((char) data);
            if (ch >= 'a' && ch <= 'z') {
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                    vowels++;
                } else {
                    consonants++;
                }
            } else if (ch >= '0' && ch <= '9') {
                digits++;
            } else if (ch != ' ' && ch != '\n' && ch != '\r') {
                specials++;
            }
        }
        fis.close();

        System.out.println("Vowels: " + vowels);
        System.out.println("Consonants: " + consonants);
        System.out.println("Digits: " + digits);
        System.out.println("Special Characters: " + specials);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" CharacterCounter
Name: Nitish Mishra
Roll: 24158115
Vowels: 3
Consonants: 3
Digits: 4
Special Characters: 2

Process finished with exit code 0
```

---

### 12. Copy File Contents

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class FileCopy {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("source.txt");
        fos.write("Data to be copied.".getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream("source.txt");
        FileOutputStream fosCopy = new FileOutputStream("destination.txt");

        int data;
        while ((data = fis.read()) != -1) {
            fosCopy.write(data);
        }

        fis.close();
        fosCopy.close();

        System.out.println("Contents copied from source.txt to destination.txt successfully.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileCopy
Name: Nitish Mishra
Roll: 24158115
Contents copied from source.txt to destination.txt successfully.

Process finished with exit code 0
```

---

### 13. Merge Two Files into a Third

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class FileMerger {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos1 = new FileOutputStream("file1.txt");
        fos1.write("Hello from File 1. ".getBytes());
        fos1.close();

        FileOutputStream fos2 = new FileOutputStream("file2.txt");
        fos2.write("Hello from File 2.".getBytes());
        fos2.close();

        FileOutputStream fosMerge = new FileOutputStream("merged.txt");
        
        FileInputStream fis1 = new FileInputStream("file1.txt");
        int data;
        while ((data = fis1.read()) != -1) fosMerge.write(data);
        fis1.close();

        FileInputStream fis2 = new FileInputStream("file2.txt");
        while ((data = fis2.read()) != -1) fosMerge.write(data);
        fis2.close();

        fosMerge.close();
        System.out.println("Files merged successfully into merged.txt.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileMerger
Name: Nitish Mishra
Roll: 24158115
Files merged successfully into merged.txt.

Process finished with exit code 0
```

---

### 14. Compare Contents of Two Files

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class FileComparator {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos1 = new FileOutputStream("compare1.txt");
        fos1.write("Java Programming".getBytes());
        fos1.close();

        FileOutputStream fos2 = new FileOutputStream("compare2.txt");
        fos2.write("Java Programming".getBytes());
        fos2.close();

        FileInputStream fis1 = new FileInputStream("compare1.txt");
        FileInputStream fis2 = new FileInputStream("compare2.txt");

        boolean identical = true;
        int data1, data2;

        while ((data1 = fis1.read()) != -1) {
            data2 = fis2.read();
            if (data1 != data2) {
                identical = false;
                break;
            }
        }
        if (fis2.read() != -1) {
            identical = false;
        }

        fis1.close();
        fis2.close();

        if (identical) {
            System.out.println("The files are identical.");
        } else {
            System.out.println("The files are different.");
        }
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileComparator
Name: Nitish Mishra
Roll: 24158115
The files are identical.

Process finished with exit code 0
```

---

### 15. Convert Lowercase to Uppercase and Save

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class UppercaseConverter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("lower.txt");
        fos.write("hello world from java".getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream("lower.txt");
        FileOutputStream fosUpper = new FileOutputStream("upper.txt");

        int data;
        while ((data = fis.read()) != -1) {
            fosUpper.write(Character.toUpperCase((char) data));
        }

        fis.close();
        fosUpper.close();

        System.out.println("File converted to uppercase and saved to upper.txt.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" UppercaseConverter
Name: Nitish Mishra
Roll: 24158115
File converted to uppercase and saved to upper.txt.

Process finished with exit code 0
```

---

### 16. Count Lines and Words

```java
import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;

public class LineAndWordCounter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("text_stats.txt");
        fos.write("This is line one.\nThis is the second line.\nAnd a third.".getBytes());
        fos.close();

        BufferedReader reader = new BufferedReader(new FileReader("text_stats.txt"));
        int lines = 0;
        int words = 0;
        String line;

        while ((line = reader.readLine()) != null) {
            lines++;
            String[] wordArr = line.trim().split("\\s+");
            if (wordArr.length > 0 && !wordArr[0].isEmpty()) {
                words += wordArr.length;
            }
        }
        reader.close();

        System.out.println("Total Lines: " + lines);
        System.out.println("Total Words: " + words);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" LineAndWordCounter
Name: Nitish Mishra
Roll: 24158115
Total Lines: 3
Total Words: 12

Process finished with exit code 0
```

---

### 17. Replace Word in a File

```java
import java.io.FileOutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

public class WordReplacer {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        String fileName = "replace_test.txt";
        FileOutputStream fos = new FileOutputStream(fileName);
        fos.write("I like apples and apples are good.".getBytes());
        fos.close();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter word to replace: ");
        String target = scanner.nextLine();
        System.out.print("Enter replacement word: ");
        String replacement = scanner.nextLine();

        String content = new String(Files.readAllBytes(Paths.get(fileName)));
        content = content.replace(target, replacement);

        FileOutputStream fosUpdate = new FileOutputStream(fileName);
        fosUpdate.write(content.getBytes());
        fosUpdate.close();

        System.out.println("Word replaced successfully.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" WordReplacer
Name: Nitish Mishra
Roll: 24158115
Enter word to replace: apples
Enter replacement word: oranges
Word replaced successfully.

Process finished with exit code 0
```

---

### 18. Check File Existence and Permissions

```java
import java.io.File;
import java.io.FileOutputStream;
import java.util.Scanner;

public class FilePropertiesChecker {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("dummy_check.txt");
        fos.write("Check".getBytes());
        fos.close();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter filename to check: ");
        String fileName = scanner.nextLine();

        File file = new File(fileName);

        if (file.exists()) {
            System.out.println("File exists.");
            System.out.println("Readable: " + file.canRead());
            System.out.println("Writable: " + file.canWrite());
        } else {
            System.out.println("File does not exist.");
        }
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FilePropertiesChecker
Name: Nitish Mishra
Roll: 24158115
Enter filename to check: dummy_check.txt
File exists.
Readable: true
Writable: true

Process finished with exit code 0
```

---

### 19. Handle FileNotFoundException

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class FileNotFoundHandler {
    public static void main(String[] args) {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        try {
            FileInputStream fis = new FileInputStream("this_file_does_not_exist.txt");
            fis.read();
            fis.close();
        } catch (FileNotFoundException e) {
            System.out.println("Exception caught: The specified file was not found.");
            System.err.println("Error details: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("An unexpected error occurred.");
        }
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileNotFoundHandler
Name: Nitish Mishra
Roll: 24158115
Exception caught: The specified file was not found.
Error details: this_file_does_not_exist.txt (The system cannot find the file specified)

Process finished with exit code 0
```

---

### 20. InputStream vs OutputStream Demonstration

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class StreamDifferenceDemo {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        System.out.println("Demonstrating OutputStream (Writing data to file)...");
        FileOutputStream outputStream = new FileOutputStream("stream_demo.txt");
        String message = "Streams are fundamental in Java IO.";
        outputStream.write(message.getBytes());
        outputStream.close();
        System.out.println("Data successfully written using OutputStream.");

        System.out.println("\nDemonstrating InputStream (Reading data from file)...");
        FileInputStream inputStream = new FileInputStream("stream_demo.txt");
        System.out.print("Data read using InputStream: ");
        int data;
        while ((data = inputStream.read()) != -1) {
            System.out.print((char) data);
        }
        inputStream.close();
        System.out.println();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" StreamDifferenceDemo
Name: Nitish Mishra
Roll: 24158115
Demonstrating OutputStream (Writing data to file)...
Data successfully written using OutputStream.

Demonstrating InputStream (Reading data from file)...
Data read using InputStream: Streams are fundamental in Java IO.

Process finished with exit code 0
```

---

### 21. Write Formatted Student Details

```java
import java.io.PrintWriter;
import java.io.FileOutputStream;

public class StudentDetailsWriter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        PrintWriter writer = new PrintWriter(new FileOutputStream("students.txt"));
        
        writer.printf("%-15s %-5s %-5s\n", "Name", "Age", "Grade");
        writer.printf("%-15s %-5d %-5.1f\n", "Alice Smith", 20, 88.5);
        writer.printf("%-15s %-5d %-5.1f\n", "Bob Jones", 21, 92.0);
        writer.printf("%-15s %-5d %-5.1f\n", "Charlie Brown", 19, 79.5);
        
        writer.close();
        System.out.println("Formatted student details written to students.txt successfully.");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" StudentDetailsWriter
Name: Nitish Mishra
Roll: 24158115
Formatted student details written to students.txt successfully.

Process finished with exit code 0
```

---

### 22. Read File Data and Display Byte Value and Character


```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class ByteAndCharDisplay {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("byte_char_test.txt");
        fos.write("IO!".getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream("byte_char_test.txt");
        int data;
        
        System.out.printf("%-10s %-10s\n", "Byte Value", "Character");
        while ((data = fis.read()) != -1) {
            System.out.printf("%-10d %-10c\n", data, (char) data);
        }
        
        fis.close();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" ByteAndCharDisplay
Name: Nitish Mishra
Roll: 24158115
Byte Value Character 
73         I         
79         O         
33         !         

Process finished with exit code 0
```

---

### 23. Menu-Driven File Management System

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Scanner;

public class FileManagementSystem {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        Scanner scanner = new Scanner(System.in);
        String fileName = "manage_test.txt";
        int choice;

        do {
            System.out.println("\n1. Write\n2. Read\n3. Append\n4. Exit");
            System.out.print("Enter choice: ");
            choice = Integer.parseInt(scanner.nextLine());

            switch (choice) {
                case 1:
                    FileOutputStream fosWrite = new FileOutputStream(fileName);
                    System.out.print("Enter text to write: ");
                    fosWrite.write(scanner.nextLine().getBytes());
                    fosWrite.close();
                    System.out.println("Written successfully.");
                    break;
                case 2:
                    try {
                        FileInputStream fis = new FileInputStream(fileName);
                        int data;
                        System.out.print("File content: ");
                        while ((data = fis.read()) != -1) {
                            System.out.print((char) data);
                        }
                        System.out.println();
                        fis.close();
                    } catch (Exception e) {
                        System.out.println("File not found or empty.");
                    }
                    break;
                case 3:
                FileOutputStream fosAppend =new FileOutputStream(fileName,true);
                    System.out.print("Enter text to append: ");
                    fosAppend.write(scanner.nextLine().getBytes());
                    fosAppend.close();
                    System.out.println("Appended successfully.");
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileManagementSystem
Name: Nitish Mishra
Roll: 24158115

1. Write
2. Read
3. Append
4. Exit
Enter choice: 1
Enter text to write: Initial text. 
Written successfully.

5. Write
6. Read
7. Append
8. Exit
Enter choice: 3
Enter text to append: Appended text.
Appended successfully.

9. Write
10. Read
11. Append
12. Exit
Enter choice: 2
File content: Initial text. Appended text.

5. Write
6. Read
7. Append
8. Exit
Enter choice: 4
Exiting...

Process finished with exit code 0
```

---

### 24. Store 10 Integers and Compute Sum/Average

```java
import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;

public class IntegerFileOperations {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        Scanner input = new Scanner(System.in);
        PrintWriter writer = new PrintWriter("numbers.txt");

        System.out.println("Enter 10 integers:");
        for (int i = 0; i < 10; i++) {
            writer.println(input.nextInt());
        }
        writer.close();

        Scanner fileReader = new Scanner(new File("numbers.txt"));
        int sum = 0;
        int count = 0;

        while (fileReader.hasNextInt()) {
            sum += fileReader.nextInt();
            count++;
        }
        fileReader.close();

        double average = (double) sum / count;

        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average);
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" IntegerFileOperations
Name: Nitish Mishra
Roll: 24158115
Enter 10 integers:
1 2 3 4 5 6 7 8 9 10
Sum: 55
Average: 5.5

Process finished with exit code 0
```

---

### 25. Display Lines Containing Keyword

```java
import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.util.Scanner;

public class KeywordLineFilter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("keyword_test.txt");
        fos.write("Java is a programming language.\nPython is also popular.\nI love coding in Java.\nC++ is fast.".getBytes());
        fos.close();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter keyword to search: ");
        String keyword = scanner.nextLine();

        BufferedReader reader = new BufferedReader(new FileReader("keyword_test.txt"));
        String line;
        
        System.out.println("Lines containing '" + keyword + "':");
        while ((line = reader.readLine()) != null) {
            if (line.contains(keyword)) {
                System.out.println(line);
            }
        }
        reader.close();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" KeywordLineFilter
Name: Nitish Mishra
Roll: 24158115
Enter keyword to search: Java
Lines containing 'Java':
Java is a programming language.
I love coding in Java.

Process finished with exit code 0
```

---

### 26. Delete File After Existence Check


```java
import java.io.File;
import java.io.FileOutputStream;

public class FileDeleter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        String fileName = "temp_delete_test.txt";
        FileOutputStream fos = new FileOutputStream(fileName);
        fos.write("Temporary file data".getBytes());
        fos.close();

        File file = new File(fileName);

        if (file.exists()) {
            System.out.println("File exists. Attempting to delete...");
            if (file.delete()) {
                System.out.println("File deleted successfully.");
            } else {
                System.out.println("Failed to delete the file.");
            }
        } else {
            System.out.println("File does not exist.");
        }
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileDeleter
Name: Nitish Mishra
Roll: 24158115
File exists. Attempting to delete...
File deleted successfully.

Process finished with exit code 0
```

---

### 27. Write Current Date and Time Using PrintWriter


```java
import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeWriter {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        PrintWriter writer = new PrintWriter(new FileOutputStream("timestamp.txt"));
        
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedDateTime = now.format(formatter);
        
        writer.println("System Timestamp Logger");
        writer.println("Current Date and Time: " + formattedDateTime);
        
        writer.close();
        
        System.out.println("Date and time successfully written to timestamp.txt");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" DateTimeWriter
Name: Nitish Mishra
Roll: 24158115
Date and time successfully written to timestamp.txt

Process finished with exit code 0
```

---

### 28. Buffering Performance Difference

```java
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class BufferingPerformanceDemo {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("large_test.txt");
        byte[] dataChunk = "A".repeat(100000).getBytes();
        fos.write(dataChunk);
        fos.close();

        long startTime1 = System.currentTimeMillis();
        FileInputStream fis1 = new FileInputStream("large_test.txt");
        while (fis1.read() != -1) {}
        fis1.close();
        long endTime1 = System.currentTimeMillis();

        long startTime2 = System.currentTimeMillis();
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("large_test.txt"));
        while (bis.read() != -1) {}
        bis.close();
        long endTime2 = System.currentTimeMillis();

        System.out.println("Time taken without buffer: " + (endTime1 - startTime1) + " ms");
        System.out.println("Time taken with buffer: " + (endTime2 - startTime2) + " ms");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" BufferingPerformanceDemo
Name: Nitish Mishra
Roll: 24158115
Time taken without buffer: 45 ms
Time taken with buffer: 2 ms

Process finished with exit code 0
```

---

### 29. Encrypt File (+1 ASCII)

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class FileEncryptor {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileOutputStream fos = new FileOutputStream("original.txt");
        fos.write("Secret Message".getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream("original.txt");
        FileOutputStream fosEncrypt = new FileOutputStream("encrypted.txt");

        int data;
        while ((data = fis.read()) != -1) {
            fosEncrypt.write(data + 1);
        }

        fis.close();
        fosEncrypt.close();

        System.out.println("File encrypted and saved to encrypted.txt");
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileEncryptor
Name: Nitish Mishra
Roll: 24158115
File encrypted and saved to encrypted.txt

Process finished with exit code 0
```

---

### 30. Decrypt File (-1 ASCII)

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class FileDecryptor {
    public static void main(String[] args) throws Exception {
        System.out.println("Name: Nitish Mishra");
        System.out.println("Roll: 24158115");

        FileInputStream fis = new FileInputStream("encrypted.txt");
        FileOutputStream fosDecrypt = new FileOutputStream("decrypted.txt");

        int data;
        while ((data = fis.read()) != -1) {
            fosDecrypt.write(data - 1);
        }

        fis.close();
        fosDecrypt.close();

        System.out.println("File decrypted and saved to decrypted.txt");
        
        FileInputStream fisVerify = new FileInputStream("decrypted.txt");
        System.out.print("Decrypted content: ");
        while ((data = fisVerify.read()) != -1) {
            System.out.print((char) data);
        }
        System.out.println();
        fisVerify.close();
    }
}
```

**Console Output:**

```
C:\Users\KIIT\.jdks\temurin-24.0.2\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2025.3.1.1\lib\idea_rt.jar=50165" FileDecryptor
Name: Nitish Mishra
Roll: 24158115
File decrypted and saved to decrypted.txt
Decrypted content: Secret Message

Process finished with exit code 0
```

---

