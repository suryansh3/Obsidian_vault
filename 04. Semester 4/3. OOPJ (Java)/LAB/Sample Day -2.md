
1. Second largest element without sorting:
```java
import java.util.Scanner;

public class SecondLargest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;
        
        for(int num : arr) {
            if(num > largest) {
                secondLargest = largest;
                largest = num;
            } else if(num > secondLargest && num != largest) {
                secondLargest = num;
            }
        }
        
        System.out.println("Second largest: " + secondLargest);
    }
}
```



--- 
2. Remove duplicates and print new size:
```java
import java.util.Scanner;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int newSize = 0;
        for(int i=0; i<n; i++) {
            boolean isDuplicate = false;
            for(int j=0; j<newSize; j++) {
                if(arr[i] == arr[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if(!isDuplicate) {
                arr[newSize] = arr[i];
                newSize++;
            }
        }
        
        System.out.println("New array size: " + newSize);
    }
}
```



---
3. Rotate array by K positions:
```java
import java.util.Scanner;

public class RotateArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        System.out.print("Enter K: ");
        int k = sc.nextInt();
        k = k % n;
        
        int[] temp = new int[n];
        for(int i=0; i<n; i++) {
            temp[(i+k)%n] = arr[i];
        }
        
        System.out.println("Rotated array:");
        for(int num : temp) {
            System.out.print(num + " ");
        }
    }
}
```




----
4. Merge two sorted arrays:
```java
import java.util.Scanner;

public class MergeSortedArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter size of first array: ");
        int n1 = sc.nextInt();
        int[] arr1 = new int[n1];
        System.out.println("Enter sorted array elements:");
        for(int i=0; i<n1; i++) {
            arr1[i] = sc.nextInt();
        }
        
        System.out.print("Enter size of second array: ");
        int n2 = sc.nextInt();
        int[] arr2 = new int[n2];
        System.out.println("Enter sorted array elements:");
        for(int i=0; i<n2; i++) {
            arr2[i] = sc.nextInt();
        }
        
        int[] result = new int[n1+n2];
        int i=0, j=0, k=0;
        
        while(i<n1 && j<n2) {
            if(arr1[i] < arr2[j]) {
                result[k++] = arr1[i++];
            } else {
                result[k++] = arr2[j++];
            }
        }
        
        while(i<n1) {
            result[k++] = arr1[i++];
        }
        
        while(j<n2) {
            result[k++] = arr2[j++];
        }
        
        System.out.println("Merged array:");
        for(int num : result) {
            System.out.print(num + " ");
        }
    }
}
```




---
5. Count frequency of elements:
```java
import java.util.Scanner;

public class FrequencyCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        boolean[] visited = new boolean[n];
        
        for(int i=0; i<n; i++) {
            if(visited[i]) continue;
            
            int count = 1;
            for(int j=i+1; j<n; j++) {
                if(arr[i] == arr[j]) {
                    count++;
                    visited[j] = true;
                }
            }
            System.out.println(arr[i] + " appears " + count + " times");
        }
    }
}
```




---
6. Find pairs with given sum:
```java
import java.util.Scanner;

public class FindPairs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        System.out.print("Enter target sum: ");
        int target = sc.nextInt();
        
        boolean[] used = new boolean[n];
        
        System.out.println("Pairs with sum " + target + ":");
        for(int i=0; i<n; i++) {
            if(used[i]) continue;
            
            for(int j=i+1; j<n; j++) {
                if(!used[j] && arr[i] + arr[j] == target) {
                    System.out.println("(" + arr[i] + ", " + arr[j] + ")");
                    used[i] = true;
                    used[j] = true;
                    break;
                }
            }
        }
    }
}
```





---
7. Check if two arrays are equal:
```java
import java.util.Scanner;

public class CheckArraysEqual {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter size of first array: ");
        int n1 = sc.nextInt();
        int[] arr1 = new int[n1];
        System.out.println("Enter array elements:");
        for(int i=0; i<n1; i++) {
            arr1[i] = sc.nextInt();
        }
        
        System.out.print("Enter size of second array: ");
        int n2 = sc.nextInt();
        int[] arr2 = new int[n2];
        System.out.println("Enter array elements:");
        for(int i=0; i<n2; i++) {
            arr2[i] = sc.nextInt();
        }
        
        boolean equal = true;
        
        if(n1 != n2) {
            equal = false;
        } else {
            for(int i=0; i<n1; i++) {
                if(arr1[i] != arr2[i]) {
                    equal = false;
                    break;
                }
            }
        }
        
        if(equal) {
            System.out.println("Arrays are equal");
        } else {
            System.out.println("Arrays are not equal");
        }
    }
}
```

8. Bubble sort with each pass:
```java
import java.util.Scanner;

public class BubbleSortPass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        for(int i=0; i<n-1; i++) {
            for(int j=0; j<n-i-1; j++) {
                if(arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
            System.out.print("Pass " + (i+1) + ": ");
            for(int num : arr) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
```

