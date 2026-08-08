# Suryansh Mithu
# Roll : 24155060

## Day - 3
---

```txt
# inAsce.txt

```

```txt
# inDesc.txt

```


```txt
# inRand.txt

```


### 3.1  Aim of the program: Write a menu driven program to sort list of array elements using Merge.

```c
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r, long long *comparisons) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));
    for (i = 0; i < n1; i++) {
        L[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++) {
        R[j] = arr[m + 1 + j];
    }
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        (*comparisons)++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
    free(L);
    free(R);
}

void mergeSort(int arr[], int l, int r, long long *comparisons) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m, comparisons);
        mergeSort(arr, m + 1, r, comparisons);
        merge(arr, l, m, r, comparisons);
    }
}

int main() {
    int choice;
    while (1) {
        printf("MAIN MENU (MERGE SORT)\n");
        printf("1. Ascending Data\n");
        printf("2. Descending Data\n");
        printf("3. Random Data\n");
        printf("4. ERROR (EXIT)\n");
        printf("Enter option: ");
        if (scanf("%d", &choice) != 1) {
            break;
        }
        if (choice == 4) {
            break;
        }
        char *in_file = NULL;
        char *out_file = NULL;
        if (choice == 1) {
            in_file = "inAsce.txt";
            out_file = "outMergeAsce.txt";
        } else if (choice == 2) {
            in_file = "inDesc.txt";
            out_file = "outMergeDesc.txt";
        } else if (choice == 3) {
            in_file = "inRand.txt";
            out_file = "outMergeRand.txt";
        } else {
            printf("Invalid option.\n\n");
            continue;
        }
        FILE *fp = fopen(in_file, "r");
        if (!fp) {
            printf("Error opening file %s\n\n", in_file);
            continue;
        }
        int arr[1000];
        int n = 0;
        while (fscanf(fp, "%d", &arr[n]) == 1) {
            n++;
            if (n >= 1000) {
                break;
            }
        }
        fclose(fp);

```

### Output : 
```
# outAsce.txt

```

```
# outDesc.txt

```

```
# outRand.txt

```




---
#### 3.2 Aim of the program: Write a menu driven program to sort a list of elements in ascending  order using Quick Sort technique. Each choice for the input data has its own disc file.

```c
#include <stdio.h>
#include <stdlib.h>

int partition(int arr[], int low, int high, long long *comparisons, long long *worst_splits, long long *total_splits) {
    int pivot = arr[low];
    int i = low;
    for (int j = low + 1; j <= high; j++) {
        (*comparisons)++;
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[low];
    arr[low] = arr[i];
    arr[i] = temp;
    int left_size = i - low;
    int right_size = high - i;
    if (left_size == 0 || right_size == 0) {
        (*worst_splits)++;
    }
    (*total_splits)++;
    return i;
}

void quickSort(int arr[], int low, int high, long long *comparisons, long long *worst_splits, long long *total_splits) {
    if (low < high) {
        int pi = partition(arr, low, high, comparisons, worst_splits, total_splits);
        quickSort(arr, low, pi - 1, comparisons, worst_splits, total_splits);
        quickSort(arr, pi + 1, high, comparisons, worst_splits, total_splits);
    }
}

int main() {
    int choice;
    while (1) {
        printf("MAIN MENU (QUICK SORT)\n");
        printf("1. Ascending Data\n");
        printf("2. Descending Data\n");
        printf("3. Random Data\n");
        printf("4. ERROR (EXIT)\n");
        printf("Enter option: ");
        if (scanf("%d", &choice) != 1) {
            break;
        }
        if (choice == 4) {
            break;
        }
        char *in_file = NULL;
        char *out_file = NULL;
        if (choice == 1) {
            in_file = "inAsce.txt";
            out_file = "outQuickAsce.dat";
        } else if (choice == 2) {
            in_file = "inDesc.txt";
            out_file = "outQuickDesc.txt";
        } else if (choice == 3) {
            in_file = "inRand.dat";
            out_file = "outQuickRand.txt";
        } else {
            printf("Invalid option.\n\n");
            continue;
        }
        FILE *fp = fopen(in_file, "r");
        if (!fp) {
            printf("Error opening file %s\n\n", in_file);
            continue;
        }
        int arr[1000];
        int n = 0;
        while (fscanf(fp, "%d", &arr[n]) == 1) {
            n++;
            if (n >= 1000) {
                break;
            }
        }
        fclose(fp);
        printf("Before Sorting: ");
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        long long comparisons = 0;
        long long worst_splits = 0;
        long long total_splits = 0;
        quickSort(arr, 0, n - 1, &comparisons, &worst_splits, &total_splits);
        FILE *out_fp = fopen(out_file, "w");
        if (out_fp) {
            for (int i = 0; i < n; i++) {
                fprintf(out_fp, "%d ", arr[i]);
            }
            fclose(out_fp);
        }
        printf("After Sorting: ");
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        printf("Number of Comparisons: %lld\n", comparisons);
        if (total_splits > 0 && (worst_splits * 100 / total_splits) > 50) {
            printf("Scenario: Worst-case\n\n");
        } else {
            printf("Scenario: Best-case\n\n");
        }
    }
    return 0;
}

```

### Output :
### Output : 
```
# outAsce.txt

```

```
# outDesc.txt

```

```
# outRand.txt

```



---
# 3.3 Binary search through an array using a file. 

```txt
# binarySearch.txt
10
1 3 5 7 9 11 23 45 70 90 900
```

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

### Output :
![[Pasted image 20260808145524.png]]


---
# 3.4 WAP to take n pair of x and y from a file then raise the power of x to y for each of the n pair using divide and conquer method.

```txt
# pairs.txt
3
2 5
4 6
7 3

```

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

### Output :
![[Pasted image 20260808145431.png]]

---