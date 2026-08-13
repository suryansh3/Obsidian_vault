# Comprehensive Data Structure Operations in C

I'll create a complete guide with C programs demonstrating key operations on arrays, linked lists (single, double, circular), and stacks. Each example is designed to be clear and easy to understand for your exam.

```c
[[include]] <stdio.h>
[[include]] <stdlib.h>

// ==================== ARRAY OPERATIONS ====================
void array_operations() {
    printf("=== ARRAY OPERATIONS ===\n");
    int arr[10] = {1, 3, 5, 7, 9};
    int size = 5;
    int capacity = 10;
    
    // Traversal
    printf("Array elements: ");
    for(int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Access/Retrieval
    printf("Element at index 2: %d\n", arr[2]);
    
    // Searching
    int target = 7, found = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] == target) {
            printf("Element %d found at index %d\n", target, i);
            found = 1;
            break;
        }
    }
    if(!found) printf("Element %d not found\n", target);
    
    // Insertion
    if(size < capacity) {
        int pos = 2, value = 10;
        for(int i = size; i > pos; i--) {
            arr[i] = arr[i-1];
        }
        arr[pos] = value;
        size++;
        printf("After insertion at pos %d: ", pos);
        for(int i = 0; i < size; i++) printf("%d ", arr[i]);
        printf("\n");
    }
    
    // Deletion
    int del_pos = 3;
    if(del_pos < size) {
        for(int i = del_pos; i < size-1; i++) {
            arr[i] = arr[i+1];
        }
        size--;
        printf("After deletion at pos %d: ", del_pos);
        for(int i = 0; i < size; i++) printf("%d ", arr[i]);
        printf("\n");
    }
    printf("\n");
}

// ==================== SINGLY LINKED LIST ====================
struct Node {
    int data;
    struct Node* next;
};

void sll_operations() {
    printf("=== SINGLY LINKED LIST OPERATIONS ===\n");
    struct Node* head = NULL;
    struct Node* second = NULL;
    struct Node* third = NULL;
    
    // Create nodes
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    
    head->data = 1;
    head->next = second;
    
    second->data = 2;
    second->next = third;
    
    third->data = 3;
    third->next = NULL;
    
    // Traversal
    printf("SLL elements: ");
    struct Node* current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
    
    // Access/Retrieval
    int pos = 1;
    current = head;
    for(int i = 0; i < pos && current != NULL; i++) {
        current = current->next;
    }
    if(current != NULL) printf("Element at position %d: %d\n", pos, current->data);
    
    // Searching
    target = 2;
    current = head;
    int position = 0;
    while(current != NULL) {
        if(current->data == target) {
            printf("Element %d found at position %d\n", target, position);
            break;
        }
        current = current->next;
        position++;
    }
    
    // Insertion at beginning
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = 0;
    new_node->next = head;
    head = new_node;
    printf("After insertion at beginning: ");
    current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
    
    // Deletion at beginning
    struct Node* temp = head;
    head = head->next;
    free(temp);
    printf("After deletion at beginning: ");
    current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n\n");
    
    // Free memory
    while(head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

// ==================== DOUBLY LINKED LIST ====================
struct DNode {
    int data;
    struct DNode* prev;
    struct DNode* next;
};

void dll_operations() {
    printf("=== DOUBLY LINKED LIST OPERATIONS ===\n");
    struct DNode* head = NULL;
    struct DNode* second = NULL;
    struct DNode* third = NULL;
    
    // Create nodes
    head = (struct DNode*)malloc(sizeof(struct DNode));
    second = (struct DNode*)malloc(sizeof(struct DNode));
    third = (struct DNode*)malloc(sizeof(struct DNode));
    
    head->data = 1;
    head->prev = NULL;
    head->next = second;
    
    second->data = 2;
    second->prev = head;
    second->next = third;
    
    third->data = 3;
    third->prev = second;
    third->next = NULL;
    
    // Traversal forward
    printf("DLL elements (forward): ");
    struct DNode* current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
    
    // Traversal backward
    printf("DLL elements (backward): ");
    current = third;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->prev;
    }
    printf("\n");
    
    // Insertion at end
    struct DNode* new_node = (struct DNode*)malloc(sizeof(struct DNode));
    new_node->data = 4;
    new_node->next = NULL;
    new_node->prev = third;
    third->next = new_node;
    
    printf("After insertion at end: ");
    current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
    
    // Deletion from middle
    struct DNode* to_delete = second;
    to_delete->prev->next = to_delete->next;
    to_delete->next->prev = to_delete->prev;
    free(to_delete);
    
    printf("After deleting middle node: ");
    current = head;
    while(current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n\n");
    
    // Free memory
    while(head != NULL) {
        struct DNode* temp = head;
        head = head->next;
        free(temp);
    }
}

// ==================== CIRCULAR LINKED LIST ====================
void cll_operations() {
    printf("=== CIRCULAR LINKED LIST OPERATIONS ===\n");
    struct Node* head = NULL;
    struct Node* second = NULL;
    struct Node* third = NULL;
    
    // Create nodes
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    
    head->data = 1;
    head->next = second;
    
    second->data = 2;
    second->next = third;
    
    third->data = 3;
    third->next = head;  // Circular reference
    
    // Traversal
    printf("CLL elements: ");
    if(head != NULL) {
        struct Node* current = head;
        do {
            printf("%d ", current->data);
            current = current->next;
        } while(current != head);
    }
    printf("\n");
    
    // Insertion at beginning
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = 0;
    
    if(head == NULL) {
        new_node->next = new_node;
        head = new_node;
    } else {
        new_node->next = head;
        struct Node* temp = head;
        while(temp->next != head) {
            temp = temp->next;
        }
        temp->next = new_node;
        head = new_node;
    }
    
    printf("After insertion at beginning: ");
    if(head != NULL) {
        struct Node* current = head;
        do {
            printf("%d ", current->data);
            current = current->next;
        } while(current != head);
    }
    printf("\n\n");
    
    // Free memory (simplified for circular list)
    if(head != NULL) {
        struct Node* current = head->next;
        while(current != head) {
            struct Node* temp = current;
            current = current->next;
            free(temp);
        }
        free(head);
    }
}

// ==================== STACK OPERATIONS ====================
[[define]] MAX 5

struct Stack {
    int top;
    int items[MAX];
};

void initializeStack(struct Stack* s) {
    s->top = -1;
}

int isFull(struct Stack* s) {
    return s->top == MAX - 1;
}

int isEmpty(struct Stack* s) {
    return s->top == -1;
}

void push(struct Stack* s, int value) {
    if(isFull(s)) {
        printf("Stack is full. Cannot push %d\n", value);
        return;
    }
    s->items[++s->top] = value;
    printf("Pushed %d to stack\n", value);
}

int pop(struct Stack* s) {
    if(isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    printf("Popped %d from stack\n", s->items[s->top]);
    return s->items[s->top--];
}

int peek(struct Stack* s) {
    if(isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    return s->items[s->top];
}

void stack_operations() {
    printf("=== STACK OPERATIONS ===\n");
    struct Stack s;
    initializeStack(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Top element: %d\n", peek(&s));
    
    pop(&s);
    printf("Top element after pop: %d\n", peek(&s));
    
    push(&s, 40);
    push(&s, 50);
    push(&s, 60);
    push(&s, 70); // This will show stack is full
    
    printf("Stack elements: ");
    while(!isEmpty(&s)) {
        printf("%d ", pop(&s));
    }
    printf("\n");
    
    pop(&s); // This will show stack is empty
    printf("\n");
}

// ==================== MAIN FUNCTION ====================
int main() {
    array_operations();
    sll_operations();
    dll_operations();
    cll_operations();
    stack_operations();
    
    printf("Good luck with your exam! You've got this!\n");
    return 0;
}
```