9. Separate even and odd numbers:
```java
import java.util.Scanner;

public class SeparateEvenOdd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int evenCount = 0;
        int oddCount = 0;
        
        for(int num : arr) {
            if(num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        
        int[] evenArr = new int[evenCount];
        int[] oddArr = new int[oddCount];
        
        int e = 0, o = 0;
        for(int num : arr) {
            if(num % 2 == 0) {
                evenArr[e++] = num;
            } else {
                oddArr[o++] = num;
            }
        }
        
        System.out.println("Even numbers:");
        for(int num : evenArr) {
            System.out.print(num + " ");
        }
        
        System.out.println("\nOdd numbers:");
        for(int num : oddArr) {
            System.out.print(num + " ");
        }
    }
}
```

10. Longest increasing subsequence:
```java
import java.util.Scanner;

public class LongestIncreasingSubsequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int[] lis = new int[n];
        for(int i=0; i<n; i++) {
            lis[i] = 1;
        }
        
        for(int i=1; i<n; i++) {
            for(int j=0; j<i; j++) {
                if(arr[i] > arr[j] && lis[i] < lis[j] + 1) {
                    lis[i] = lis[j] + 1;
                }
            }
        }
        
        int max = 0;
        for(int i=0; i<n; i++) {
            if(lis[i] > max) {
                max = lis[i];
            }
        }
        
        System.out.println("Length of LIS: " + max);
    }
}
```

