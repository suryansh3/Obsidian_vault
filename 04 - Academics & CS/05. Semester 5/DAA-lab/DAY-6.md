```c
 #inlcude <stdio.h>

int firstOccur(int arr[],int n, int key)
{
  int low = 0, high = n-1, result = -1;

  while(low<=high)
  {
    int mid = low + (high-low)/2;
    if(arr[mid] == key)
    {  result = mid;
    high = mid -1;}
    else if(arr[mid]<key)
    {
      low = mid + 1;
    }
    else 
      high = mid -1;
  }
  return result;   
}
  int main()
  {
  int arr[] = {1,2,2,2,4,5,6};
  int n = (sizeof(arr))/(sizeof(arr[0]));
  int key = 2;
    printf("First Occurence = index %d",firstOccur(arr,n,key));
  return 0;
  }
```



---
```c 
#inlcude <stdio.h>

int searchRotated(int arr[],int n, int key)
{
  int low = 0, high = n-1;

  while(low<=high)
  {
    int mid = low + (high-low)/2;
    if(arr[mid] == key)
      return mid;

    if (arr[low] < arr[mid])
    {
      if( key >= arr[low] && key < arr[mid])
       high = mid + 1;
      else  
       low = mid -1;
    } 
    else 
    { 
      if(key > arr[mid] && key < arr[high])
      low = mid +1;
      else high = mid -1;
    }

      
  }
  return -1;
  }

  int main()
{
  int arr[] = {6,7,8,1,2,3,4,5};
  int n = sizeof(arr)/sizeof(arr[0]);
  int key = 3;
  printf("Element found at index %d ",searchRotated(arr,n,key));
  return 0;
}
```



---

```c 
#inlcude <stdio.h>

int integerSqrt(int n) 
{
  if (n< 0) 
  return -1;
  int low = 0, high = n, ans = 0;
  while (low <= high) {
  int mid = low + (high - low) / 2;
    if (mid * mid <= n) {
      ans = mid;
    low = mid + 1;
    } 
    else {
    high = mid - 1;
    }
    }
    return ans;
}

int main() {
    int N = 27;
    printf("N = %d Output: %d\n", N, integerSqrt(N));
    return 0;
}
```


----
```c 
#inlcude <stdio.h>

int smallestGreat(int arr[], int n, int key)
{
  int low = 0, high = n-1, ans = -1;
  
  while(low<=high)
  {
    int mid = low + (high-low)/2;
     if (arr[mid]>=key)
    { ans = arr[mid];
      high = mid -1;
    }
    else 
    {
      low = mid + 1;
    }
  }
 return ans;
}

int main()
{
 int arr[] = {2,5,8,12,16,20};
  int n = sizeof(arr)/sizeof(arr[0]);
  int key = 10;
  int result = smallestGreat(arr,n,key);
  if(result != 0)
    printf("K = %d  Output : %d",key,result);
  else
    printf("No element found int the given array");

}
```


---
```c 
#inlcude <stdio.h>
void selectionSort(int arr[], int n) {
int comparisons = 0, swaps = 0;
    
for (int i = 0; i < n - 1; i++) {
int min_index = i;
  for (int j = i + 1; j < n; j++) {
    comparisons++;
      if (arr[j] < arr[min_index]) {
      min_index = j;
        }
      }
  if (min_index != i) {
int temp = arr[i];
      arr[i] = arr[min_index];
    arr[min_index] = temp;
  swaps++;
      }
    }
    
    printf("Sorted Array: \n");
    for (int i = 0; i < n; i++) 
    printf("%d ", arr[i]);
    printf("\nTotal Comparisons: %d, Total Swaps: %d", comparisons, swaps);
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    return 0;
}
```

---

