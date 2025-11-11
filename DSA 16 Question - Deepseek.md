Deepseek

## 1. Binary Search

```c
#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    
    return -1;
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 45, 67, 89};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    
    int result = binarySearch(arr, size, target);
    
    if (result != -1)
        printf("Element %d found at index %d\n", target, result);
    else
        printf("Element %d not found in array\n", target);
    
    return 0;
}
```

## 2. Quick Sort

```c
#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, size);
    
    quickSort(arr, 0, size - 1);
    
    printf("Sorted array: ");
    printArray(arr, size);
    
    return 0;
}
```

## 3. Merge Sort

```c
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));
    
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    i = 0;
    j = 0;
    k = left;
    
    while (i < n1 && j < n2) {
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

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, size);
    
    mergeSort(arr, 0, size - 1);
    
    printf("Sorted array: ");
    printArray(arr, size);
    
    return 0;
}
```

## 4. Insertion Sort (Ascending & Descending)

```c
#include <stdio.h>

void insertionSortAscending(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void insertionSortDescending(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] < key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr1) / sizeof(arr1[0]);
    
    printf("Original array: ");
    printArray(arr1, size);
    
    insertionSortAscending(arr1, size);
    printf("Ascending order: ");
    printArray(arr1, size);
    
    int arr2[] = {64, 34, 25, 12, 22, 11, 90};
    insertionSortDescending(arr2, size);
    printf("Descending order: ");
    printArray(arr2, size);
    
    return 0;
}
```

## 5. Selection Sort (Ascending & Descending)

```c
#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSortAscending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        swap(&arr[min_idx], &arr[i]);
    }
}

void selectionSortDescending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int max_idx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] > arr[max_idx])
                max_idx = j;
        }
        swap(&arr[max_idx], &arr[i]);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr1) / sizeof(arr1[0]);
    
    printf("Original array: ");
    printArray(arr1, size);
    
    selectionSortAscending(arr1, size);
    printf("Ascending order: ");
    printArray(arr1, size);
    
    int arr2[] = {64, 34, 25, 12, 22, 11, 90};
    selectionSortDescending(arr2, size);
    printf("Descending order: ");
    printArray(arr2, size);
    
    return 0;
}
```

## 6. Undirected Graph - DFS Traversal

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int adjMatrix[MAX][MAX];
int visited[MAX];
int vertices;

void initializeGraph() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            adjMatrix[i][j] = 0;
        }
    }
}

void addEdge(int src, int dest) {
    adjMatrix[src][dest] = 1;
    adjMatrix[dest][src] = 1;
}

void DFS(int vertex) {
    visited[vertex] = 1;
    printf("%d ", vertex);
    
    for (int i = 0; i < vertices; i++) {
        if (adjMatrix[vertex][i] == 1 && !visited[i]) {
            DFS(i);
        }
    }
}

int main() {
    initializeGraph();
    vertices = 5;
    
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(1, 4);
    addEdge(2, 4);
    
    for (int i = 0; i < vertices; i++) {
        visited[i] = 0;
    }
    
    printf("DFS Traversal of Undirected Graph: ");
    DFS(0);
    printf("\n");
    
    return 0;
}
```

## 7. Undirected Graph - BFS Traversal

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int adjMatrix[MAX][MAX];
int visited[MAX];
int vertices;

typedef struct Queue {
    int items[MAX];
    int front;
    int rear;
} Queue;

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}

int isEmpty(Queue* q) {
    return q->rear == -1;
}

void enqueue(Queue* q, int value) {
    if (q->rear == MAX - 1)
        return;
    if (q->front == -1)
        q->front = 0;
    q->rear++;
    q->items[q->rear] = value;
}

int dequeue(Queue* q) {
    if (isEmpty(q))
        return -1;
    int item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = q->rear = -1;
    }
    return item;
}

void initializeGraph() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            adjMatrix[i][j] = 0;
        }
    }
}

void addEdge(int src, int dest) {
    adjMatrix[src][dest] = 1;
    adjMatrix[dest][src] = 1;
}

void BFS(int startVertex) {
    Queue* q = createQueue();
    
    visited[startVertex] = 1;
    enqueue(q, startVertex);
    
    while (!isEmpty(q)) {
        int currentVertex = dequeue(q);
        printf("%d ", currentVertex);
        
        for (int i = 0; i < vertices; i++) {
            if (adjMatrix[currentVertex][i] == 1 && !visited[i]) {
                visited[i] = 1;
                enqueue(q, i);
            }
        }
    }
    free(q);
}

int main() {
    initializeGraph();
    vertices = 5;
    
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(1, 4);
    addEdge(2, 4);
    
    for (int i = 0; i < vertices; i++) {
        visited[i] = 0;
    }
    
    printf("BFS Traversal of Undirected Graph: ");
    BFS(0);
    printf("\n");
    
    return 0;
}
```

