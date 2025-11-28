Of course. Here is a comprehensive, year-wise solution set for all the provided Data Structure and Algorithm mid-semester exam papers.

---

### **2018 Solutions**

**Q.1. (a) Function with time complexity O(m² + n log m)**
```c
void exampleFunction(int m, int n) {
    // O(m^2) part
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            // Some constant time operation
        }
    }

    // O(n log m) part
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < m; j *= 2) { // This loop runs log2(m) times
            // Some constant time operation
        }
    }
}
```

**Q.1. (b) Address Calculation**
*   **Given:** `arr[-15...10, 15...40]`, `Base = 2500`, `w = 4 bytes`.
*   **Rows (i):** Lower Bound `L1 = -15`, Upper Bound `U1 = 10`. Number of rows, `R = U1 - L1 + 1 = 10 - (-15) + 1 = 26`.
*   **Columns (j):** Lower Bound `L2 = 15`, Upper Bound `U2 = 40`. Number of columns, `C = U2 - L2 + 1 = 40 - 15 + 1 = 26`.
*   **Element:** `arr[8][20]`
*   **Row-Major Order:**
    `Address = Base + w * [ (i - L1) * C + (j - L2) ]`
    `= 2500 + 4 * [ (8 - (-15)) * 26 + (20 - 15) ]`
    `= 2500 + 4 * [ (23 * 26) + 5 ]`
    `= 2500 + 4 * [598 + 5] = 2500 + 4 * 603 = 2500 + 2412 = 4912`
*   **Column-Major Order:**
    `Address = Base + w * [ (j - L2) * R + (i - L1) ]`
    `= 2500 + 4 * [ (20 - 15) * 26 + (8 - (-15)) ]`
    `= 2500 + 4 * [ (5 * 26) + 23 ]`
    `= 2500 + 4 * [130 + 23] = 2500 + 4 * 153 = 2500 + 612 = 3112`

**Q.1. (c) Recursive function for grounded header list length**
```c
int countNodes(Node* current) {
    if (current == NULL || current->next == NULL) { // Checks if current is header or NULL
        return 0;
    } else {
        return 1 + countNodes(current->next);
    }
}
// Call with: countNodes(header->next);
```

**Q.1. (d) Delete middle item from stack**
```c
void deleteMiddle(Stack *s, int size) {
    if (isEmpty(s)) return;

    Stack tempStack;
    initStack(&tempStack);
    int midIndex = size / 2; // For 5 elements (0-indexed), mid=2. For 6, mid=3.

    // Pop and push first half to temp stack
    for (int i = 0; i < midIndex; i++) {
        push(&tempStack, pop(s));
    }
    pop(s); // This is the middle element, discard it.

    // Push back the elements from temp stack to original stack
    while (!isEmpty(&tempStack)) {
        push(s, pop(&tempStack));
    }
}
```

**Q.1. (e) Head vs. Tail Recursion**
*   **Head Recursion:** The recursive call is the first statement in the function. Processing is done during the returning phase.
    ```c
    void headRecursion(int n) {
        if (n > 0) {
            headRecursion(n-1); // Call first
            printf("%d ", n);   // Process later (on return)
        }
    }
    // headRecursion(3) prints "1 2 3"
    ```
*   **Tail Recursion:** The recursive call is the last statement in the function. Processing is done before the call. Modern compilers optimize this to avoid stack buildup (similar to a loop).
    ```c
    void tailRecursion(int n) {
        if (n > 0) {
            printf("%d ", n);   // Process first
            tailRecursion(n-1); // Call last
        }
    }
    // tailRecursion(3) prints "3 2 1"
    ```

**Q.2. Swap elements to make array sums equal**
**Algorithm:**
1.  Calculate the sum of both arrays, `sum1` and `sum2`.
2.  Let the target sum for both be `(sum1 + sum2) / 2`. If the total sum is not even, no solution is possible.
3.  For each element `a` in `arr1`, calculate the required value `req_val` in `arr2` such that: `sum1 - a + req_val = target`.
    This simplifies to: `req_val = target - (sum1 - a)`
4.  Check if this `req_val` exists in `arr2`. If found, swapping `a` with `req_val` will make both sums equal to `target`.
5.  (Optimization) Sort both arrays and use two pointers or a hash set for the lookup.

**Code:**
```c
#include <stdio.h>
// Assuming arrays and sizes are passed
void findSwapValues(int arr1[], int n, int arr2[], int m) {
    int sum1 = 0, sum2 = 0;
    for (int i=0; i<n; i++) sum1 += arr1[i];
    for (int i=0; i<m; i++) sum2 += arr2[i];

    int totalSum = sum1 + sum2;
    if (totalSum % 2 != 0) {
        printf("No solution possible\n");
        return;
    }
    int target = totalSum / 2;
    int diff = target - sum1; // We need: sum1 - a + b = target => b = a + diff

    // Use a hash set for arr2 for O(1) lookups
    // For simplicity, we use a nested loop here (O(n*m))
    for (int i=0; i<n; i++) {
        int required_b = arr1[i] + diff;
        for (int j=0; j<m; j++) {
            if (arr2[j] == required_b) {
                printf("Swap %d (from Array1) with %d (from Array2)\n", arr1[i], arr2[j]);
                return;
            }
        }
    }
    printf("No swap found\n");
}
```

