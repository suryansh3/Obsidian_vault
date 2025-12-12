The code is written using JetBrains IDE.
The the code in the block space format pdf is written using obsidian 
**Array Question**

---
# 1. Second Largest Number without Sorting

``` Java
public class Day2_1{  
    public static void main(String[] args) {  
        System.out.println("Name : Suryansh Mithu");  
        System.out.println("Roll : 24155060");  
        int[] arr = {12, 35, 1, 10, 34, 1};  
        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;  
        for (int i=0;i<arr.length;i++) {  
           int num = arr[i];  
            if (num > first) {  
                second = first;  
                first = num;  
            } else if (num > second && num != first) {  
                second = num;  
            }        
        }  
    System.out.println("Second Largest: " + second);  
    }
    }
```

## Output

![[Pasted image 20251209124725.png]]


---
# 2.  Remove duplicate elements from array and print new array size











---
# 3. Rotation of array by k position (Right Rotation)

``` Java
//3. Write a Java program to rotate an array by K positions to the right (user inputs K).  
import java.util.*;  
  
public class Day2_3 {  
    public static void main(String[] args) {  
        int[] arr = {12,23,56,78,234,13};  
        Scanner sc = new Scanner(System.in);  
        System.out.println("Enter postion to rotate");  
        int k = sc.nextInt();  
        int n = arr.length;  
        k = k % n;  
  
        int[] temp = new int[n];  
        for (int i = 0; i < n; i++) {  
            temp[(i + k) % n] = arr[i];  
        }        System.out.println(Arrays.toString(temp));  
    }}

```

## Output

![[Pasted image 20251209131003.png]]

---
# 4. Merge 2 sorted array into new sorted array

```
//**4. Write a Java program to merge two sorted arrays into a new sorted array (without using built-in sort).**

```










---
# 5. Count the frequency of each element in an array  

``` Java
//5. Write a Java program to count the frequency of each element in an array (using another array/map logic).  
import java.util.*;  
  
public class Day2_5 {  
    public static void main(String[] args) {  
        System.out.println("Name : Suryansh Mithu");  
        System.out.println("Roll : 24155060");  
        int[] arr = {1,12,23,12,45,23,23,31,31,31,45};  
        Map<Integer,Integer> freq = new HashMap<>();  
        for(int num: arr)  
        {freq.put(num, freq.getOrDefault(num,0)+1);}  
        System.out.println("Element" + "  " + "Frequency");  
        for(Map.Entry<Integer,Integer> e: freq.entrySet())  
            System.out.println(e.getKey()+"   =    "+e.getValue());  
    }}
```

## Output :

![[Pasted image 20251209134825.png]]

# 6.  Java program to find all pairs of elements whose sum equals a given target 

```JAVA
//**Write a Java program to find all pairs of elements whose sum equals a given target (avoid duplicates).**


```

## Output :










---

# 7. **Java program to check whether two arrays are equal**

```JAVA
//**Write a Java program to check whether two arrays are equal (same elements in same order).**
```

# Output :






---

# 8.  **Sort an array using Bubble Sort and print each pass**

```JAVA
// **Write a Java program to sort an array using Bubble Sort and print each pass.**
```

# Output :









----

# 9. **Separate even and odd numbers into two different arrays.**

```JAVA
//**Write a Java program to separate even and odd numbers into two different arrays.**

```

# Output:











----
# 10. 
