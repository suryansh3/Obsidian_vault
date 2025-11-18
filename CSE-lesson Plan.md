Based on a detailed analysis of the four examination papers you provided (from 2021, 2022, 2023, and 2024), I have identified the most important topics, their weightage, and a high-yield study plan.

The exams consistently test a core set of topics in both the compulsory short-answer section (Section A) and the long-answer sections where you have a choice.

### 📜 Analysis of Important Topics & Weightage

Here is a breakdown of all topics that appeared, organized from highest to lowest priority.

#### Tier 1: Core Topics (Extremely High Weightage)

These topics appear in **every single exam**, often in _both_ Section A and as a dedicated, high-mark question in Section B/C/D. Mastering these is non-negotiable.

- **1. Linked Lists (Singly, Doubly, & Circular)**
    
    - **Weightage:** Highest. Guaranteed to be a long-answer question.
        
    - **Key Subtopics:**
        
        - **Operations:** Reversing a list (SLL/DLL), merging two lists (alternating or sorted) , finding the merge point of two lists, and rotating a list.
            
        - **Implementation:** C-code or algorithms for insertion, deletion, and traversal.
            
        - **Problem Solving:** Deleting alternate nodes, finding the middle element, or separating odd/even numbers.
            
        - **Representation:** Using linked lists to represent polynomials  sparse matrices.
            
- **2. Trees (Binary, BST, & AVL)**
    
    - **Weightage:** Highest. This unit is a major source of marks, with AVL trees being a favorite long-answer question.
        
    - **Key Subtopics:**
        
        - **AVL Trees:** This is the most critical. You **must** know how to construct an AVL tree by inserting nodes one-by-one, including performing all four rotation types (LL, RR, LR, RL) to maintain . AVL deletion also appears.
            
        - **Tree Construction:** Building a binary tree from its traversal sequences (e.g., given In-order and Post-order, find Pre-order).
            
        - **Traversals:** Writing or tracing In-order, Pre-order, and Post-order traversals (both recursive and non-recursive/iterative methods).
            
        - **Binary Search Trees (BST):** Basic insertion 14, finding min/max elements , and checking if two trees are identical16.
            
- **3. Stacks & Queues (Applications)**
    
    - **Weightage:** Highest. While implementation is simple, the _applications_ of stacks are a guaranteed question.
        
    - **Key Subtopics:**
        
        - **Expression Conversion:** Infix to Postfix  Infix to . This is a frequent, algorithmic question.
            
        - **Expression Evaluation:** Evaluating a Postfix expression using a .
            
        - **Queues:** Circular Queue implementation (especially overflow/underflow conditions).
            
        - **Deques:** Input-restricted and output-restricted deques.
            
        - **Implementations:** Using a single array to implement two stacks.
            

#### Tier 2: Common Topics (High Weightage)

These topics appear in almost every exam and are common choices for long-answer questions.

- **4. Hashing**
    
    - **Weightage:** High. This is a very common long-answer question.
        
    - **Key Subtopics:**
        
        - **Collision Resolution:** You must be able to manually insert keys into a hash table and show the final state using:
            
            - **Separate Chaining** 
                
            - **Linear Probing** 
                
            - **Quadratic Probing** 
                
            - **Double Hashing** 
                
        - **Hash Functions:** Understanding the simple division method (e.g., `k % 10`).
            
- **5. Sorting**
    
    - **Weightage:** High. You are often asked to trace a sort or write the algorithm.
        
    - **Key Subtopics:**
        
        - **Insertion Sort:** Tracing the steps/passes.
            
        - **Bubble Sort:** Tracing the steps and understanding the optimized version (for an already-sorted list).
            
        - **Heap Sort:** Tracing the steps (building the max-heap, then deleting).
            
        - **Merge Sort:** Explaining the divide and conquer principle.
            
        - **Quick Sort:** Understanding the pivot and partition concept.
            
- **6. Graphs**
    
    - **Weightage:** High. Appears in 3 out of 4 papers as a long-answer question.
        
    - **Key Subtopics:**
        
        - **Traversals:** Tracing **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** starting from a given node.
            
        - **Representation:** Drawing a graph from an adjacency matrix or writing the adjacency list/matrix for a given graph.
            

#### Tier 3: Supporting Topics (Medium to Low Weightage)

These are either components of larger questions or appear as smaller, compulsory short questions.

- **7. Arrays & Sparse Matrices**
    
    - **Weightage:** Medium. Sparse matrix is a recurring long-answer question.
        
    - **Key Subtopics:**
        
        - **Sparse Matrix:** Understanding the 3-tuple (row-triplet) representation and writing functions for addition or subtraction.
            
        - **Address Calculation:** Finding the memory address of an element in a 2D array using row-major or column-major order.
            
        - **Array Problems:** Max sub-array sum, code tracing40.
            
- **8. Heaps**
    
    - **Weightage:** Medium. This often appears with Priority Queues or Heap Sort.
        
    - **Key Subtopics:**
        
        - **Priority Queue:** Implementation using a binary heap.
            
        - **Heap Operations:** Complexity of extracting max and inserting.
            
- **9. B-Trees**
    
    - **Weightage:** Very Low. Appeared only once as a 3-way B-Tree construction.
        

---

### 🚀 The 30/90 Study Plan: A High-Yield Strategy

Given the exam structure, you don't need to master all 9 topics. The long-answer sections (worth 70-80% of the marks) **always give you a choice**.

Your goal is to become an expert on **4 core topics** that are guaranteed to appear as long-answer questions. This is the 30% of effort that can yield 90% of the marks.

> **The "Core 4" for a 90% Result:**
> 
> 1. **Linked Lists (All Types):** Practice all common operations (reversal, merging, deletion of specific nodes, rotation). Be able to write the C function/algorithm for them from memory.
>     
> 2. **Trees (BST & AVL):** Focus 80% of your time here on **AVL construction**. Practice inserting nodes and performing all four rotations (LL, RR, LR, RL) until it is automatic. Also, be sure you can construct a tree from its traversals (e.g., In-order + Post-order).
>     
> 3. **Stacks (Applications):** Master the algorithms for **Infix-to-Postfix** and **Postfix Evaluation**. These are "cookbook" questions—if you know the steps, you cannot get them wrong.
>     
> 4. **Hashing (Collision Resolution):** Be able to take a list of keys and manually fill a hash table using **Linear Probing** and **Separate Chaining**. These are the two most frequently asked methods.
>     

#### Why this plan works:

- **Guaranteed Long Questions:** These four topics consistently appear as dedicated 4, 5, or 12-mark questions in the choice-based . You will be able to select your required number of questions just from this list.
    
- **High-Scoring in Section A:** These topics are also the most common in the compulsory short-answer.
    

#### If You Have More Time (The "Insurance" Topics):

If you master the "Core 4" and have extra time, add these two in order:

- **5. Graphs:** Learn to trace BFS and DFS. This is another common, easy-to-score question.
    
- **6. Sorting:** Know how to trace **Insertion Sort** and **Heap Sort** step-by-step.
    

By focusing your study on this "Core 4" list, you will be prepared for the vast majority of the marks in any of these exams.

Would you like me to create a focused study schedule or provide practice problems for one of these "Core 4" topics?