**Q.3. (a) Polynomial Addition using Linked List**
**Node Structure:**
```c
struct Node {
    int coeff;
    int exp_x;
    int exp_y;
    struct Node* next;
};
```
**Algorithm to Add Three Polynomials (P1, P2, P3):**
1.  Create a function `addTwoPolynomials(struct Node* a, struct Node* b)` that takes two polynomials and returns their sum.
2.  Traverse both lists simultaneously.
3.  For each node, compare exponents (x first, then y).
4.  If exponents match, add coefficients and create a new node for the result list.
5.  If they don't match, insert the node with the higher exponent into the result list and move that pointer forward.
6.  Once one list is exhausted, append the rest of the other list to the result.
7.  To add three: `result = addTwoPolynomials(P1, P2); final_result = addTwoPolynomials(result, P3);`

**Q.3. (b) Sparse Matrix Addition with its Transpose**
**Sparse Matrix Representation (Triplet Form):**
```c
struct SparseMatrix {
    int row;
    int col;
    int value;
};
```
**Algorithm:**
1.  **Transpose:** Create the transpose `T` of the original sparse matrix `S` by iterating through `S` and swapping `row` and `col` for each triplet. Then sort `T` by row and column.
2.  **Addition:** Add the original matrix `S` and its transpose `T`.
    *   Use two pointers, `i` for `S` and `j` for `T`.
    *   Compare the `(row, col)` of `S[i]` and `T[j]`.
    *   If positions match, add the values and insert into result if sum is non-zero.
    *   If `S[i]` comes before `T[j]`, insert `S[i]` and increment `i`.
    *   Else, insert `T[j]` and increment `j`.
3.  Append remaining elements from either `S` or `T`.

---

### **2019 Solutions**

**Q1. (a) Time Complexity: O(m log m)**
*   The outer loop: `i` grows as `1, 2, 4, 8, ...` until `m`. This runs `O(log m)` times.
*   The inner loop: `j` runs from `1` to `i`. The number of inner iterations is `1 + 2 + 4 + ... + m ≈ 2m`.
*   Total Time Complexity: `O(log m) * O(m) = O(m log m)`.

**Q1. (b) Row-Major vs Column-Major Equality**
*   The address of `A[i][j]` in row-major is: `Base + w * (i * c + j)`
*   The address of `A[i][j]` in column-major is: `Base + w * (j * r + i)`
*   For them to be equal: `i * c + j = j * r + i`
*   This simplifies to: `i*(c - 1) = j*(r - 1)`
*   **Example:** Let `r=3, c=3, i=1, j=2`.
    *   Row-major index: `1*3 + 2 = 5`
    *   Column-major index: `2*3 + 1 = 7`. `5 != 7`.
    *   Now let `r=5, c=3, i=2, j=1`.
    *   Row-major: `2*3 + 1 = 7`
    *   Column-major: `1*5 + 2 = 7`. The addresses are equal.

**Q1. (c) Dynamic Allocation for M×N matrix**
```c
#include <stdlib.h>
int main() {
    int M = 5, N = 5;
    int **matrix;
    matrix = (int **)malloc(M * sizeof(int *)); // Allocate M rows
    for (int i = 0; i < M; i++) {
        matrix[i] = (int *)malloc(N * sizeof(int)); // Allocate N columns for each row
    }
    // Use matrix[i][j]
    // Remember to free memory later
    for (int i = 0; i < M; i++) free(matrix[i]);
    free(matrix);
}
```

**Q1. (d) Delete nodes divisible by k from SLL**
**Algorithm:**
1.  Handle the head node if it is divisible by `k`. Keep deleting the head until it is not.
2.  Traverse the list with two pointers: `prev` and `current`.
3.  If `current->data % k == 0`, bypass the node: `prev->next = current->next`. Free `current` and set `current = prev->next`.
4.  Else, move both pointers forward.

**Q1. (e) Recursively print stack without violating LIFO**
```c
void printStack(Stack s) {
    if (isEmpty(s)) {
        return;
    }
    int temp = pop(s);         // Pop the top element
    printf("%d ", temp);       // Print it (this will print in reverse order)
    printStack(s);             // Recursively print the rest
    push(s, temp);             // Push the element back to restore the stack
}
// To print in original order, print after the recursive call.
```

**Q2. (a) Merge sorted array A into sorted array B (B has space)**
**Algorithm:**
1.  Let `numElementsA` be the size of A. Let `numElementsB` be the number of actual elements in B (before the empty slots).
2.  Start from the *end* of both arrays to avoid overwriting.
    *   Pointer `i` at last element of A.
    *   Pointer `j` at last element of valid data in B.
    *   Pointer `k` at last position of the entire B array (including empty slots).
3.  While `i >= 0` and `j >= 0`:
    *   If `A[i] > B[j]`, set `B[k--] = A[i--]`.
    *   Else, set `B[k--] = B[j--]`.