11. Maximum sum subarray (Kadane's):
```java
import java.util.Scanner;

public class KadaneAlgorithm {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];
        
        for(int i=1; i<n; i++) {
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        
        System.out.println("Maximum sum: " + maxSoFar);
    }
}
```

12. Check sparse matrix:
```java
import java.util.Scanner;

public class SparseMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        int zeroCount = 0;
        int totalElements = rows * cols;
        
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(matrix[i][j] == 0) {
                    zeroCount++;
                }
            }
        }
        
        if(zeroCount > totalElements/2) {
            System.out.println("It is a sparse matrix");
        } else {
            System.out.println("It is not a sparse matrix");
        }
    }
}
```

13. Add two matrices:
```java
import java.util.Scanner;

public class AddMatrices {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        int[][] mat1 = new int[rows][cols];
        int[][] mat2 = new int[rows][cols];
        int[][] sum = new int[rows][cols];
        
        System.out.println("Enter first matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                mat1[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("Enter second matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                mat2[i][j] = sc.nextInt();
            }
        }
        
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                sum[i][j] = mat1[i][j] + mat2[i][j];
            }
        }
        
        System.out.println("Sum matrix:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                System.out.print(sum[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

14. Multiply two matrices:
```java
import java.util.Scanner;

public class MultiplyMatrices {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter rows and columns of first matrix: ");
        int r1 = sc.nextInt();
        int c1 = sc.nextInt();
        
        System.out.print("Enter rows and columns of second matrix: ");
        int r2 = sc.nextInt();
        int c2 = sc.nextInt();
        
        if(c1 != r2) {
            System.out.println("Multiplication not possible");
            return;
        }
        
        int[][] mat1 = new int[r1][c1];
        int[][] mat2 = new int[r2][c2];
        int[][] product = new int[r1][c2];
        
        System.out.println("Enter first matrix elements:");
        for(int i=0; i<r1; i++) {
            for(int j=0; j<c1; j++) {
                mat1[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("Enter second matrix elements:");
        for(int i=0; i<r2; i++) {
            for(int j=0; j<c2; j++) {
                mat2[i][j] = sc.nextInt();
            }
        }
        
        for(int i=0; i<r1; i++) {
            for(int j=0; j<c2; j++) {
                for(int k=0; k<c1; k++) {
                    product[i][j] += mat1[i][k] * mat2[k][j];
                }
            }
        }
        
        System.out.println("Product matrix:");
        for(int i=0; i<r1; i++) {
            for(int j=0; j<c2; j++) {
                System.out.print(product[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

15. Row with maximum sum:
```java
import java.util.Scanner;

public class MaxRowSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        int maxSum = Integer.MIN_VALUE;
        int maxRow = 0;
        
        for(int i=0; i<rows; i++) {
            int rowSum = 0;
            for(int j=0; j<cols; j++) {
                rowSum += matrix[i][j];
            }
            if(rowSum > maxSum) {
                maxSum = rowSum;
                maxRow = i;
            }
        }
        
        System.out.println("Row " + maxRow + " has maximum sum: " + maxSum);
    }
}
```

16. Check symmetric matrix:
```java
import java.util.Scanner;

public class SymmetricMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        if(rows != cols) {
            System.out.println("Matrix is not symmetric");
            return;
        }
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        boolean symmetric = true;
        
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(matrix[i][j] != matrix[j][i]) {
                    symmetric = false;
                    break;
                }
            }
            if(!symmetric) break;
        }
        
        if(symmetric) {
            System.out.println("Matrix is symmetric");
        } else {
            System.out.println("Matrix is not symmetric");
        }
    }
}
```

17. Print boundary elements:
```java
import java.util.Scanner;

public class BoundaryElements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("Boundary elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if(i==0 || i==rows-1 || j==0 || j==cols-1) {
                    System.out.print(matrix[i][j] + " ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
}
```

18. In-place transpose:
```java
import java.util.Scanner;

public class InPlaceTranspose {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of square matrix: ");
        int n = sc.nextInt();
        
        int[][] matrix = new int[n][n];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        System.out.println("Transpose:");
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

19. Sort each row individually:
```java
import java.util.Scanner;

public class SortRows {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows and columns: ");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("Enter matrix elements:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols-1; j++) {
                for(int k=0; k<cols-j-1; k++) {
                    if(matrix[i][k] > matrix[i][k+1]) {
                        int temp = matrix[i][k];
                        matrix[i][k] = matrix[i][k+1];
                        matrix[i][k+1] = temp;
                    }
                }
            }
        }
        
        System.out.println("Matrix with sorted rows:");
        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

20. Move zeroes to end:
```java
import java.util.Scanner;

public class MoveZeroes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array elements:");
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int count = 0;
        
        for(int i=0; i<n; i++) {
            if(arr[i] != 0) {
                arr[count++] = arr[i];
            }
        }
        
        while(count < n) {
            arr[count++] = 0;
        }
        
        System.out.println("Array after moving zeroes:");
        for(int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

21. Student class:
```java
import java.util.Scanner;

class Student {
    String name;
    int roll;
    int marks1, marks2, marks3;
    
    void inputDetails() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter roll: ");
        roll = sc.nextInt();
        System.out.print("Enter marks of 3 subjects: ");
        marks1 = sc.nextInt();
        marks2 = sc.nextInt();
        marks3 = sc.nextInt();
    }
    
    float calculatePercentage() {
        return (marks1 + marks2 + marks3) / 3.0f;
    }
    
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Roll: " + roll);
        System.out.println("Marks: " + marks1 + ", " + marks2 + ", " + marks3);
        System.out.println("Percentage: " + calculatePercentage() + "%");
    }
    
    public static void main(String[] args) {
        Student s = new Student();
        s.inputDetails();
        s.displayDetails();
    }
}
```

22. Rectangle class:
```java
import java.util.Scanner;

class Rectangle {
    float length;
    float breadth;
    
    void input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length: ");
        length = sc.nextFloat();
        System.out.print("Enter breadth: ");
        breadth = sc.nextFloat();
    }
    
    float computeArea() {
        return length * breadth;
    }
    
    float computePerimeter() {
        return 2 * (length + breadth);
    }
    
    void display() {
        System.out.println("Area: " + computeArea());
        System.out.println("Perimeter: " + computePerimeter());
    }
    
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.input();
        r.display();
    }
}
```

23. Account class:
```java
import java.util.Scanner;

class Account {
    int accountNo;
    String name;
    float balance;
    
    void openAccount() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter account number: ");
        accountNo = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter initial balance: ");
        balance = sc.nextFloat();
    }
    
    void deposit(float amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }
    
    void withdraw(float amount) {
        if(amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient balance");
        }
    }
    
    void displayBalance() {
        System.out.println("Balance: " + balance);
    }
    
    public static void main(String[] args) {
        Account acc = new Account();
        acc.openAccount();
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter deposit amount: ");
        float dep = sc.nextFloat();
        acc.deposit(dep);
        
        System.out.print("Enter withdrawal amount: ");
        float wd = sc.nextFloat();
        acc.withdraw(wd);
        
        acc.displayBalance();
    }
}
```

24. Box class with comparison:
```java
import java.util.Scanner;

class Box {
    float height;
    float width;
    float depth;
    
    void input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter height: ");
        height = sc.nextFloat();
        System.out.print("Enter width: ");
        width = sc.nextFloat();
        System.out.print("Enter depth: ");
        depth = sc.nextFloat();
    }
    
    float computeVolume() {
        return height * width * depth;
    }
    
    void display() {
        System.out.println("Volume: " + computeVolume());
    }
    
    public static void main(String[] args) {
        System.out.println("Enter details for Box 1:");
        Box box1 = new Box();
        box1.input();
        
        System.out.println("\nEnter details for Box 2:");
        Box box2 = new Box();
        box2.input();
        
        float vol1 = box1.computeVolume();
        float vol2 = box2.computeVolume();
        
        System.out.println("\nBox 1 volume: " + vol1);
        System.out.println("Box 2 volume: " + vol2);
        
        if(vol1 > vol2) {
            System.out.println("Box 1 has larger volume");
        } else if(vol2 > vol1) {
            System.out.println("Box 2 has larger volume");
        } else {
            System.out.println("Both boxes have equal volume");
        }
    }
}
```

