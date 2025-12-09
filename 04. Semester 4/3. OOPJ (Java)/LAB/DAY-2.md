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
            }        }        System.out.println("Second Largest: " + second);  
    }}
```

## Output

![[Pasted image 20251209124725.png]]


---
# 2.  Remove duplicate elements from array and print new array size