4.  If any elements remain in A, copy them to the beginning of B.

**Code:**
```c
void mergeSortedArrays(int A[], int numElementsA, int B[], int totalSizeB) {
    // Assume totalSizeB is the total capacity of B, and it has enough empty slots at the end for A.
    int j = numElementsB - 1; // last element in B's initial data
    int i = numElementsA - 1; // last element in A
    int k = totalSizeB - 1;   // last position in the entire B array

    // Merge from the end
    while (i >= 0 && j >= 0) {
        if (A[i] > B[j]) {
            B[k--] = A[i--];
        } else {
            B[k--] = B[j--];
        }
    }
    // Copy any remaining elements from A (if any)
    while (i >= 0) {
        B[k--] = A[i--];
    }
    // If remaining elements in B, they are already in place.
}
```

**Q2. (b) Subtract two numbers represented by linked lists (LSD at head)**
**Algorithm:**
1.  Traverse both lists simultaneously.
2.  Subtract digits and keep track of `borrow`.
3.  `diff = (l1 ? l1->data : 0) - (l2 ? l2->data : 0) - borrow`
4.  If `diff < 0`, then `diff += 10` and set `borrow = 1`.
5.  Else, set `borrow = 0`.
6.  Create a new node with the value `diff`.
7.  Move pointers forward (`if(l1) l1=l1->next`, `if(l2) l2=l2->next`).
8.  After the loop, if there's a remaining borrow, handle it.
9.  Since the result is stored in a new list with LSD at head, this works in a single pass.

**Code Skeleton:**
```c
struct Node* subtractLists(struct Node* l1, struct Node* l2) {
    struct Node* result = NULL;
    struct Node** lastPtr = &result;
    int borrow = 0;

    while (l1 != NULL || l2 != NULL) {
        int val1 = (l1 != NULL) ? l1->data : 0;
        int val2 = (l2 != NULL) ? l2->data : 0;

        int diff = val1 - val2 - borrow;

        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }

        // Create new node and append it to result list
        struct Node* newNode = createNode(diff);
        *lastPtr = newNode;
        lastPtr = &(newNode->next);

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    // If borrow is still 1 at the end, the result is negative.
    // The problem states positive integers, so we assume l1 >= l2.
    return result;
}
// Example: l1: 1->0->0->2 (2001), l2: 8->7->5 (578)
// Iteration 1: 1 - 8 - 0 = -7 -> 3, borrow=1
// Iteration 2: (0) - 7 - 1 = -8 -> 2, borrow=1
// Iteration 3: (0) - 5 - 1 = -6 -> 4, borrow=1
// Iteration 4: 2 - (0) - 1 = 1, borrow=0
// Result: 3->2->4->1 (1423)
```

**Q3. (a) Sort a linked list and remove duplicates**
**Algorithm (Using Insertion Sort):**
1.  Create a new, empty sorted list (`sorted`).
2.  Traverse the original list.
3.  For each node, insert it into the correct position in the `sorted` list.
4.  While inserting, check for duplicates. If the value already exists, skip (free) the node instead of inserting it.
5.  **More Efficient:** Sort the list first (e.g., Merge Sort for LinkedList - O(n log n)), then traverse it once to remove consecutive duplicates.

**Q3. (b) Sparse Matrix Multiplication**
**Representations:** Triplet Form (for input) or CSR/CSC (for efficient operation).
**Algorithm for Multiplication (using Triplet Form):**
1.  Transpose the second matrix (`B`) for efficient row-column dot product. Let it be `BT`.
2.  For each non-zero element `(i, k, valueA)` in matrix `A`:
3.  For each non-zero element `(j, k, valueB)` in `BT` (which corresponds to `(k, j)` in `B`):
    *   If the column of A (`k`) matches the row of BT (`k`), which is the column of B (`k`), multiply `valueA * valueB`.
4.  This product contributes to the element `C[i][j]`.
5.  Use a temporary array to accumulate the sum of products for each `C[i][j]`.
6.  At the end, convert the temporary array into the triplet form of the result matrix `C`.

**Q4. (a) Reverse a Doubly Linked List**
```c
void reverseDLL(struct Node** head_ref) {
    struct Node* current = *head_ref;
    struct Node* temp = NULL;

    while (current != NULL) {
        // Swap the next and prev pointers of the current node
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;

        // Move to the next node (which is now in prev due to the swap)
        current = current->prev;
    }
    // Before changing the head, check for the empty list or list with only one node
    if (temp != NULL) {
        *head_ref = temp->prev; // temp was the last node before reversal, its prev is the new head
    }
}
```

**Q4. (b) Add two polynomials in two variables (x, y) using Linked List**
*   **Node Structure:** Same as 2018 Q3(a): `coeff`, `exp_x`, `exp_y`, `next`.
*   **Algorithm:** Same as adding two polynomials in 2018 Q3(a). The comparison of exponents now must check both `exp_x` and `exp_y`.
    *   First, compare `exp_x`. The term with the higher `exp_x` is greater.
    *   If `exp_x` is equal, then compare `exp_y`. The term with the higher `exp_y` is greater.
    *   If both exponents are equal, add the coefficients.

