I'll create a comprehensive yet concise guide for your viva. Here are the key concepts with basic C code implementations:

## 1. Linear Queue (Array Implementation)

```c
[[include]] <stdio.h>
[[define]] MAX 5

typedef struct {
    int arr[MAX];
    int front, rear;
} Queue;

void initQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(Queue *q) {
    return (q->front == -1);
}

int isFull(Queue *q) {
    return (q->rear == MAX-1);
}

void enqueue(Queue *q, int value) {
    if(isFull(q)) {
        printf("Queue Overflow!\n");
        return;
    }
    if(isEmpty(q)) {
        q->front = 0;
    }
    q->arr[++(q->rear)] = value;
}

int dequeue(Queue *q) {
    if(isEmpty(q)) {
        printf("Queue Underflow!\n");
        return -1;
    }
    int value = q->arr[q->front];
    if(q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front++;
    }
    return value;
}

void traverse(Queue *q) {
    if(isEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    for(int i = q->front; i <= q->rear; i++) {
        printf("%d ", q->arr[i]);
    }
    printf("\n");
}
```

## 2. Linear Queue (Linked List Implementation)

```c
[[include]] <stdio.h>
[[include]] <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *front, *rear;
} Queue;

void initQueue(Queue *q) {
    q->front = q->rear = NULL;
}

int isEmpty(Queue *q) {
    return (q->front == NULL);
}

void enqueue(Queue *q, int value) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    
    if(isEmpty(q)) {
        q->front = q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

int dequeue(Queue *q) {
    if(isEmpty(q)) {
        printf("Queue Underflow!\n");
        return -1;
    }
    Node *temp = q->front;
    int value = temp->data;
    q->front = q->front->next;
    
    if(q->front == NULL) {
        q->rear = NULL;
    }
    free(temp);
    return value;
}

void traverse(Queue *q) {
    if(isEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    Node *current = q->front;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
```

## 3. Circular Queue (Array Implementation)

```c
[[include]] <stdio.h>
[[define]] MAX 5

typedef struct {
    int arr[MAX];
    int front, rear;
} CircularQueue;

void initQueue(CircularQueue *q) {
    q->front = q->rear = -1;
}

int isEmpty(CircularQueue *q) {
    return (q->front == -1);
}

int isFull(CircularQueue *q) {
    return ((q->rear + 1) % MAX == q->front);
}

void enqueue(CircularQueue *q, int value) {
    if(isFull(q)) {
        printf("Queue Overflow!\n");
        return;
    }
    if(isEmpty(q)) {
        q->front = 0;
    }
    q->rear = (q->rear + 1) % MAX;
    q->arr[q->rear] = value;
}

int dequeue(CircularQueue *q) {
    if(isEmpty(q)) {
        printf("Queue Underflow!\n");
        return -1;
    }
    int value = q->arr[q->front];
    if(q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX;
    }
    return value;
}

void traverse(CircularQueue *q) {
    if(isEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    int i = q->front;
    while(1) {
        printf("%d ", q->arr[i]);
        if(i == q->rear) break;
        i = (i + 1) % MAX;
    }
    printf("\n");
}
```

## 4. Deque (Double Ended Queue)

```c
[[include]] <stdio.h>
[[define]] MAX 5

typedef struct {
    int arr[MAX];
    int front, rear;
} Deque;

void initDeque(Deque *dq) {
    dq->front = -1;
    dq->rear = 0;
}

int isEmpty(Deque *dq) {
    return (dq->front == -1);
}

int isFull(Deque *dq) {
    return ((dq->front == 0 && dq->rear == MAX-1) || 
            dq->front == dq->rear + 1);
}

// Input Restricted - Only rear insertion
void insertRear(Deque *dq, int value) {
    if(isFull(dq)) {
        printf("Deque Overflow!\n");
        return;
    }
    if(isEmpty(dq)) {
        dq->front = dq->rear = 0;
    } else {
        dq->rear = (dq->rear + 1) % MAX;
    }
    dq->arr[dq->rear] = value;
}

// Output Restricted - Only front deletion
int deleteFront(Deque *dq) {
    if(isEmpty(dq)) {
        printf("Deque Underflow!\n");
        return -1;
    }
    int value = dq->arr[dq->front];
    if(dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else {
        dq->front = (dq->front + 1) % MAX;
    }
    return value;
}
```