```c 
#inlcude <stdio.h>

void mergeArrays(int A[], int n1, int B[], int n2, int C[]) {
    int i = 0, j = 0, k = 0;

while (i < n1 && j < n2) {
 if (A[i] <= B[j]) 
      C[k++] = A[i++];
  else 
      C[k++] = B[j++];
}
while (i < n1) 
    C[k++] = A[i++];
while (j < n2) 
    C[k++] = B[j++];
}

int main() {
  int A[] = {1, 4, 7, 10};
int B[] = {2, 3, 8, 9};
  int n1 = sizeof(A) / sizeof(A[0]);
int n2 = sizeof(B) / sizeof(B[0]);
int C[n1 + n2];
 printf("A[] : ");
  for (int i=0;i<n1;i++) 
  {printf("%d  ", A[i]);}
  printf("B[] : ");
 for (int i = 1; i < n2; i++) {
    printf("%d  ", B[i]);
  } 
 
mergeArrays(A, n1, B, n2, C);
printf("Output: ");
  for (int i = 0; i < n1 + n2; i++) 
    printf("%d ", C[i]);
  printf("\n");
  return 0;
}
```


---
```c 
#inlcude <stdio.h>

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void buildMaxHeap(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

int main() {
    int arr[] = {4, 10, 3, 5, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    buildMaxHeap(arr, n);
    printf("Max Heap: ");
    for (int i = 1; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```



---
```c 
#inlcude <stdio.h>
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}
int findKthLargest(int arr[], int n, int k) {
    for (int i = n / 2 - 1; i >= 0; i--) {
  heapify(arr, n, i);
    }  
    for (int i = 0; i < k - 1; i++) {
    int temp = arr[0];
     arr[0] = arr[n - 1 - i];
    arr[n - 1 - i] = temp;
      heapify(arr, n - 1 - i, 0);
    }
    return arr[0];
}
int main() {
    int arr[] = {10, 4, 7, 2, 15, 8, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    int K = 3;
    printf("Kth Largest (K=%d): %d\n", K, findKthLargest(arr, n, K));
    return 0;
}
```



---
```c 
#inlcude <stdio.h>
#inlcude <string.h>

typedef struct {
    char item[20];
    int priority;
} Node;

typedef struct {
    Node heap[100];
    int size;
} Priority;

void swap(Node *a, Node *b) {
    Node temp = *a;
    *a = *b;
    *b = temp;
}

void insert(Priority *pq, const char item[], int priority) {
    strcpy(pq->heap[pq->size].item, item);
    pq->heap[pq->size].priority = priority;
    int curr = pq->size;
    pq->size++;

    while (curr > 0) {
        int parent = (curr - 1) / 2;
        if (pq->heap[curr].priority > pq->heap[parent].priority) {
            swap(&pq->heap[curr], &pq->heap[parent]);
            curr = parent;
        } else break;
    }
}

void heapifyPQ(Priority *pq, int idx) {
    int largest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < pq->size && pq->heap[left].priority > pq->heap[largest].priority) largest = left;
    if (right < pq->size && pq->heap[right].priority > pq->heap[largest].priority) largest = right;

    if (largest != idx) {
        swap(&pq->heap[idx], &pq->heap[largest]);
        heapifyPQ(pq, largest);
    }
}

Node deleteMax(Priority *pq) {
    Node maxNode = pq->heap[0];
    pq->heap[0] = pq->heap[pq->size - 1];
    pq->size--;
    heapifyPQ(pq, 0);
    return maxNode;
}

void peek(Priority *pq) {
    if (pq->size > 0)
        printf("PEEK: %s (priority: %d)\n", pq->heap[0].item, pq->heap[0].priority);
}

void display(Priority *pq) {
    printf(": ");
    for (int i = 0; i < pq->size; i++) {
        printf("%s(p:%d) ", pq->heap[i].item, pq->heap[i].priority);
    }
    printf("\n");
}

int main() {
    Priority pq = {.size = 0};

    printf(" Inserting 5 Elements \n");
    insert(&pq, "A", 2); display(&pq);
    insert(&pq, "B", 5); display(&pq);
    insert(&pq, "C", 1); display(&pq);
    insert(&pq, "D", 4); display(&pq);
    insert(&pq, "E", 3); display(&pq);

    printf("\n Peek Top Element \n");
    peek(&pq);

    printf("\n Deleting Elements \n");
    Node deleted = deleteMax(&pq);
    printf("Deleted: %s (p:%d)\n", deleted.item, deleted.priority);
    display(&pq);

    deleted = deleteMax(&pq);
    printf("Deleted: %s (p:%d)\n", deleted.item, deleted.priority);
    display(&pq);

    return 0;
}
```