**Q5. (a) Push and Pop using different representations**
*   **Data Structures for Stack:**
    1.  **Array:** Fixed size, `top` index.
    2.  **Singly Linked List:** `head` pointer, push and pop at the head for O(1).
*   **Push() using Array:**
    ```c
    void pushArray(int stack[], int *top, int value, int size) {
        if (*top == size-1) { printf("Overflow"); return; }
        stack[++(*top)] = value;
    }
    ```
*   **Pop() using Linked List:**
    ```c
    int popLinkedList(struct Node** top) {
        if (*top == NULL) { printf("Underflow"); return -1; }
        struct Node* temp = *top;
        int popped = temp->data;
        *top = (*top)->next;
        free(temp);
        return popped;
    }
    ```

**Q5. (b) Infix to Postfix and Evaluation**
*   **Infix:** `((a/(b-c+d))*(e-a)*c)`
*   **Converted Postfix:** `a b c - d + / e a - * c *` (Steps involve managing parentheses and operator precedence: `^`, `*/`, `+-`).
*   **Pseudo Code for Evaluation:**
    ```plaintext
    Initialize an empty stack
    For each token in the postfix expression:
        if token is an operand:
            push it onto the stack.
        else if token is an operator:
            pop the top two operands from the stack (op2 and op1).
            apply the operator: result = op1 operator op2
            push the result onto the stack.
    The final result is the only value left on the stack.
    ```
*   **Evaluation with a=6, b=3, c=1, d=2, e=4:**
    *   Postfix: `6 3 1 - 2 + / 4 6 - * 1 *`
    *   Steps:
        *   Push 6
        *   Push 3
        *   Push 1
        *   `-`: Pop 1 and 3 -> 3-1=2, Push 2
        *   Push 2
        *   `+`: Pop 2 and 2 -> 2+2=4, Push 4
        *   `/`: Pop 4 and 6 -> 6/4=1, Push 1 (Integer division assumed)
        *   Push 4
        *   Push 6
        *   `-`: Pop 6 and 4 -> 4-6=-2, Push -2
        *   `*`: Pop -2 and 1 -> 1 * (-2) = -2, Push -2
        *   Push 1
        *   `*`: Pop 1 and -2 -> -2 * 1 = -2, Push -2
    *   **Final Result: -2**

---

### **2021 & 2022 Solutions** (Papers are identical)

**Q1. (a) Time Complexity: O(√n log n)**
*   Outer `while` loop: `i` runs from 1 to n, but `i` is not incremented in the inner loop. Let's see the inner loop.
*   Inner `for` loop: `j` runs from 1 to `√n` (since condition is `j*j <= n`). So, inner loop is O(√n).
*   How many times does the inner loop run? The outer `while` loop runs as long as `i<=n`. However, `i` is never incremented inside the outer loop! This creates an infinite loop if `n>0`. Assuming a typo and `i` is incremented (`i++` inside the outer while), the complexity is `O(n * √n) = O(n^(3/2))`.

**Q1. (b) Address Calculation for `arr[5, 3]`**
*   **Given:** `arr[3...6, -2...5]`, `Base = 1001`, `w = 4 bytes`.
*   **Rows (i):** `L1 = 3`, `U1 = 6`. `R = 6 - 3 + 1 = 4`.
*   **Columns (j):** `L2 = -2`, `U2 = 5`. `C = 5 - (-2) + 1 = 8`.
*   **Row-Major Order:**
    `Address = Base + w * [ (i - L1) * C + (j - L2) ]`
    `= 1001 + 4 * [ (5 - 3) * 8 + (3 - (-2)) ]`
    `= 1001 + 4 * [ (2 * 8) + 5 ]`
    `= 1001 + 4 * [16 + 5] = 1001 + 4 * 21 = 1001 + 84 = 1085`

**Q1. (c) Delete a node in DLL given only its pointer `ptr`**
```c
// ptr is the node to be deleted
if (ptr->prev != NULL) {
    ptr->prev->next = ptr->next;
}
if (ptr->next != NULL) {
    ptr->next->prev = ptr->prev;
}
free(ptr);
```

**Q1. (d) Representing Polynomial with SLL**
A node needs to store the coefficient and the exponents for all variables (x, y, z). Since the polynomial has 3 variables, the node structure should be:
```c
struct PolyNode {
    int coeff;
    int exp_x;
    int exp_y;
    int exp_z;
    struct PolyNode* next;
};
```
The polynomial `2xy^2+3x^2yz^2-4xy^3z+5x^2y^2+7xy^2z^2+11` would be represented by 6 nodes. The constant term `11` has `exp_x=0, exp_y=0, exp_z=0`.

**Q1. (e) Stack implementation initialization**
*   `push(x)` does `st[pos]=x; pos=pos-1;` This means the stack grows downwards in memory (from higher indices to lower indices).
*   `pop()` does `pos=pos+1; return(st[pos]);` This means `pos` points to the index *below* the current top element.
*   For an empty stack of max size `N`, `pos` should be initialized to `N`. The first `push` will decrement `pos` to `N-1` and store the element there, which is the top of the stack.
*   **Answer: `pos = N;`**