## 8. Directed Graph - DFS Traversal

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int adjMatrix[MAX][MAX];
int visited[MAX];
int vertices;

void initializeGraph() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            adjMatrix[i][j] = 0;
        }
    }
}

void addEdge(int src, int dest) {
    adjMatrix[src][dest] = 1;
}

void DFS(int vertex) {
    visited[vertex] = 1;
    printf("%d ", vertex);
    
    for (int i = 0; i < vertices; i++) {
        if (adjMatrix[vertex][i] == 1 && !visited[i]) {
            DFS(i);
        }
    }
}

int main() {
    initializeGraph();
    vertices = 5;
    
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(2, 1);
    addEdge(3, 4);
    
    for (int i = 0; i < vertices; i++) {
        visited[i] = 0;
    }
    
    printf("DFS Traversal of Directed Graph: ");
    DFS(0);
    printf("\n");
    
    return 0;
}
```

## 9. Directed Graph - BFS Traversal

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int adjMatrix[MAX][MAX];
int visited[MAX];
int vertices;

typedef struct Queue {
    int items[MAX];
    int front;
    int rear;
} Queue;

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}

int isEmpty(Queue* q) {
    return q->rear == -1;
}

void enqueue(Queue* q, int value) {
    if (q->rear == MAX - 1)
        return;
    if (q->front == -1)
        q->front = 0;
    q->rear++;
    q->items[q->rear] = value;
}

int dequeue(Queue* q) {
    if (isEmpty(q))
        return -1;
    int item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = q->rear = -1;
    }
    return item;
}

void initializeGraph() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            adjMatrix[i][j] = 0;
        }
    }
}

void addEdge(int src, int dest) {
    adjMatrix[src][dest] = 1;
}

void BFS(int startVertex) {
    Queue* q = createQueue();
    
    visited[startVertex] = 1;
    enqueue(q, startVertex);
    
    while (!isEmpty(q)) {
        int currentVertex = dequeue(q);
        printf("%d ", currentVertex);
        
        for (int i = 0; i < vertices; i++) {
            if (adjMatrix[currentVertex][i] == 1 && !visited[i]) {
                visited[i] = 1;
                enqueue(q, i);
            }
        }
    }
    free(q);
}

int main() {
    initializeGraph();
    vertices = 5;
    
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(2, 1);
    addEdge(3, 4);
    
    for (int i = 0; i < vertices; i++) {
        visited[i] = 0;
    }
    
    printf("BFS Traversal of Directed Graph: ");
    BFS(0);
    printf("\n");
    
    return 0;
}
```

## 10. Binary Search Tree - Preorder Traversal

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* createNode(int data) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode* insert(TreeNode* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}

