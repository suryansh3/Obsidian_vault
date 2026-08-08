# Suryansh Mithu
# Roll : 24155060

## Day - 3
---

# 3.1  Aim of the program: Write a menu driven program to sort list of array elements using Merge.

```text 

```





# 3.3 Binary search through an array using a file. 

```c
#include <stdio.h>

int binarySearch(int arr[], int n, int target) {
  int low = 0, high = n - 1;
  while (low4<= high) {
  int mid = low + (high - low) / 2;
  if (arr[mid] == target) {
  return mid;
  }
  if (arr[mid] < target) {
  low = mid + 1;
  } 
  else {
        high = mid - 1;
        }
    }
    return -1; 
}
int main() {
    int arr[100];
    int n = 0;
    FILE *fp = fopen("binarySearch.txt", "r");
    if (!fp) {
        printf("Error opening file \n");
        return 1;
    }
    while(n<100 && fscanf(fp, "%d", &arr[n])==1)
    n++;
    fclose(fp);
    if (n == 0) {
        printf("No sorted integers read from the file!\n");
        return 1;
    }
    printf("Sorted Array  ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    int target;
    printf("Enter the integer to search: ");
    if (scanf("%d", &target) != 1) {
        printf("Invalid input.\n");
        return 1;
    }
    int index = binarySearch(arr, n, target);
    if (index != -1) {
        printf("Element %d found at index %d.\n", target, index);
    } else {
        printf("Element %d not found in the array.\n", target);
    }
    return 0;
}
```

# 3.4 WAP to take n pair of x and y from a file then raise the power of x to y for each of the n pair using divide and conquer method.

```c
#include <stdio.h>
#include <stdlib.h>
int power(int x, int y) {
    if (y == 0) return 1;
    if (y == 1) return x;
    int half = power(x, y / 2);
    if (y % 2 == 0)
    return half * half;
    else
    return x * half * half;
}

int main() {
    FILE *fp;
    int n,x,y;
    fp = fopen("pairs.txt", "r");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fscanf(fp, "%d", &n);
    printf("Computing powers for %d pairs:\n", n);
    for (int i = 0; i < n; i++) {
    fscanf(fp, "%d %d", &x, &y);
    int result = power(x, y);
     printf("%d^%d = %d\n", x, y, result);
    }
    fclose(fp);
    return 0;
}


```