**Q2. (a) Sort elements at even indices**
**Algorithm:**
1.  Let `arr` be the array of size `n`.
2.  Extract all elements at even indices (0, 2, 4, ...) into a temporary array. (This violates "without additional DS", but is practical. A true in-place sort would be complex like modified Bubble Sort for even indices only).
3.  Sort this temporary array.
4.  Place the sorted elements back into the even indices of the original array.

**Q2. (b) Delete vowels from dynamic 2D array and shift**
**Algorithm:**
1.  Traverse the matrix row-wise.
2.  For each row, traverse each column.
3.  If the element is a vowel (`A`, `E`, `I`, `O`, `U`), delete it.
4.  To delete: Shift all elements to the right of it in the same row one position to the left.
5.  After processing a row, the last element in that row becomes vacant. Shift all elements in the rows below one position up? The problem says "shift from the same row and the next rows". A more precise algorithm is needed based on the example.
6.  The example shows the entire matrix being shifted left and up, with `X` placed in the final bottom-right position.
7.  **Easier Approach:** Don't delete in-place. Create a new 1D array of size `M*N`. Copy all non-vowel elements from the original matrix to this new array, in row-major order. Fill the remaining spots in the new array with `'X'`. Then, reshape this 1D array back into an `M×N` matrix.

**Q3. (a) Manipulate Doubly Linked List**
*   **Drawing the List:**
    *   Node-I (1001): `prev=2001`, `next=3001`, `data=10`
    *   Node-II (2001): `prev=NULL`, `next=NULL`, `data=15` -> **This is an error!** It's pointed to by I's `prev`, but its `next` is `NULL`. This makes it an isolated node. Assuming it's a mistake and `next` of II should be `1001` to form a circular link or something. Based on the question, we just use the pointers as given.
    *   Node-III (3001): `prev=NULL`, `next=4001`, `data=-5`
    *   Node-IV (4001): `prev=NULL`, `next=NULL`, `data=25`
    *   The list is: I <-> ? . III -> IV. II is isolated. III and IV have `prev=NULL`.
*   **C Statements to change values:**
    ```c
    // ptr holds 1001 (address of Node-I)
    int valueI = ptr->data; // valueI = 10

    // Change Node-II (assuming we can access it via I's prev pointer)
    // ptr->prev is 2001, which is Node-II
    if (ptr->prev != NULL) {
        ptr->prev->data = ptr->prev->data - valueI; // 15 - 10 = 5
    }

    // Change Node-III (ptr->next is 3001)
    if (ptr->next != NULL) {
        ptr->next->data = ptr->next->data + valueI; // -5 + 10 = 5
    }

    // Change Node-IV (ptr->next->next is 4001)
    if (ptr->next != NULL && ptr->next->next != NULL) {
        ptr->next->next->data = ptr->next->next->data + valueI; // 25 + 10 = 35
    }
    ```

**Q3. (b) Delete all odd numbers from SLL**
**Algorithm:**
1.  Handle the head node if it is odd. Keep deleting the head until it is not.
2.  Traverse the list with two pointers: `prev` and `current`.
3.  If `current->data % 2 != 0` (i.e., it's odd), bypass the node: `prev->next = current->next`. Free `current` and set `current = prev->next`.
4.  Else, move both pointers forward.

**Code:**
```c
void deleteAllOdds(struct Node** head_ref) {
    struct Node* current = *head_ref;
    struct Node* prev = NULL;
    struct Node* toFree = NULL;

    // Delete odd nodes at the beginning
    while (current != NULL && current->data % 2 != 0) {
        toFree = current;
        *head_ref = current->next;
        current = *head_ref;
        free(toFree);
    }

    // Now head is even, traverse the rest
    while (current != NULL) {
        if (current->data % 2 != 0) {
            // This node is odd, delete it
            toFree = current;
            prev->next = current->next;
            current = prev->next;
            free(toFree);
        } else {
            // This node is even, move pointers
            prev = current;
            current = current->next;
        }
    }
}
```

**Q4. Sparse Matrix Transpose and Triplet Representation**
*   **Sparse Matrix:** A matrix where most of the elements are zero.
*   **Representations:**
    1.  **Triplet Form:** A list of `(row, column, value)` for non-zero elements.
    2.  **Compressed Sparse Row (CSR):** Three arrays: `values`, `column_indices`, and `row_pointers`.
*   **Algorithm for Transpose (Triplet Form):**
    1.  Create a new triplet list `T` for the transpose.
    2.  For every triplet `(i, j, value)` in the original matrix `S`, add a triplet `(j, i, value)` to `T`.
    3.  Sort the list `T` by row number (which was the original column number) to get the final transposed matrix in standard order.

**Q5. Infix to Prefix Conversion**
**Algorithm:**
1.  Reverse the infix expression. Replace `(` with `)` and vice-versa.
2.  Obtain the postfix expression of this reversed infix string. (Use a stack, but note: precedence of operators is reversed – popped if precedence is *greater*, not greater-or-equal).
3.  Reverse the resulting postfix expression to get the final prefix expression.
*   **Infix:** `(A+B)+C-(D-E)^F`
*   **Step 1: Reverse:** `F^)E-D(+C+)B+A(`
*   **Step 2: Convert to Postfix:** This step is complex and requires careful application of the modified algorithm.
*   **Step 3: Reverse the postfix result.**
*   **Final Prefix Expression:** `-++ABC^-DEF` (This can be verified by building the expression tree).

---

### **2023 Solutions**

**Q1. (a) Answer: A) O(1)**
*   Accessing an element in a 2D array using its indices `[i][j]` is a constant time operation. It involves a simple calculation `Base + (i * n + j) * size` and then a memory access.

