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

#include <stdio.h>
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

#include <stdio.h>
#include <string.h>

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

#include <stdio.h>
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

#include <stdio.h>
#include <string.h>

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
