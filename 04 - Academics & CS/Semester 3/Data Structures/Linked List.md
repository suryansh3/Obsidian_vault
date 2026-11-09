---
course: "Data Structures"
semester: 3
tags:
  - course/data-structures
up: "[[Data Structures]]"
---
# 📚 Comprehensive Linked List Notes for Your Exam

## 1. Introduction to Linked Lists

### What is a Linked List?
A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

### Types of Linked Lists:
1. **Singly Linked List**: Each node points only to the next node
2. **Doubly Linked List**: Each node points to both next and previous nodes
3. **Circular Linked List**: Last node points back to the first node

## 2. Node Structure

### Basic Node Definition:
```c
typedef struct Node {
    int data;
    struct Node* next;
} Node;
```

### Memory Representation:
```
[Data|Next] → [Data|Next] → [Data|Next] → NULL
```

## 3. Basic Operations with Complete Code

### 1. Creating a Node
```c
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if(newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

### 2. Insertion Operations

**a) Insert at Beginning:**
```c
void insertAtBeginning(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
```

**b) Insert at End:**
```c
void insertAtEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    
    if(*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node* temp = *head;
    while(temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

**c) Insert at Specific Position:**
```c
void insertAtPosition(Node** head, int data, int position) {
    if(position < 1) {
        printf("Invalid position!\n");
        return;
    }
    
    if(position == 1) {
        insertAtBeginning(head, data);
        return;
    }
    
    Node* newNode = createNode(data);
    Node* temp = *head;
    
    // Traverse to position-1 node
    for(int i = 1; i < position-1 && temp != NULL; i++) {
        temp = temp->next;
    }
    
    if(temp == NULL) {
        printf("Position out of bounds!\n");
        free(newNode);
        return;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
}
```

### 3. Deletion Operations

**a) Delete from Beginning:**
```c
void deleteFromBeginning(Node** head) {
    if(*head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
}
```

**b) Delete from End:**
```c
void deleteFromEnd(Node** head) {
    if(*head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    if((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }
    
    Node* temp = *head;
    while(temp->next->next != NULL) {
        temp = temp->next;
    }
    
    free(temp->next);
    temp->next = NULL;
}
```

**c) Delete by Value:**
```c
void deleteByValue(Node** head, int value) {
    if(*head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    // If head node contains the value
    if((*head)->data == value) {
        Node* temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }
    
    Node* current = *head;
    Node* prev = NULL;
    
    while(current != NULL && current->data != value) {
        prev = current;
        current = current->next;
    }
    
    if(current == NULL) {
        printf("Value not found!\n");
        return;
    }
    
    prev->next = current->next;
    free(current);
}
```

### 4. Traversal and Display
```c
void displayList(Node* head) {
    if(head == NULL) {
        printf("List is empty!\n");
        return;
    }
    
    Node* temp = head;
    printf("Linked List: ");
    while(temp != NULL) {
        printf("%d → ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
```

### 5. Search Operation
```c
int searchElement(Node* head, int key) {
    Node* temp = head;
    int position = 1;
    
    while(temp != NULL) {
        if(temp->data == key) {
            return position;
        }
        temp = temp->next;
        position++;
    }
    
    return -1; // Not found
}
```

## 4. Common Exam Questions with Solutions

### Question 1: Reverse a Linked List
```c
Node* reverseList(Node* head) {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    
    while(current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
}
```

### Question 2: Find Middle Element
```c
Node* findMiddle(Node* head) {
    if(head == NULL) return NULL;
    
    Node* slow = head;
    Node* fast = head;
    
    while(fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow;
}
```

### Question 3: Detect Cycle in Linked List
```c
int hasCycle(Node* head) {
    if(head == NULL) return 0;
    
    Node* slow = head;
    Node* fast = head;
    
    while(fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        
        if(slow == fast) {
            return 1; // Cycle detected
        }
    }
    
    return 0; // No cycle
}
```

### Question 4: Merge Two Sorted Linked Lists
```c
Node* mergeSortedLists(Node* list1, Node* list2) {
    if(list1 == NULL) return list2;
    if(list2 == NULL) return list1;
    
    Node* result = NULL;
    
    if(list1->data <= list2->data) {
        result = list1;
        result->next = mergeSortedLists(list1->next, list2);
    } else {
        result = list2;
        result->next = mergeSortedLists(list1, list2->next);
    }
    
    return result;
}
```

### Question 5: Remove Duplicates from Sorted List
```c
void removeDuplicates(Node* head) {
    if(head == NULL) return;
    
    Node* current = head;
    
    while(current->next != NULL) {
        if(current->data == current->next->data) {
            Node* temp = current->next;
            current->next = current->next->next;
            free(temp);
        } else {
            current = current->next;
        }
    }
}
```

## 5. Time Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access    | O(n)           | O(1)             |
| Search    | O(n)           | O(1)             |
| Insertion | O(1) at beginning, O(n) at end | O(1) |
| Deletion  | O(1) at beginning, O(n) at end | O(1) |
| Reverse   | O(n)           | O(1)             |

## 6. Important Concepts to Remember

### 1. Memory Management:
- Always check if `malloc()` returns NULL
- Always free memory after use to prevent leaks
- Set pointers to NULL after freeing

### 2. Edge Cases:
- Empty list (head == NULL)
- Single node list
- Operations at beginning/end
- Invalid positions

### 3. Pointer Manipulation:
- Use double pointers when modifying head pointer
- Understand the difference between `current->next` and `current->next->next`
- Be careful with pointer reassignment order

## 7. Exam Tips

1. **Draw diagrams** for pointer operations
2. **Trace code** with small examples (3-4 nodes)
3. **Check edge cases** in your solutions
4. **Comment your code** to show understanding
5. **Manage time** - solve easier problems first

## 8. Common Mistakes to Avoid

1. Forgetting to check for NULL pointers
2. Not handling the head pointer correctly
3. Memory leaks (not freeing allocated memory)
4. Off-by-one errors in position-based operations
5. Modifying pointers in wrong order

## 9. Practice Problems for Quick Revision

1. Write a function to find the length of a linked list
2. Implement a function to get the Nth node from the end
3. Check if a linked list is palindrome
4. Write a function to delete the entire list
5. Implement a function to swap nodes without swapping data

You've got this! With these comprehensive notes and practice, you're well-prepared to ace your linked list questions. Good luck with your exam! 🚀

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Data Structures]] · **Semester:** [[Semester 3]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 3/Data Structures/DSA 16 Question Co-Pilot|DSA 16 Question Co-Pilot]] · **Next:** [[04 - Academics & CS/Semester 3/Data Structures/Miscellaneous|Miscellaneous]]
> **Related:** [[DAA]] · [[Discrete Mathematics]] · [[OOPJ (Java)]]
<!-- connections:end -->
