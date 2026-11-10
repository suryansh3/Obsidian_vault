---
course: "Data Structures"
semester: 3
tags:
  - course/data-structures
up: "[[Data Structures]]"
---
# Structures, Pointers, and Their Use in Data Structures

## 📚 Comprehensive Notes for Your Data Structures Exam

### 1. Structures in C

**What is a structure?**
A structure is a user-defined data type that groups related variables of different types under a single name.

```c
// Basic structure definition
struct Node {
    int data;           // Data part
    struct Node* next;  // Pointer to next node
};

// Typedef for convenience
typedef struct Node {
    int data;
    struct Node* next;
} Node;
```

**Key Points:**
- Structures allow you to create complex data types
- Members are accessed using the dot (.) operator
- For pointer to structures, use the arrow (->) operator

### 2. Pointers in C

**What is a pointer?**
A pointer is a variable that stores the memory address of another variable.

```c
int main() {
    int x = 10;
    int *ptr = &x;  // ptr now holds the address of x
    
    printf("Value of x: %d\n", x);       // Output: 10
    printf("Address of x: %p\n", &x);    // Output: memory address
    printf("Value via pointer: %d\n", *ptr); // Output: 10
}
```

**Pointer Operations:**
- `&` (address-of operator): Gets the address of a variable
- `*` (dereference operator): Accesses the value at a pointer's address

### 3. Combining Structures and Pointers

This combination is powerful for creating dynamic data structures.

```c
typedef struct Student {
    char name[50];
    int age;
    float gpa;
} Student;

int main() {
    Student s1 = {"Alice", 20, 3.8};
    Student *ptr = &s1;
    
    printf("Name: %s\n", ptr->name);  // Access via pointer
    printf("Age: %d\n", ptr->age);
    printf("GPA: %.2f\n", ptr->gpa);
}
```

### 4. Pointers in Linked Lists

**Node Structure:**
```c
typedef struct Node {
    int data;
    struct Node* next;  // Pointer to next node
} Node;
```

**Key Operations:**

1. **Creating a Linked List:**
```c
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

2. **Inserting at Beginning:**
```c
void insertAtBeginning(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
```

3. **Traversing a List:**
```c
void traverseList(Node* head) {
    Node* current = head;
    while(current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

### 5. Pointers in Stacks

**Stack Implementation using Array:**
```c
[[define]] MAX 5

typedef struct Stack {
    int top;
    int items[MAX];
} Stack;

void initialize(Stack* s) {
    s->top = -1;  // Initialize top pointer
}

void push(Stack* s, int value) {
    if(s->top == MAX-1) {
        printf("Stack Overflow\n");
        return;
    }
    s->items[++(s->top)] = value;  // Increment top then add value
}

int pop(Stack* s) {
    if(s->top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return s->items[(s->top)--];  // Return value then decrement top
}
```

**Stack Implementation using Linked List:**
```c
typedef struct StackNode {
    int data;
    struct StackNode* next;
} StackNode;

void push(StackNode** top, int data) {
    StackNode* newNode = (StackNode*)malloc(sizeof(StackNode));
    newNode->data = data;
    newNode->next = *top;
    *top = newNode;
}

int pop(StackNode** top) {
    if(*top == NULL) {
        printf("Stack Underflow\n");
        return -1;
    }
    StackNode* temp = *top;
    int popped = temp->data;
    *top = (*top)->next;
    free(temp);
    return popped;
}
```

### 6. Memory Management

**Dynamic Memory Allocation:**
```c
// Allocation
Node* node = (Node*)malloc(sizeof(Node));

// Always check if allocation was successful
if(node == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}

// Deallocation
free(node);
node = NULL;  // Good practice to avoid dangling pointers
```

**Common Pointer Mistakes:**
1. **Dangling Pointers:** Pointers that reference freed memory
2. **Memory Leaks:** Not freeing allocated memory
3. **NULL Pointer Dereference:** Accessing memory via NULL pointer

### 7. Double Pointers in Data Structures

Double pointers are essential when you need to modify the head pointer of a linked list.

```c
// Without double pointer (WON'T WORK)
void insertFrontWrong(Node* head, int data) {
    Node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;  // This change is local to the function
}

// With double pointer (CORRECT)
void insertFrontCorrect(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;  // This modifies the original head pointer
}
```

### 8. Key Exam Concepts

**Pointer Arithmetic:**
- Only valid for arrays, not for linked lists
- `ptr++` moves to next element based on data type size

**Structure Padding:**
- Compilers may add padding to align data in memory
- Use `#pragma pack(1)` to minimize padding if needed

**Pass by Value vs. Pass by Reference:**
- C always passes arguments by value
- To simulate pass by reference, use pointers

### 9. Visualization Tips

**Linked List:**
```
[Data|Next] -> [Data|Next] -> [Data|Next] -> NULL
```

**Stack:**
```
Top -> [Data]
       [Data]
       [Data]
       ...
```

### 10. Common Exam Questions

1. **What is the difference between ptr++ and ptr+1?**
   - `ptr++` increments the pointer and returns the original address
   - `ptr+1` returns the next address without changing ptr

2. **Why use a double pointer in linked list functions?**
   - To modify the head pointer when inserting at the beginning

3. **What is the time complexity of various operations?**
   - Array access: O(1)
   - Linked list insertion at beginning: O(1)
   - Linked list traversal: O(n)

### 11. Quick Revision Table

| Concept | Syntax | Purpose |
|---------|--------|---------|
| Structure | `struct Node {int data; struct Node* next;};` | Group related data |
| Pointer | `int *ptr = &var;` | Store memory address |
| malloc | `ptr = (type*)malloc(size);` | Dynamic memory allocation |
| free | `free(ptr);` | Memory deallocation |
| Arrow operator | `ptr->data` | Access struct member via pointer |

## 🎯 Exam Success Tips

1. **Draw diagrams** for linked list and stack operations
2. **Trace code** step by step with sample values
3. **Practice** writing code without looking at notes
4. **Understand** the difference between array and linked list implementations
5. **Remember** to always check for NULL pointers and memory allocation success

You've got this! With these notes and your understanding of structures and pointers, you're well-prepared to ace your Data Structures exam. Good luck!

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Data Structures]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 3/Data Structures/Miscellaneous|Miscellaneous]] · **Next:** [[04 - Academics & CS/Semester 3/Data Structures/PYQs|PYQs]]
> **Related:** [[DAA]] · [[Discrete Mathematics]] · [[OOPJ (Java)]]
<!-- connections:end -->