void preorder(TreeNode* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

int main() {
    TreeNode* root = NULL;
    int elements[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(elements) / sizeof(elements[0]);
    
    for (int i = 0; i < n; i++) {
        root = insert(root, elements[i]);
    }
    
    printf("Preorder traversal: ");
    preorder(root);
    printf("\n");
    
    return 0;
}
```

## 11. Binary Search Tree - Postorder Traversal

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* createNode(int data) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode* insert(TreeNode* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}

void postorder(TreeNode* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

int main() {
    TreeNode* root = NULL;
    int elements[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(elements) / sizeof(elements[0]);
    
    for (int i = 0; i < n; i++) {
        root = insert(root, elements[i]);
    }
    
    printf("Postorder traversal: ");
    postorder(root);
    printf("\n");
    
    return 0;
}
```

## 12. Binary Search Tree - Inorder Traversal

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* createNode(int data) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode* insert(TreeNode* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}

void inorder(TreeNode* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

int main() {
    TreeNode* root = NULL;
    int elements[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(elements) / sizeof(elements[0]);
    
    for (int i = 0; i < n; i++) {
        root = insert(root, elements[i]);
    }
    
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    
    return 0;
}
```

## 13. Priority Queue using Linked List

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    int priority;
    struct Node* next;
} Node;

Node* createNode(int data, int priority) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->priority = priority;
    newNode->next = NULL;
    return newNode;
}

void enqueue(Node** head, int data, int priority) {
    Node* newNode = createNode(data, priority);
    
    if (*head == NULL || (*head)->priority > priority) {
        newNode->next = *head;
        *head = newNode;
    } else {
        Node* current = *head;
        while (current->next != NULL && current->next->priority <= priority) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
    printf("Enqueued: (%d, priority %d)\n", data, priority);
}

int dequeue(Node** head) {
    if (*head == NULL) {
        printf("Queue is empty!\n");
        return -1;
    }
    
    Node* temp = *head;
    int data = temp->data;
    *head = (*head)->next;
    free(temp);
    return data;
}

void display(Node* head) {
    if (head == NULL) {
        printf("Queue is empty!\n");
        return;
    }
    
    printf("Priority Queue: ");
    while (head != NULL) {
        printf("(%d, %d) ", head->data, head->priority);
        head = head->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;
    
    enqueue(&head, 10, 2);
    enqueue(&head, 20, 1);
    enqueue(&head, 30, 3);
    enqueue(&head, 40, 2);
    
    display(head);
    
    printf("Dequeued: %d\n", dequeue(&head));
    printf("Dequeued: %d\n", dequeue(&head));
    
    display(head);
    
    return 0;
}
```

## 14. Linear Queue using Linked List

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
} Queue;

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

void enqueue(Queue* q, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
    printf("Enqueued: %d\n", data);
}

int dequeue(Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty!\n");
        return -1;
    }
    
    Node* temp = q->front;
    int data = temp->data;
    q->front = q->front->next;
    
    if (q->front == NULL) {
        q->rear = NULL;
    }
    
    free(temp);
    return data;
}

void display(Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty!\n");
        return;
    }
    
    Node* current = q->front;
    printf("Queue: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    Queue* q = createQueue();
    
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    enqueue(q, 40);
    
    display(q);
    
    printf("Dequeued: %d\n", dequeue(q));
    printf("Dequeued: %d\n", dequeue(q));
    
    display(q);
    
    return 0;
}
```

## 15. Stack using Linked List (Menu Driven)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Stack {
    Node* top;
} Stack;

Stack* createStack() {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->top = NULL;
    return s;
}

void push(Stack* s, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = s->top;
    s->top = newNode;
    printf("Pushed %d to stack\n", data);
}

int pop(Stack* s) {
    if (s->top == NULL) {
        printf("Stack is empty!\n");
        return -1;
    }
    
    Node* temp = s->top;
    int data = temp->data;
    s->top = s->top->next;
    free(temp);
    return data;
}

void display(Stack* s) {
    if (s->top == NULL) {
        printf("Stack is empty!\n");
        return;
    }
    
    Node* current = s->top;
    printf("Stack (top to bottom): ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    Stack* s = createStack();
    int choice, value;
    
    do {
        printf("\nStack Operations:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(s, value);
                break;
            case 2:
                value = pop(s);
                if (value != -1)
                    printf("Popped value: %d\n", value);
                break;
            case 3:
                display(s);
                break;
            case 4:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 4);
    
    // Free remaining nodes
    while (s->top != NULL) {
        pop(s);
    }
    free(s);
    
    return 0;
}
```

## 16. Infix to Postfix Conversion

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

typedef struct Stack {
    int top;
    char items[MAX];
} Stack;

Stack* createStack() {
    Stack* s = (Stack*)malloc(sizeof(Stack));
    s->top = -1;
    return s;
}

int isEmpty(Stack* s) {
    return s->top == -1;
}

int isFull(Stack* s) {
    return s->top == MAX - 1;
}

void push(Stack* s, char c) {
    if (isFull(s)) {
        printf("Stack overflow!\n");
        return;
    }
    s->items[++(s->top)] = c;
}

char pop(Stack* s) {
    if (isEmpty(s)) {
        printf("Stack underflow!\n");
        return '\0';
    }
    return s->items[(s->top)--];
}

char peek(Stack* s) {
    if (isEmpty(s))
        return '\0';
    return s->items[s->top];
}

int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

int isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

void infixToPostfix(char* infix, char* postfix) {
    Stack* s = createStack();
    int i = 0, j = 0;
    
    while (infix[i] != '\0') {
        char c = infix[i];
        
        if (isalnum(c)) {
            postfix[j++] = c;
        } else if (c == '(') {
            push(s, c);
        } else if (c == ')') {
            while (!isEmpty(s) && peek(s) != '(') {
                postfix[j++] = pop(s);
            }
            pop(s); // Remove '(' from stack
        } else if (isOperator(c)) {
            while (!isEmpty(s) && precedence(peek(s)) >= precedence(c)) {
                postfix[j++] = pop(s);
            }
            push(s, c);
        }
        i++;
    }
    
    while (!isEmpty(s)) {
        postfix[j++] = pop(s);
    }
    
    postfix[j] = '\0';
    free(s);
}

int main() {
    char infix[MAX], postfix[MAX];
    
    printf("Enter infix expression: ");
    fgets(infix, MAX, stdin);
    infix[strcspn(infix, "\n")] = 0;
    
    infixToPostfix(infix, postfix);
    printf("Postfix expression: %s\n", postfix);
    
    return 0;
}
```

