Based on the provided Spring Mid-Semester Examination paper (2025) for Computer Organization and Architecture, here are the solutions to the questions.

---

## **Section 1: Compulsory Short Answer Questions**

**1. a) Compare Instruction Analysis**

**Instruction:** `Compare R5, R6` (where R6 is the destination) **Initial Values:** $R5 = 100$, $R6 = 200$

- **Final Value of R5:** **100**. The `Compare` (CMP) instruction is non-destructive; it performs a subtraction ($Destination - Source$) but does not store the result.
    
- **Final Value of R6:** **200**. The destination register remains unchanged after a comparison.
    
- **Carry Flag (C):** **0**. In most architectures, because $200 \ge 100$, no "borrow" is required for the subtraction.
    
- **Sign Flag (S):** **0** (Positive). The internal result of $200 - 100$ is $+100$, which is positive.
    

**1. b) Branch Instruction Analysis**

**Initial Values:** $R1 = 90$, $R2 = -120$ **Code Segment:**

1. `3050: ADD R1, R2`
    
2. `3054: Branch<=0 1000`
    

- **Step 1:** `ADD R1, R2` results in $90 + (-120) = -30$.
    
- **Step 2:** The branch condition is `Branch <= 0`. Since $-30 \le 0$, the condition is **True**.
    
- **Final PC Value:** **1000**. Because the condition is met, the Program Counter (PC) loads the target address specified in the branch instruction.
    

**1. c) Memory References**

- **`POP M`:** **3 references**.
    
    1. **Instruction Fetch:** Fetching the instruction from memory.
        
    2. **Stack Read:** Reading the value from the memory location pointed to by the Stack Pointer (SP).
        
    3. **Memory Write:** Writing that value to memory location `M`.
        
- **`XOR R5, (R6)+`:** **2 references**.
    
    1. **Instruction Fetch:** Fetching the instruction.
        
    2. **Operand Read:** Reading the second operand from the memory address stored in `R6` (Autoincrement mode). _Note: Updating the register `R6` is an internal CPU operation and not a memory reference._
        

**1. d) Hardwired Control Unit Inflexibility**

The statement is justified because hardwired control logic is implemented using **fixed physical hardware components** (logic gates, flip-flops, and decoders).

- **Lack of Reconfigurability:** To add a new instruction or modify an existing one, the physical wiring and circuit design must be redesigned and rebuilt, which is difficult and costly compared to updating microcode in a microprogrammed unit.
    

**1. e) 2's Complement Overflow ($R1 + R2$)**

Overflow in 4-bit 2's complement (range: $-8$ to $+7$) occurs if the sum of two numbers with the same sign results in a different sign.

- $R1=1111 (-1), R2=1101 (-3) \rightarrow$ Result: $11100 (-4)$. **No Overflow**.
    
- $R1=1110 (-2), R2=1100 (-4) \rightarrow$ Result: $11010 (-6)$. **No Overflow**.
    
- **$R1=1000 (-8), R2=1100 (-4) \rightarrow$ Result: $10100 (+4)$.** **Overflow**. (Adding two negatives resulted in a positive value).
    
- $R1=1010 (-6), R2=1110 (-2) \rightarrow$ Result: $11000 (-8)$. **No Overflow**.
    

---

## **Section 2: Question 2**

**2. a) Endianness Representation of (-111)**

- **Value:** $-111$ in 16-bit (2 bytes) 2's complement.
    
- **Binary (+111):** `0000 0000 0110 1111` ($6F$ in hex).
    
- **Binary (-111):** `1111 1111 1001 0001` (**$FF91$** in hex).
    

|**Address**|**Big Endian**|**Little Endian**|
|---|---|---|
|**1000**|$FF$ (MSB)|$91$ (LSB)|
|**1001**|$91$ (LSB)|$FF$ (MSB)|

**2. b) Subroutine Execution Trace**

_Initial: SP = 6000, Stack Top = 500, Word Size = 4 bytes (Decreasing order)._

|**Condition**|**PC**|**SP**|**Top of Stack Value**|
|---|---|---|---|
|**i) After CALL SUB1 (Main)**|2000|5996|1012 (Return address)|
|**ii) After CALL SUB2 (SUB1)**|3000|5992|2008 (Return address)|
|**iii) After Return from SUB2**|2008|5996|1012|
|**iv) After Return from SUB1**|1012|6000|500|

---

## **Section 3: Question 3**

**3. a) Memory Contents After Execution**

_Initial: Memory 2000-2016 contains numbers 1, 2, 3, 4, 5. $R1=10, R2=20$._

1. `Move #2000, R0`: $R0 = 2000$.
    
2. `Add R1, 4(R0)`: $10 +$ (Value at 2004) $\rightarrow 10 + 2 = 12$. Memory [2004] becomes **12**.
    
3. `Add #4, R0`: $R0 = 2004$.
    
4. `Add 4(R0), R2`: (Value at 2008) $+ 20 \rightarrow 3 + 20 = 23$. $R2 = 23$.
    
5. `Move R2, 8(R0)`: Move 23 to address $2004 + 8 = 2012$. Memory [2012] becomes **23**.
    

**Final Contents at Address:**

- **2000:** 1
    
- **2004:** 12
    
- **2008:** 3
    
- **2012:** 23
    
- **2016:** 5
    

**3. b) Multi-bus CPU Architecture**

**Sequence for `MUL 40(R1), R2, R3` (Destination R3):**

1. `PCout, Bus A, Read, Select 4, Add, Zın` (Fetch Instruction)
    
2. `Zout, PCın, WMFC` (Increment PC)
    
3. `MDRout, IRın` (Load IR)
    
4. `R1out, Bus A, Select 40, Add, Zın` (Calculate Effective Address: $R1 + 40$)
    
5. `Zout, MARın, Read`
    
6. `WMFC`
    
7. `MDRout, Bus A, R2out, Bus B, Multiply, R3ın, END`
    

Would you like me to provide the **Assembly Program (Q4.b)** or the **Hardwired Design logic (Q5)**?