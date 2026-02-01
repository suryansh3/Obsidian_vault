This response provides solutions for the **SPRING MID SEMESTER EXAMINATION-2023** for **Computer Architecture (CS 2006)**.

---

## **1. Section 1: Compulsory Short Answer Questions**

### **a) Compare Instruction Analysis**

**Instruction:** `Compare R1, R2` (Initially $R1=10, R2=20$).

- **Final Value of R1:** **10**. The Compare instruction is non-destructive and does not change the source or destination register values.
    
- **Final Value of R2:** **20**.
    

### **b) Memory References**

- **INC A (2-WORD instruction):** **2 references**. Both references are used for fetching the 2-word instruction from memory; no additional reference is needed as 'A' is an internal register.
    
- **JMP L1 (2-WORD instruction):** **2 references**. These are required to fetch the 2-word instruction.
    

### **c) Shift Instruction (Multiply by 128)**

- To multiply an unsigned integer by $128$ ($2^7$) without using `MUL`, use a **Logical Shift Left (LSL)** by 7 bits.
    
- **Instruction:** `LSL R1, #7` (or `SHL R1, 7` depending on the instruction set).
    

### **d) Importance of RUN and END Signals**

- **RUN Signal:** This signal indicates that the processor is currently in the execution phase of an instruction cycle and prevents other processes from interrupting the bus until the cycle is complete.
    
- **END Signal:** This signal indicates the completion of the current instruction's execution. It triggers the start of the next Instruction Fetch cycle.
    

### **e) Possible Values of PC (Branch Instruction)**

**Instruction:** `2000: Branch>0 1000` (1 word = 4 bytes).

- **If Condition is True (Value > 0):** The PC will be loaded with the target address **1000**.
    
- **If Condition is False (Value ≤ 0):** The PC will increment to the next sequential instruction: **2004** ($2000 + 4$).
    

---

## **2. Question 2: Endianness and Performance**

### **A) Endianness for "-20"**

- **Value:** $-20$ in 32-bit hex. $+20 = 00000014H$. 2's complement = **FFFFFFECH**.
    
- **Organization:** Byte-addressable, 32-bit words (4 bytes) starting at address 2000.
    

|**Address**|**Big Endian**|**Little Endian**|
|---|---|---|
|**2000**|$FF$ (MSB)|$EC$ (LSB)|
|**2001**|$FF$|$FF$|
|**2002**|$FF$|$FF$|
|**2003**|$EC$ (LSB)|$FF$ (MSB)|
||||

### **B) Performance Comparison**

- **System-1:** $100 \text{ MHz}$, 200 instructions.
    
    - **Cycles:** $(100 \times 4) + (50 \times 2) + (10 \times 8) + (40 \times 5) = 400 + 100 + 80 + 200 = \mathbf{780 \text{ cycles}}$.
        
    - **Execution Time:** $\frac{780}{100 \times 10^6} = \mathbf{7.8 \text{ \mu s}}$.
        
- **System-2:** $50 \text{ MHz}$, 150 instructions.
    
    - **Cycles:** $(60 \times 3) + (45 \times 2) + (15 \times 10) + (30 \times 7) = 180 + 90 + 150 + 210 = \mathbf{630 \text{ cycles}}$.
        
    - **Execution Time:** $\frac{630}{50 \times 10^6} = \mathbf{12.6 \text{ \mu s}}$.
        
- **Conclusion:** **System-1** gives better performance because its execution time is lower.
    

---

## **3. Question 3: Control Units and Subroutines**

### **A) Microprogrammed Control Unit**

- **Working Principle:** It uses a control store (ROM) to store a sequence of microinstructions. The Control Address Register (CAR) identifies the next microinstruction to be executed based on the opcode in the Instruction Register (IR).
    
- **Speed Comparison:** **Hardwired units are faster** because the control signals are generated through combinatorial logic gates with minimal delay. Microprogrammed units are slower because they require a memory access to the control store for every micro-operation.
    

### **B) Subroutine Execution Trace**

Initial: SP = 5000, Word Size = 4 bytes (Decreasing order).

|**Condition**|**PC**|**SP**|**Top of Stack Value**|
|---|---|---|---|
|**i) After CALL SUB1 (Main)**|3000|4996|2012 (Return address)|
|**ii) After CALL SUB2 (SUB1)**|4000|4992|3008 (Return address)|
|**iii) After Return from SUB2**|3008|4996|2012|
|**iv) After Return from SUB1**|2012|5000|1000|
|||||

---

## **4. Question 5: CPU Organization**

### **A) Three-Bus CPU Organization**

- **Constant 4:** In a byte-addressable machine with 32-bit (4-byte) words, the **Constant 4** is used to increment the Program Counter (PC) to the next word address during the fetch cycle ($PC \leftarrow PC + 4$).
    

### **B) Single-Bus Control Signals for RETURN**

The `RETURN` instruction pops the return address from the stack back into the PC.

1. **Fetch:** `PCout, MARin, Read, Select4, Add, Zin`
    
2. **Wait:** `Zout, PCin, WMFC`
    
3. **Decode:** `MDRout, IRin`
    
4. **Pop PC:** `SPout, MARin, Read`
    
5. **Update SP:** `SPout, Select4, Add, Zin, WMFC`
    
6. **Finalize:** `Zout, SPin, MDRout, PCin, END`
    

---

Would you like me to provide the **Assembly Language Programs** for **SAFEPUSH/SAFEPOP (Q4.A)** or **Array Swapping (Q4.B)**?