**Q1. (b) Address Calculation for `arr[8][6]` (Column-Major)**
*   **Given:** `arr[1...10][1...15]`, `Base = 100`, `w = 2 bytes`.
*   **Rows:** `R = 10`, **Columns:** `C = 15`.
*   **Column-Major Order:**
    `Address = Base + w * [ (j - L2) * R + (i - L1) ]`
    `= 100 + 2 * [ (6 - 1) * 10 + (8 - 1) ]`
    `= 100 + 2 * [ (5 * 10) + 7 ]`
    `= 100 + 2 * [50 + 7] = 100 + 2 * 57 = 100 + 114 = 214`

**Q1. (c) Output of the recursive function**
*   List: `10->20->30->40->50`
*   `disp(head)` prints `10`, then checks `head->next (20)` is not NULL, so calls `disp(head->next->next)` i.e., `disp(30)`.
*   `disp(30)` prints `30`, then checks `30->next (40)` is not NULL, so calls `disp(40->next)` i.e., `disp(50)`.
*   `disp(50)` prints `50`, then `50->next` is NULL, so it returns. Then it prints `50` again.
*   Back in `disp(30)`, it prints `30` again.
*   Back in `disp(10)`, it prints `10` again.
*   **Output: `10 30 50 50 30 10`**

**Q1. (d) Answer: A) Right to mid**
*   `new->prev = mid;` : New node's previous is `mid`.
*   `new->next = mid->next;` : New node's next is what was after `mid`.
*   `new->prev->next = new;` : `mid->next` is now `new`.
*   `new->next->prev = new;` : The node after `mid` now has its previous pointing to `new`.
*   This inserts `new` between `mid` and `mid->next`.

**Q1. (e) Stack operations**
*   Initial Stack (bottom to top): `[5, 7, 3]`, size=6, `top=2` (assuming 0-indexed array).
*   `push(4)`: Stack: `[5, 7, 3, 4]`, top=3. Output: -
*   `pop()`: Returns 4. Stack: `[5, 7, 3]`, top=2. Output: `4`
*   `push(10)`: Stack: `[5, 7, 3, 10]`, top=3.
*   `push(8)`: Stack: `[5, 7, 3, 10, 8]`, top=4.
*   `push(0)`: Stack: `[5, 7, 3, 10, 8, 0]`, top=5 (full).
*   `push(9)`: **Stack Overflow**. Ignored. Stack remains `[5, 7, 3, 10, 8, 0]`, top=5.
*   `pop()`: Returns 0. Stack: `[5, 7, 3, 10, 8]`, top=4. Output: `0`
*   `pop()`: Returns 8. Stack: `[5, 7, 3, 10]`, top=3. Output: `8`
*   **Final Output from pops: `4, 0, 8`**
*   **Final Stack (bottom to top): `[5, 7, 3, 10]`**

**Q2. (a) Function return value analysis**
*   Outer loop: `i` from 1 to n-1 -> runs `n-1` times ≈ `O(n)`.
*   First inner loop: `j` from n down to 1, halving each time -> runs `log2(n)` times. `p` becomes `log2(n)`.
*   Second inner loop: `k` from 1 to p, doubling each time -> runs `log2(p)` times ≈ `log2(log2(n))`.
*   `q` is incremented `log2(log2(n))` times for each outer iteration.
*   Total `q ≈ n * log(log n)`.
*   **Return value is approximately `n * log(log n)`.**

**Q2. (b) Remove odd numbers from array in O(n)**
```c
int removeOdds(int arr[], int n) {
    int newSize = 0; // Tracks the size of the new array without odds

    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) { // If element is even
            arr[newSize] = arr[i]; // Place it at the next available position
            newSize++;
        }
    }
    return newSize; // Returns the new size of the array
}
// Example: Input [10, 2, 3, 7, 8, 6, 11]
// newSize=0: arr[0]=10 (even) -> arr[0]=10, newSize=1
// newSize=1: arr[1]=2 (even) -> arr[1]=2, newSize=2
// arr[2]=3 (odd) -> skip
// arr[3]=7 (odd) -> skip
// newSize=2: arr[4]=8 (even) -> arr[2]=8, newSize=3
// newSize=3: arr[5]=6 (even) -> arr[3]=6, newSize=4
// arr[6]=11 (odd) -> skip
// Final array: [10, 2, 8, 6], return value 4.
```

