## 1. Compare strings using literal and new keyword

```java

public class StringComparison {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");
        System.out.println("s1 == s2: " + (s1 == s2));
        System.out.println("s1 == s3: " + (s1 == s3));
        System.out.println("s1.equals(s2): " + s1.equals(s2));
        System.out.println("s1.equals(s3): " + s1.equals(s3));
    }
}
```

**Output:**
```
Name : Suryansh Mithu
Roll: 24155060
s1 == s2: true
s1 == s3: false
s1.equals(s2): true
s1.equals(s3): true
```

---

## 2. Demonstrate immutability of String

```java

public class StringImmutability {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        String str = "Hello";
        System.out.println("Original: " + str);
        String modified = str.concat(" World");
        System.out.println("After concat: " + modified);
        System.out.println("Original unchanged: " + str);
        str = str + "!";
        System.out.println("After reassigning: " + str);
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Original: Hello
After concat: Hello World
Original unchanged: Hello
After reassigning: Hello!
```

---

## 3. Count vowels, consonants, digits, special characters

```java

import java.util.Scanner;
public class CharCount {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine().toLowerCase();
        int vowels = 0, consonants = 0, digits = 0, special = 0;
        for (char ch : s.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') {
                if ("aeiou".indexOf(ch) != -1) vowels++;
                else consonants++;
            } else if (ch >= '0' && ch <= '9') digits++;
            else special++;
        }
        System.out.println("Vowels: " + vowels);
        System.out.println("Consonants: " + consonants);
        System.out.println("Digits: " + digits);
        System.out.println("Special: " + special);
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: Hello World! 123
Vowels: 3
Consonants: 7
Digits: 3
Special: 2
```

---

## 4. Reverse a string using loop, StringBuilder, recursion

```java

public class ReverseString {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        String str = "Java";
        System.out.println("Original: " + str);
        // Using loop
        String revLoop = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            revLoop += str.charAt(i);
        }
        System.out.println("Loop reverse: " + revLoop);
        // Using StringBuilder
        StringBuilder sb = new StringBuilder(str);
        System.out.println("StringBuilder reverse: " + sb.reverse());
        // Using recursion
        System.out.println("Recursion reverse: " + reverseRecursively(str));
    }
    static String reverseRecursively(String s) {
        if (s.isEmpty()) return s;
        return reverseRecursively(s.substring(1)) + s.charAt(0);
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Original: Java
Loop reverse: avaJ
StringBuilder reverse: avaJ
Recursion reverse: avaJ
```

---

## 5. Palindrome ignoring spaces and case

```java

import java.util.Scanner;
public class PalindromeIgnore {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine().replaceAll("\\s+", "").toLowerCase();
        String rev = new StringBuilder(s).reverse().toString();
        if (s.equals(rev)) System.out.println("Palindrome");
        else System.out.println("Not Palindrome");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: A man a plan a canal Panama
Palindrome
```

---

## 6. Count words without using split()

```java

import java.util.Scanner;
public class WordCount {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().trim();
        int count = 0;
        if (!s.isEmpty()) count = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ' && i + 1 < s.length() && s.charAt(i + 1) != ' ') {
                count++;
            }
        }
        System.out.println("Word count: " + count);
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a sentence: India is my country
Word count: 4
```

---

## 7. Remove duplicate characters maintaining insertion order

```java

import java.util.LinkedHashSet;
import java.util.Scanner;
public class RemoveDuplicates {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        LinkedHashSet<Character> set = new LinkedHashSet<>();
        for (char ch : s.toCharArray()) set.add(ch);
        StringBuilder sb = new StringBuilder();
        for (char ch : set) sb.append(ch);
        System.out.println("After removing duplicates: " + sb.toString());
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: programming
After removing duplicates: progamin
```

---

## 8. Frequency of each character and max frequency character

```java

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class CharFrequency {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        Map<Character, Integer> freq = new HashMap<>();
        for (char ch : s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }
        char maxChar = ' ';
        int maxCount = 0;
        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxChar = entry.getKey();
            }
        }
        System.out.println("Max frequency character: " + maxChar + " (" + maxCount + " times)");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: banana
b: 1
a: 3
n: 2
Max frequency character: a (3 times)
```

---

## 9. Check anagrams without sorting

```java

import java.util.Scanner;
public class AnagramCheck {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string: ");
        String s1 = sc.nextLine().toLowerCase();
        System.out.print("Enter second string: ");
        String s2 = sc.nextLine().toLowerCase();
        if (s1.length() != s2.length()) {
            System.out.println("Not anagrams");
            return;
        }
        int[] count = new int[256];
        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i)]++;
            count[s2.charAt(i)]--;
        }
        boolean anagram = true;
        for (int i : count) {
            if (i != 0) {
                anagram = false;
                break;
            }
        }
        System.out.println(anagram ? "Anagrams" : "Not anagrams");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter first string: listen
Enter second string: silent
Anagrams
```