## 5. Priority Queue (Linked List Implementation)

```c
[[include]] <stdio.h>
[[include]] <stdlib.h>

typedef struct Node {
    int data;
    int priority;
    struct Node *next;
} Node;

Node* createNode(int data, int priority) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->priority = priority;
    newNode->next = NULL;
    return newNode;
}

void enqueue(Node **head, int data, int priority) {
    Node *newNode = createNode(data, priority);
    
    if(*head == NULL || (*head)->priority > priority) {
        newNode->next = *head;
        *head = newNode;
    } else {
        Node *current = *head;
        while(current->next != NULL && 
              current->next->priority <= priority) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

int dequeue(Node **head) {
    if(*head == NULL) {
        printf("Priority Queue is empty!\n");
        return -1;
    }
    Node *temp = *head;
    int value = temp->data;
    *head = (*head)->next;
    free(temp);
    return value;
}

void traverse(Node *head) {
    if(head == NULL) {
        printf("Priority Queue is empty!\n");
        return;
    }
    Node *current = head;
    while(current != NULL) {
        printf("(%d, p:%d) ", current->data, current->priority);
        current = current->next;
    }
    printf("\n");
}
```

## 6. Binary Search Tree (Linked List Implementation)

```c
[[include]] <stdio.h>
[[include]] <stdlib.h>

typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode* createNode(int value) {
    TreeNode *newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

TreeNode* insert(TreeNode *root, int value) {
    if(root == NULL) return createNode(value);
    
    if(value < root->data) {
        root->left = insert(root->left, value);
    } else if(value > root->data) {
        root->right = insert(root->right, value);
    }
    return root;
}

void inorder(TreeNode *root) {
    if(root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void preorder(TreeNode *root) {
    if(root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(TreeNode *root) {
    if(root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

TreeNode* search(TreeNode *root, int key) {
    if(root == NULL || root->data == key) {
        return root;
    }
    if(key < root->data) {
        return search(root->left, key);
    }
    return search(root->right, key);
}

int findLargest(TreeNode *root) {
    while(root != NULL && root->right != NULL) {
        root = root->right;
    }
    return root ? root->data : -1;
}

int findSmallest(TreeNode *root) {
    while(root != NULL && root->left != NULL) {
        root = root->left;
    }
    return root ? root->data : -1;
}

int height(TreeNode *node) {
    if(node == NULL) return 0;
    int leftHeight = height(node->left);
    int rightHeight = height(node->right);
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int countLeafNodes(TreeNode *root) {
    if(root == NULL) return 0;
    if(root->left == NULL && root->right == NULL) return 1;
    return countLeafNodes(root->left) + countLeafNodes(root->right);
}
```

## Key Points to Remember:

### Queue Types:
- **Linear Queue**: Simple but inefficient (memory waste)
- **Circular Queue**: Efficient memory usage
- **Priority Queue**: Elements processed based on priority
- **Deque**: Double-ended operations

### Time Complexities:
- **Array Queue**: Enqueue/O(1), Dequeue/O(1)
- **Linked List Queue**: Enqueue/O(1), Dequeue/O(1)
- **BST Operations**: Search/Insert/Delete - O(h) where h is height

### Important Definitions:
- **Enqueue**: Add element to rear
- **Dequeue**: Remove element from front
- **IsEmpty**: Check if queue has no elements
- **IsFull**: Check if queue has reached capacity
- **Traverse**: Display all elements

### BST Traversals:
- **Inorder**: Left-Root-Right (Gives sorted order)
- **Preorder**: Root-Left-Right
- **Postorder**: Left-Right-Root

Good luck with your viva! Focus on understanding the concepts rather than memorizing code.