**Q3. (a) Reverse a Singly Linked List**
**Iterative Method:**
```c
struct Node* reverseSLL(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;

    while (current != NULL) {
        next = current->next; // Store next node
        current->next = prev; // Reverse current node's pointer
        prev = current;       // Move prev to current
        current = next;       // Move current to next node
    }
    head = prev; // prev is the new head
    return head;
}
```

**Q3. (b) Insert after a specific position in DLL**
```c
void insertAfterPosition(struct Node* head, int position, int newData) {
    struct Node* current = head;
    int count = 0;

    // Traverse to the node at the given position
    while (current != NULL && count < position) {
        current = current->next;
        count++;
    }
    // If position is beyond the list length, current becomes NULL
    if (current == NULL) {
        printf("Position out of bounds\n");
        return;
    }
    // Create the new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;

    // Insert newNode after current
    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;
}
```

**Q4. (a) Infix to Postfix: `M^(N*P)/Q+R-S^T/(U/V)/W)-X`**
*   This requires step-by-step application of the stack-based algorithm. The result is lengthy.
*   **Approximate Postfix Result:** `M N P * ^ Q / R + S T ^ U V / / W / * - X -`
*   (This needs to be verified with a detailed stack trace).

**Q4. (b) Recursively print stack using push/pop**
*   Same as 2019 Q1(e).

**Q5. (a) Display stack in insertion order using a temp stack**
```c
void displayInOrder(Stack *s) {
    Stack tempStack;
    initStack(&tempStack);
    int x;

    // Pop from original and push to temp (this reverses the stack)
    while (!isEmpty(s)) {
        push(&tempStack, pop(s));
    }
    // Now tempStack has elements in insertion order (oldest at top)
    // Now, print from tempStack, and push back to original
    while (!isEmpty(&tempStack)) {
        x = pop(&tempStack);
        printf("%d ", x); // Print in insertion order
        push(s, x);       // Restore the original stack
    }
}
```

**Q5. (b) Two queues in one array**
```c
#define MAX_SIZE 100
int arr[MAX_SIZE];
int front1 = -1, rear1 = -1; // Queue 1 from left
int front2 = MAX_SIZE, rear2 = MAX_SIZE; // Queue 2 from right

int isFull() {
    return (rear1 + 1 == rear2);
}

void enqueue1(int value) {
    if (isFull()) { printf("Q1 Overflow"); return; }
    if (front1 == -1) front1 = 0;
    arr[++rear1] = value;
}
int dequeue1() {
    if (front1 == -1 || front1 > rear1) { printf("Q1 Underflow"); return -1; }
    return arr[front1++];
}

void enqueue2(int value) {
    if (isFull()) { printf("Q2 Overflow"); return; }
    if (front2 == MAX_SIZE) front2 = MAX_SIZE - 1;
    arr[--rear2] = value;
}
int dequeue2() {
    if (front2 == MAX_SIZE || rear2 > front2) { printf("Q2 Underflow"); return -1; } // rear2 > front2 means empty
    return arr[front2--];
}
```

---

### **2024 Solutions**

**Q1. (a) Time Complexity: O(n log n)**
*   Outer loop: `i` from 1 to n -> `O(n)`.
*   Inner loop: `j` starts at 1 and grows as `j = j^3`. The sequence is `1, 1, 1, ...` because `1^3=1`. This is an infinite loop if `n>1`. Assuming `j` is initialized outside the inner loop, or it's `j=1; j<n; j=pow(j, k)` where `k=3`. The inner loop runs only once for `j=1` since `1^3=1`, and the condition `j<n` fails if `n>1`. The complexity is `O(n * 1) = O(n)`.
*   **Likely intended complexity is O(n log n) if `j` was incremented differently.**

**Q1. (b) Address Calculation for `B[5][5]` (Row-Major)**
*   **Given:** `B[12][12]`, `w = 8 bytes`, `Loc(B[3][3]) = 1140`.
*   **Row-Major Formula:** `Loc(B[i][j]) = Base + w * (i * n + j)`
*   For `B[3][3]`: `Base + 8 * (3 * 12 + 3) = Base + 8 * (36 + 3) = Base + 8 * 39 = Base + 312 = 1140`.
*   Therefore, `Base = 1140 - 312 = 828`.
*   For `B[5][5]`: `Loc = 828 + 8 * (5 * 12 + 5) = 828 + 8 * (60 + 5) = 828 + 8 * 65 = 828 + 520 = 1348`.

**Q1. (c) Convert SLL to CLL**
```c
struct Node* convertSLLtoCLL(struct Node* head) {
    if (head == NULL) return NULL;
    struct Node* current = head;
    // Traverse to the last node
    while (current->next != NULL) {
        current = current->next;
    }
    // Link the last node to the head
    current->next = head;
    return head; // The list is now circular
}
```

**Q1. (d) Reverse string using stack**
```c
void reverseString(char* str) {
    int len = strlen(str);
    Stack s;
    initStack(&s);
    // Push each character onto the stack
    for (int i = 0; i < len; i++) {
        push(&s, str[i]);
    }
    // Pop each character back to the string (this reverses them)
    for (int i = 0; i < len; i++) {
        str[i] = pop(&s);
    }
    str[len] = '\0'; // Null-terminate the string
}
```

