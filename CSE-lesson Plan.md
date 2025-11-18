Based on a detailed analysis of the four examination papers you provided (from 2021, 2022, 2023, and 2024), I have identified the most important topics, their weightage, and a high-yield study plan.

The exams consistently test a core set of topics in both the compulsory short-answer section (Section A) and the long-answer sections where you have a choice.

### 📜 Analysis of Important Topics & Weightage

Here is a breakdown of all topics that appeared, organized from highest to lowest priority.

#### Tier 1: Core Topics (Extremely High Weightage)

These topics appear in **every single exam**, often in _both_ Section A and as a dedicated, high-mark question in Section B/C/D. Mastering these is non-negotiable.

- **1. Linked Lists (Singly, Doubly, & Circular)**
    
    - **Weightage:** Highest. Guaranteed to be a long-answer question.
        
    - **Key Subtopics:**
        
        - **Operations:** Reversing a list (SLL/DLL) 111111111111, merging two lists (alternating or sorted) 222, finding the merge point of two lists 3, and rotating a list444444444444.
            
        - **Implementation:** C-code or algorithms for insertion, deletion, and traversal.
            
        - **Problem Solving:** Deleting alternate nodes 5, finding the middle element 6, or separating odd/even numbers7.
            
        - **Representation:** Using linked lists to represent polynomials 88888888888or sparse matrices999.
            
- **2. Trees (Binary, BST, & AVL)**
    
    - **Weightage:** Highest. This unit is a major source of marks, with AVL trees being a favorite long-answer question.
        
    - **Key Subtopics:**
        
        - **AVL Trees:** This is the most critical. You **must** know how to construct an AVL tree by inserting nodes one-by-one, including performing all four rotation types (LL, RR, LR, RL) to maintain balance101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010. AVL deletion also appears11.
            
        - **Tree Construction:** Building a binary tree from its traversal sequences (e.g., given In-order and Post-order, find Pre-order)121212121212121212121212121212121212121212121212121212121212121212.
            
        - **Traversals:** Writing or tracing In-order, Pre-order, and Post-order traversals (both recursive and non-recursive/iterative methods)131313131313131313131313131313131313.
            
        - **Binary Search Trees (BST):** Basic insertion 14, finding min/max elements 15, and checking if two trees are identical16.
            
- **3. Stacks & Queues (Applications)**
    
    - **Weightage:** Highest. While implementation is simple, the _applications_ of stacks are a guaranteed question.
        
    - **Key Subtopics:**
        
        - **Expression Conversion:** Infix to Postfix 171717171717171717171717171717171717171717171717and Infix to Prefix181818181818181818181818. This is a frequent, algorithmic question.
            
        - **Expression Evaluation:** Evaluating a Postfix expression using a stack19191919191919191919191919.
            
        - **Queues:** Circular Queue implementation (especially overflow/underflow conditions)2020202020202020202020202020.
            
        - **Deques:** Input-restricted and output-restricted deques21212121.
            
        - **Implementations:** Using a single array to implement two stacks22.
            

#### Tier 2: Common Topics (High Weightage)

These topics appear in almost every exam and are common choices for long-answer questions.

- **4. Hashing**
    
    - **Weightage:** High. This is a very common long-answer question.
        
    - **Key Subtopics:**
        
        - **Collision Resolution:** You must be able to manually insert keys into a hash table and show the final state using:
            
            - **Separate Chaining** 232323232323232323232323232323232323232323232323
                
            - **Linear Probing** 24242424242424242424242424242424242424242424
                
            - **Quadratic Probing** 2525252525252525252525252525
                
            - **Double Hashing** 262626262626262626262626
                
        - **Hash Functions:** Understanding the simple division method (e.g., `k % 10`)272727272727272727272727.
            
- **5. Sorting**
    
    - **Weightage:** High. You are often asked to trace a sort or write the algorithm.
        
    - **Key Subtopics:**
        
        - **Insertion Sort:** Tracing the steps/passes28282828.
            
        - **Bubble Sort:** Tracing the steps and understanding the optimized version (for an already-sorted list)292929292929292929.
            
        - **Heap Sort:** Tracing the steps (building the max-heap, then deleting)30.
            
        - **Merge Sort:** Explaining the divide and conquer principle31.
            
        - **Quick Sort:** Understanding the pivot and partition concept32.
            
- **6. Graphs**
    
    - **Weightage:** High. Appears in 3 out of 4 papers as a long-answer question.
        
    - **Key Subtopics:**
        
        - **Traversals:** Tracing **Breadth-First Search (BFS)** 33333333and **Depth-First Search (DFS)** 34343434 starting from a given node.
            
        - **Representation:** Drawing a graph from an adjacency matrix 35or writing the adjacency list/matrix for a given graph36363636.
            

#### Tier 3: Supporting Topics (Medium to Low Weightage)

These are either components of larger questions or appear as smaller, compulsory short questions.

- **7. Arrays & Sparse Matrices**
    
    - **Weightage:** Medium. Sparse matrix is a recurring long-answer question.
        
    - **Key Subtopics:**
        
        - **Sparse Matrix:** Understanding the 3-tuple (row-triplet) representation and writing functions for addition or subtraction373737373737373737373737373737373737373737373737373737.
            
        - **Address Calculation:** Finding the memory address of an element in a 2D array using row-major or column-major order38383838.
            
        - **Array Problems:** Max sub-array sum 39, code tracing40.
            
- **8. Heaps**
    
    - **Weightage:** Medium. This often appears with Priority Queues or Heap Sort.
        
    - **Key Subtopics:**
        
        - **Priority Queue:** Implementation using a binary heap41.
            
        - **Heap Operations:** Complexity of extracting max and inserting42.
            
- **9. B-Trees**
    
    - **Weightage:** Very Low. Appeared only once as a 3-way B-Tree construction43.
        

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

- **Guaranteed Long Questions:** These four topics consistently appear as dedicated 4, 5, or 12-mark questions in the choice-based sections444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444. You will be able to select your required number of questions just from this list.
    
- **High-Scoring in Section A:** These topics are also the most common in the compulsory short-answer section45454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545454545.
    

#### If You Have More Time (The "Insurance" Topics):

If you master the "Core 4" and have extra time, add these two in order:

- **5. Graphs:** Learn to trace BFS and DFS. This is another common, easy-to-score question.
    
- **6. Sorting:** Know how to trace **Insertion Sort** and **Heap Sort** step-by-step.
    

By focusing your study on this "Core 4" list, you will be prepared for the vast majority of the marks in any of these exams.

Would you like me to create a focused study schedule or provide practice problems for one of these "Core 4" topics?