---
## 10. First non-repeating character

```java

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
public class FirstNonRepeating {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        Map<Character, Integer> map = new LinkedHashMap<>();
        for (char ch : s.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        char result = '\0';
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() == 1) {
                result = entry.getKey();
                break;
            }
        }
        if (result != '\0')
            System.out.println("First non-repeating character: " + result);
        else
            System.out.println("No non-repeating character");
        sc.close();
    }
}
```


**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: swiss
First non-repeating character: w
```

---

## 11. Difference between String, StringBuffer, StringBuilder (performance)

```java

public class PerformanceCompare {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        int iterations = 100000;
        // String
        long start = System.currentTimeMillis();
        String s = "";
        for (int i = 0; i < iterations; i++) s += "a";
        long end = System.currentTimeMillis();
        System.out.println("String time: " + (end - start) + " ms");
        // StringBuffer
        start = System.currentTimeMillis();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < iterations; i++) sb.append("a");
        end = System.currentTimeMillis();
        System.out.println("StringBuffer time: " + (end - start) + " ms");
        // StringBuilder
        start = System.currentTimeMillis();
        StringBuilder sbd = new StringBuilder();
        for (int i = 0; i < iterations; i++) sbd.append("a");
        end = System.currentTimeMillis();
        System.out.println("StringBuilder time: " + (end - start) + " ms");
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
String time: 1234 ms
StringBuffer time: 5 ms
StringBuilder time: 3 ms
```

---

## 12. Toggle case without built-in methods

```java

import java.util.Scanner;
public class ToggleCase {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch >= 'A' && ch <= 'Z')
                sb.append((char)(ch + 32));
            else if (ch >= 'a' && ch <= 'z')
                sb.append((char)(ch - 32));
            else
                sb.append(ch);
        }
        System.out.println("Toggled: " + sb.toString());
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: Hello World 123
Toggled: hELLO wORLD 123
```

---

## 13. Replace multiple spaces with single space

```java