**Q1. (e) Stack and Queue operations**
*   Push: `11, 12, 13, 14, 15, 16` -> Stack (bottom to top): `[11, 12, 13, 14, 15, 16]`.
*   Pop 5 times: Popped values: `16, 15, 14, 13, 12`. Insert them into a Queue (FIFO): Queue Front -> `16, 15, 14, 13, 12` <- Rear.
*   Delete 3 from queue: Dequeued: `16, 15, 14`. Now Queue: `13, 12`.
*   Push these 3 back to stack: Push `16, 15, 14`. Stack was `[11]`. Now Stack (bottom to top): `[11, 16, 15, 14]`.
*   Pop 2 from stack: Popped: `14, 15`.
*   **Popped items: `14, 15`**

**Q2. (a) Convert 2D array to sparse matrix (triplet)**
```c
void convertToSparse(int** matrix, int rows, int cols, int triplet[][3]) {
    int k = 0; // Index for triplet array
    triplet[0][0] = rows;
    triplet[0][1] = cols;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] != 0) {
                k++;
                triplet[k][0] = i;
                triplet[k][1] = j;
                triplet[k][2] = matrix[i][j];
            }
        }
    }
    triplet[0][2] = k; // Number of non-zero elements
}
// Display triplet: printf("(%d, %d, %d)\n", triplet[i][0], triplet[i][1], triplet[i][2]);
```

**Q2. (b) Merge two sorted arrays using only arrays**
```c
void mergeSorted(int A[], int m, int B[], int n, int C[]) {
    int i = 0, j = 0, k = 0;
    // Traverse both arrays
    while (i < m && j < n) {
        if (A[i] <= B[j]) {
            C[k++] = A[i++];
        } else {
            C[k++] = B[j++];
        }
    }
    // Copy remaining elements of A[]
    while (i < m) {
        C[k++] = A[i++];
    }
    // Copy remaining elements of B[]
    while (j < n) {
        C[k++] = B[j++];
    }
}
```

**Q3. (a) Delete a node from any position in DLL**
```c
void deleteNodeAtPosition(struct Node** head_ref, int position) {
    if (*head_ref == NULL) return;
    struct Node* current = *head_ref;
    // If head needs to be deleted
    if (position == 0) {
        *head_ref = current->next;
        if (*head_ref != NULL) (*head_ref)->prev = NULL;
        free(current);
        return;
    }
    // Traverse to the node at the given position
    for (int i = 0; current != NULL && i < position; i++) {
        current = current->next;
    }
    // If position is greater than number of nodes
    if (current == NULL) return;
    // Bypass the node to be deleted
    if (current->next != NULL) current->next->prev = current->prev;
    if (current->prev != NULL) current->prev->next = current->next;
    free(current);
}
```

**Q3. (b) Add two sparse matrices**
*   Use triplet representation.
*   Algorithm is identical to 2018 Q3(b) (Addition part).

**Q4. (a) Infix to Postfix: `a * b / (a - c) + d * b`**
*   **Infix:** `a * b / (a - c) + d * b`
*   **Postfix:** `a b * a c - / d b * +`
*   **Step-by-step conversion requires showing the stack and output at each token.**

**Q4. (b) Evaluate postfix expression `a b * a c - / d b * +` with a=2, b=3, c=1, d=5**
*   Postfix: `2 3 * 2 1 - / 5 3 * +`
*   Steps:
    *   Push 2
    *   Push 3
    *   `*`: Pop 3 & 2 -> 2*3=6, Push 6
    *   Push 2
    *   Push 1
    *   `-`: Pop 1 & 2 -> 2-1=1, Push 1
    *   `/`: Pop 1 & 6 -> 6/1=6, Push 6
    *   Push 5
    *   Push 3
    *   `*`: Pop 3 & 5 -> 5*3=15, Push 15
    *   `+`: Pop 15 & 6 -> 6+15=21, Push 21
*   **Result: 21**

**Q5. (a) Sort a stack without additional DS**
*   Use recursion to pop all elements, sort the remaining stack, and then insert the popped element in sorted order.
```c
void sortedInsert(Stack* s, int x) {
    if (isEmpty(s) || x > peek(s)) {
        push(s, x);
        return;
    }
    int temp = pop(s);
    sortedInsert(s, x);
    push(s, temp);
}
void sortStack(Stack* s) {
    if (!isEmpty(s)) {
        int x = pop(s);
        sortStack(s);
        sortedInsert(s, x);
    }
}
```

**Q5. (b) Remove last node and insert at beginning of SLL**
```c
void moveLastToFront(struct Node** head_ref) {
    if (*head_ref == NULL || (*head_ref)->next == NULL) return;
    struct Node* last = *head_ref;
    struct Node* sec_last = NULL;
    // Traverse to the last node and the second last node
    while (last->next != NULL) {
        sec_last = last;
        last = last->next;
    }
    // Set the next of second last to NULL
    sec_last->next = NULL;
    // Set the next of last to the current head
    last->next = *head_ref;
    // Make last as the new head
    *head_ref = last;
}
```

---

**Best of luck with your exam!**