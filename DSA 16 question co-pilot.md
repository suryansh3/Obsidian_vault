
Smart GPT - 5 (Co-pilot)
---

### 🔍 1. Binary Search in Array

```c
#include <stdio.h>
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
int main() {
    int arr[] = {2, 4, 6, 8, 10}, key = 6;
    int index = binarySearch(arr, 5, key);
    printf(index != -1 ? "Found at index %d\n" : "Not found\n", index);
    return 0;
}
```

---

### ⚡ 2. Quick Sort

```c
#include <stdio.h>
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high], i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++; int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        int pi = i + 1;
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5}, n = 6;
    quickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
```

---

### 🔀 3. Merge Sort

```c
#include <stdio.h>
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m); mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7}, n = 6;
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
```

---

### 📈 4. Ascending Sort (Bubble Sort)

```c
#include <stdio.h>
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = temp;
            }
}
int main() {
    int arr[] = {5, 1, 4, 2, 8}, n = 5;
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
```

---

### 🔃 5. Selection Sort (Asc & Desc)

```c
#include <stdio.h>
void selectionSort(int arr[], int n, int asc) {
    for (int i = 0; i < n - 1; i++) {
        int idx = i;
        for (int j = i + 1; j < n; j++)
            if ((asc && arr[j] < arr[idx]) || (!asc && arr[j] > arr[idx]))
                idx = j;
        int temp = arr[idx]; arr[idx] = arr[i]; arr[i] = temp;
    }
}
int main() {
    int arr[] = {64, 25, 12, 22, 11}, n = 5;
    selectionSort(arr, n, 1); // Ascending
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
    selectionSort(arr, n, 0); // Descending
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
```

---

🧠 I’ll continue with graph traversal, BST, queue, stack, and infix-postfix conversion in the next message to keep things clean and digestible. Ready for part 2?

---

### 🌐 6 & 7. Undirected Graph – DFS & BFS Traversal

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int adj[MAX][MAX], visited[MAX], n;

void DFS(int v) {
    visited[v] = 1;
    printf("%d ", v);
    for (int i = 0; i < n; i++)
        if (adj[v][i] && !visited[i])
            DFS(i);
}

void BFS(int start) {
    int queue[MAX], front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;
    while (front < rear) {
        int v = queue[front++];
        printf("%d ", v);
        for (int i = 0; i < n; i++) {
            if (adj[v][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    printf("DFS: ");
    DFS(0);
    for (int i = 0; i < n; i++) visited[i] = 0;
    printf("\nBFS: ");
    BFS(0);
    return 0;
}
```

---

### 🎯 8 & 9. Directed Graph – DFS & BFS Traversal

(Same code as above works; just input directed adjacency matrix)

---

### 🌳 10–12. Binary Search Tree – Preorder, Inorder, Postorder

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *left, *right;
} Node;

Node* insert(Node* root, int data) {
    if (!root) {
        root = (Node*)malloc(sizeof(Node));
        root->data = data; root->left = root->right = NULL;
    } else if (data < root->data)
        root->left = insert(root->left, data);
    else
        root->right = insert(root->right, data);
    return root;
}

void preorder(Node* root) {
    if (root) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}
void inorder(Node* root) {
    if (root) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
void postorder(Node* root) {
    if (root) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

int main() {
    Node* root = NULL;
    int n, val;
    printf("Enter number of nodes: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &val);
        root = insert(root, val);
    }
    printf("Preorder: "); preorder(root); printf("\n");
    printf("Inorder: "); inorder(root); printf("\n");
    printf("Postorder: "); postorder(root); printf("\n");
    return 0;
}
```

---

### 🔁 13. Linear Queue Using Linked List

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node *front = NULL, *rear = NULL;

void enqueue(int val) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = val; temp->next = NULL;
    if (!rear) front = rear = temp;
    else { rear->next = temp; rear = temp; }
}

void dequeue() {
    if (!front) printf("Queue is empty\n");
    else {
        Node* temp = front;
        front = front->next;
        if (!front) rear = NULL;
        free(temp);
    }
}

void display() {
    Node* temp = front;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    enqueue(10); enqueue(20); enqueue(30);
    display(); dequeue(); display();
    return 0;
}
```

---

### 📚 14. Stack Using Linked List

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* top = NULL;

void push(int val) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = val; temp->next = top;
    top = temp;
}

void pop() {
    if (!top) printf("Stack is empty\n");
    else {
        Node* temp = top;
        top = top->next;
        free(temp);
    }
}

void display() {
    Node* temp = top;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    push(10); push(20); push(30);
    display(); pop(); display();
    return 0;
}
```

---

### 🧮 15. Infix to Postfix Using Stack

```c
#include <stdio.h>
#include <ctype.h>
#define SIZE 100

char stack[SIZE]; int top = -1;

void push(char c) { stack[++top] = c; }
char pop() { return stack[top--]; }
char peek() { return stack[top]; }

int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}

void infixToPostfix(char* expr) {
    for (int i = 0; expr[i] != '\0'; i++) {
        char c = expr[i];
        if (isalnum(c)) printf("%c", c);
        else if (c == '(') push(c);
        else if (c == ')') {
            while (peek() != '(') printf("%c", pop());
            pop(); // remove '('
        } else {
            while (top != -1 && precedence(peek()) >= precedence(c))
                printf("%c", pop());
            push(c);
        }
    }
    while (top != -1) printf("%c", pop());
    printf("\n");
}

int main() {
    char expr[] = "a+b*(c^d-e)^(f+g*h)-i";
    infixToPostfix(expr);
    return 0;
}
```

---

Would you like me to compile these into a reference sheet or help you test them interactively? I can also add diagrams or flowcharts if you want visual clarity.