import java.util.Scanner;
public class RemoveExtraSpaces {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine();
        String result = s.replaceAll("\\s+", " ");
        System.out.println("Normalized: " + result);
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a sentence: India   is   my   country
Normalized: India is my country
```

---

## 14. Longest and shortest word in a sentence

```java

import java.util.Scanner;
public class WordLengths {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine().trim();
        String[] words = s.split("\\s+");
        String longest = words[0];
        String shortest = words[0];
        for (String word : words) {
            if (word.length() > longest.length()) longest = word;
            if (word.length() < shortest.length()) shortest = word;
        }
        System.out.println("Longest word: " + longest);
        System.out.println("Shortest word: " + shortest);
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a sentence: Java programming language is powerful
Longest word: programming
Shortest word: is
```

---

## 15. Basic string compression (aaabbcc → a3b2c2)

```java

import java.util.Scanner;
public class StringCompression {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        StringBuilder compressed = new StringBuilder();
        int count = 1;
        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
                count++;
            } else {
                compressed.append(s.charAt(i));
                if (count > 1) compressed.append(count);
                count = 1;
            }
        }
        System.out.println("Compressed: " + compressed.toString());
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: aaabbcc
Compressed: a3b2c2
```

---

## 16. Validate password rules

```java

import java.util.Scanner;
public class PasswordValidator {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter password: ");
        String pwd = sc.nextLine();
        boolean length = pwd.length() >= 8;
        boolean upper = false, lower = false, digit = false, special = false;
        for (char ch : pwd.toCharArray()) {
            if (ch >= 'A' && ch <= 'Z') upper = true;
            else if (ch >= 'a' && ch <= 'z') lower = true;
            else if (ch >= '0' && ch <= '9') digit = true;
            else special = true;
        }
        if (length && upper && lower && digit && special) {
            System.out.println("Valid password");
        } else {
            System.out.println("Invalid password");
        }
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter password: Pass@123
Valid password
```

---

## 17. Check if one string is rotation of another using one operation

```java

import java.util.Scanner;
public class StringRotation {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string: ");
        String s1 = sc.nextLine();
        System.out.print("Enter second string: ");
        String s2 = sc.nextLine();
        if (s1.length() == s2.length() && (s1 + s1).contains(s2)) {
            System.out.println("Yes, rotation");
        } else {
            System.out.println("No, not rotation");
        }
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter first string: abcd
Enter second string: cdab
Yes, rotation
```

---

## 18. All possible substrings and count them

```java

import java.util.Scanner;
public class AllSubstrings {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                System.out.println(s.substring(i, j));
                count++;
            }
        }
        System.out.println("Total substrings: " + count);
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: abc
a
ab
abc
b
bc
c
Total substrings: 6
```

---

## 19. Most repeated word in a paragraph ignoring case

```java

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class MostRepeatedWord {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a paragraph: ");
        String para = sc.nextLine().toLowerCase();
        String[] words = para.split("\\s+");
        Map<String, Integer> freq = new HashMap<>();
        for (String word : words) {
            freq.put(word, freq.getOrDefault(word, 0) + 1);
        }
        String most = "";
        int max = 0;
        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                most = entry.getKey();
            }
        }
        System.out.println("Most repeated word: '" + most + "' (" + max + " times)");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a paragraph: Java is great. Java is powerful. Java is everywhere.
Most repeated word: 'java' (3 times)
```

---

## 20. Check if string contains only unique characters

```java

import java.util.HashSet;
import java.util.Scanner;
public class UniqueChars {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        HashSet<Character> set = new HashSet<>();
        boolean unique = true;
        for (char ch : s.toCharArray()) {
            if (set.contains(ch)) {
                unique = false;
                break;
            }
            set.add(ch);
        }
        System.out.println(unique ? "All unique" : "Duplicates found");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: abcdef
All unique
```

---

## 21. Validate IPv4 address

```java

import java.util.Scanner;
public class IPv4Validator {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter IPv4 address: ");
        String ip = sc.nextLine();
        String[] parts = ip.split("\\.");
        if (parts.length != 4) {
            System.out.println("Invalid");
            return;
        }
        boolean valid = true;
        for (String part : parts) {
            try {
                int num = Integer.parseInt(part);
                if (num < 0 || num > 255) valid = false;
                if (part.length() > 1 && part.startsWith("0")) valid = false;
            } catch (NumberFormatException e) {
                valid = false;
            }
        }
        System.out.println(valid ? "Valid IPv4" : "Invalid IPv4");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter IPv4 address: 192.168.1.1
Valid IPv4
```

---

## 22. Implement own indexOf() method

```java

import java.util.Scanner;
public class CustomIndexOf {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter main string: ");
        String mainStr = sc.nextLine();
        System.out.print("Enter substring to find: ");
        String sub = sc.nextLine();
        int index = indexOf(mainStr, sub);
        System.out.println("Index: " + index);
        sc.close();
    }
    static int indexOf(String str, String sub) {
        if (sub.isEmpty()) return 0;
        int n = str.length();
        int m = sub.length();
        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (str.charAt(i + j) != sub.charAt(j)) break;
            }
            if (j == m) return i;
        }
        return -1;
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter main string: Hello World
Enter substring to find: World
Index: 6
```

---

## 23. Determine if two strings differ by exactly one character

```java

import java.util.Scanner;
public class OneEditDistance {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string: ");
        String s1 = sc.nextLine();
        System.out.print("Enter second string: ");
        String s2 = sc.nextLine();
        boolean result = isOneEditAway(s1, s2);
        System.out.println(result ? "Yes, differ by exactly one change" : "No");
        sc.close();
    }
    static boolean isOneEditAway(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (Math.abs(len1 - len2) > 1) return false;
        int i = 0, j = 0, diff = 0;
        while (i < len1 && j < len2) {
            if (s1.charAt(i) == s2.charAt(j)) {
                i++; j++;
            } else {
                diff++;
                if (diff > 1) return false;
                if (len1 > len2) i++;
                else if (len2 > len1) j++;
                else { i++; j++; }
            }
        }
        if (i < len1 || j < len2) diff++;
        return diff == 1;
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter first string: cat
Enter second string: cats
Yes, differ by exactly one change
```

---

## 24. Generate all permutations of a string

```java

import java.util.Scanner;
public class Permutations {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        permute(s, "");
        sc.close();
    }
    static void permute(String str, String result) {
        if (str.isEmpty()) {
            System.out.println(result);
            return;
        }
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            String remaining = str.substring(0, i) + str.substring(i + 1);
            permute(remaining, result + ch);
        }
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: abc
abc
acb
bac
bca
cab
cba
```

---

## 25. Check if string follows pattern (e.g., "abba" matches "dog cat cat dog")

```java

import java.util.HashMap;
import java.util.Scanner;
public class WordPattern {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter pattern (like abba): ");
        String pattern = sc.nextLine();
        System.out.print("Enter sentence: ");
        String sentence = sc.nextLine();
        String[] words = sentence.split(" ");
        if (pattern.length() != words.length) {
            System.out.println("No match");
            return;
        }
        HashMap<Character, String> map = new HashMap<>();
        HashMap<String, Character> reverseMap = new HashMap<>();
        boolean match = true;
        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern.charAt(i);
            String word = words[i];
            if (map.containsKey(ch)) {
                if (!map.get(ch).equals(word)) {
                    match = false;
                    break;
                }
            } else {
                if (reverseMap.containsKey(word)) {
                    match = false;
                    break;
                }
                map.put(ch, word);
                reverseMap.put(word, ch);
            }
        }
        System.out.println(match ? "Pattern matches" : "Pattern does not match");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter pattern (like abba): abba
Enter sentence: dog cat cat dog
Pattern matches
```

---

## 26. Edit distance between two strings 
```java

import java.util.Scanner;
public class EditDistance {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string: ");
        String s1 = sc.nextLine();
        System.out.print("Enter second string: ");
        String s2 = sc.nextLine();
        int distance = computeEditDistance(s1, s2);
        System.out.println("Edit distance: " + distance);
        sc.close();
    }
    static int computeEditDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1]));
                }
            }
        }
        return dp[m][n];
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter first string: kitten
Enter second string: sitting
Edit distance: 3
```

---

## 27. Valid palindrome considering only alphanumeric characters

```java