## Key Points to Remember for Your Exam:

### Arrays:
- **Fixed size**, contiguous memory allocation
- **Random access** - O(1) time complexity
- **Insertion/Deletion** - O(n) time complexity as elements need shifting
- Good for frequent access, bad for frequent modifications

### Linked Lists:
- **Dynamic size**, non-contiguous memory
- **Sequential access** - O(n) time complexity
- **Insertion/Deletion** - O(1) at known positions
- **Types**:
  - **Singly**: One pointer to next node
  - **Doubly**: Two pointers to next and previous nodes
  - **Circular**: Last node points back to first node

### Stacks:
- **LIFO** (Last In First Out) structure
- **Operations**:
  - Push: Add element to top
  - Pop: Remove element from top
  - Peek: View top element without removing
- Can be implemented using arrays or linked lists

### Time Complexity Summary:
| Operation | Array | Linked List | Stack |
|-----------|-------|-------------|-------|
| Access    | O(1)  | O(n)        | O(1)* |
| Search    | O(n)  | O(n)        | O(n)  |
| Insertion | O(n)  | O(1)*       | O(1)  |
| Deletion  | O(n)  | O(1)*       | O(1)  |

*At known positions for linked lists, top element for stacks

This comprehensive code and summary should help you ace your Data Structures exam! Good luck!