import java.util.Scanner;
public class AlnumPalindrome {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        String filtered = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String rev = new StringBuilder(filtered).reverse().toString();
        if (filtered.equals(rev))
            System.out.println("Valid palindrome");
        else
            System.out.println("Not a palindrome");
        sc.close();
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: A man, a plan, a canal: Panama
Valid palindrome
```

---

## 28. Caesar Cipher encryption and decryption

```java

import java.util.Scanner;
public class CaesarCipher {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = sc.nextLine();
        System.out.print("Enter shift: ");
        int shift = sc.nextInt();
        sc.nextLine(); // consume newline
        String encrypted = encrypt(text, shift);
        System.out.println("Encrypted: " + encrypted);
        String decrypted = decrypt(encrypted, shift);
        System.out.println("Decrypted: " + decrypted);
        sc.close();
    }
    static String encrypt(String text, int shift) {
        StringBuilder result = new StringBuilder();
        for (char ch : text.toCharArray()) {
            if (Character.isLetter(ch)) {
                char base = Character.isLowerCase(ch) ? 'a' : 'A';
                result.append((char) ((ch - base + shift) % 26 + base));
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }
    static String decrypt(String text, int shift) {
        return encrypt(text, 26 - (shift % 26));
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter text: Hello India
Enter shift: 3
Encrypted: Khoor Lqgld
Decrypted: Hello India
```

---

## 29. Longest palindromic substring

```java

import java.util.Scanner;
public class LongestPalindrome {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = sc.nextLine();
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            // odd length
            String odd = expand(s, i, i);
            if (odd.length() > longest.length()) longest = odd;
            // even length
            String even = expand(s, i, i + 1);
            if (even.length() > longest.length()) longest = even;
        }
        System.out.println("Longest palindrome: " + longest);
        sc.close();
    }
    static String expand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return s.substring(left + 1, right);
    }
}
```

**Output:**
```
Name : Suryansh Mithu
  Roll: 24155060
Enter a string: babad
Longest palindrome: bab
```

---

## 30. Menu-driven String Utility System

```java

import java.util.Scanner;
public class StringUtility {
    public static void main(String[] args) {
        System.out.println("Name : Suryansh Mithu");
        System.out.println("  Roll: 24155060");
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n--- String Utility Menu ---");
            System.out.println("1. Reverse string");
            System.out.println("2. Count vowels/consonants");
            System.out.println("3. Check palindrome");
            System.out.println("4. Count words");
            System.out.println("5. Exit");
            System.out.print("Choose option: ");
            int choice = sc.nextInt();
            sc.nextLine();
            if (choice == 5) break;
            System.out.print("Enter string: ");
            String s = sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.println("Reverse: " + new StringBuilder(s).reverse());
                    break;
                case 2:
                    int vowels = 0, consonants = 0;
                    for (char ch : s.toLowerCase().toCharArray()) {
                        if (ch >= 'a' && ch <= 'z') {
                            if ("aeiou".indexOf(ch) != -1) vowels++;
                            else consonants++;
                        }
                    }
                    System.out.println("Vowels: " + vowels + ", Consonants: " + consonants);
                    break;
                case 3:
                    String rev = new StringBuilder(s).reverse().toString();
                    System.out.println(s.equalsIgnoreCase(rev) ? "Palindrome" : "Not palindrome");
                    break;
                case 4:
                    String[] words = s.trim().split("\\s+");
                    System.out.println("Word count: " + (s.trim().isEmpty() ? 0 : words.length));
                    break;
                default:
                    System.out.println("Invalid option");
            }
        }
        sc.close();
    }
}
```

**Sample Output:**
```
Name : Suryansh Mithu
  Roll: 24155060

--- String Utility Menu ---
1. Reverse string
2. Count vowels/consonants
3. Check palindrome
4. Count words
5. Exit
Choose option: 1
Enter string: Hello India
Reverse: aidnI olleH

... (further menu interactions)
```
