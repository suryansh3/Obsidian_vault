---
course: "COA"
semester: 4
tags:
  - course/coa
up: "[[COA]]"
---
These are the solutions for the **SPRING MID SEMESTER EXAMINATION-2024** for **Computer Organization and Architecture**.

---

## **1. Section 1: Compulsory Short Answer Questions**

### **a) Address Bus Size Calculation**

- **Total Memory:** $16 \text{ TB} = 2^4 \times 2^{40} \text{ bytes} = 2^{44} \text{ bytes}$.
    
- **Word Size:** $8 \text{ bytes} = 2^3 \text{ bytes}$.
    
- **Number of Addressable Units (Words):** $\frac{2^{44}}{2^3} = 2^{41} \text{ words}$.
    
- **Address Bus Size:** At least **41 bits**.
    

### **b) Instruction Execution Steps (5 Special Purpose Registers)**

Execution typically involves these steps using **PC, MAR, MDR, IR, and Y (or Temp)**:

1. **Instruction Fetch:** Transfer address from **PC** to **MAR**; read memory; move instruction from **MDR** to **IR**.
    
2. **Instruction Decode:** Determine the operation and operand locations.
    
3. **Operand Fetch:** Load required data into registers or buffers.
    
4. **Execute:** Perform the operation (e.g., using the ALU).
    
5. **Write Back:** Store the result in the destination register or memory.
    

### **c) Von Neumann vs. Harvard Architecture**

- **Von Neumann:** Uses a **single shared memory** and bus for both instructions and data.
    
- **Harvard:** Uses **separate memories** and buses for instructions and data.
    
- **Practicality:** Harvard architecture is less common for general-purpose main memory because it requires twice the wiring and lacks the flexibility to dynamically allocate space between code and data.
    

### **d) System Bus Size**

The system bus consists of Data, Address, and Control lines:

- **Data Bus:** Matches word size = **64 bits**.
    
- **Address Bus:** $8 \text{ GB} = 2^{33} \text{ bytes}$. Word addressable with $2^3 \text{ byte words} \rightarrow \frac{2^{33}}{2^3} = 2^{30}$ words. Address lines = **30 bits**.
    
- **Control/Interrupt Lines:** $80 + 40 = \mathbf{120 \text{ lines}}$.
    
- **Total System Bus Size:** $64 + 30 + 120 = \mathbf{214 \text{ bits}}$.
    

### **e) Endianness for "-65"**

- **Decimal -65 in 16-bit Hex:** $+65 = 0041H$. 2’s complement of $0041H = FFBFH$.
    
- **Organization:** Byte-addressable, 16-bit words (2 bytes).
    

|**Address**|**Big Endian**|**Little Endian**|
|---|---|---|
|**2000**|$FF$ (MSB)|$BF$ (LSB)|
|**2001**|$BF$ (LSB)|$FF$ (MSB)|

---

## **2. Question 2**

**i) Step-by-Step Execution**

1. **Load LOCA, R1:**
    
    - **MAR $\leftarrow$ [IR(address field)]**: Address of LOCA moved to MAR.
        
    - **MDR $\leftarrow$ Memory[MAR]**: Data from LOCA read into MDR.
        
    - **R1 $\leftarrow$ MDR**: Data moved to R1.
        
2. **ADD R1, R0 (Result in R0):**
    
    - **ALU inputs $\leftarrow$ R1, R0**: Operands fed to the ALU.
        
    - **R0 $\leftarrow$ ALU Output**: Result stored in the destination register R0.
        

**ii) Addressing Modes**

_Given: Instruction at 1070, Address Field at 1071 (Value 1205). R1 = 1205._

_Memory: [1204]=1500, [1205]=2803, [1206]=4800, [2803]=1200._

|**Mode**|**Effective Address (EA)**|**Operand Value**|
|---|---|---|
|**(a) Auto-Increment**|$1205$|**2803** (R1 then becomes 1206)|
|**(b) Auto-Decrement**|$1204$ (R1 decrements first)|**1500**|

---

## 3.

Question 3: Code Analysis

### **(a.) Branch Offset for BGTZ**

- Instructions are 4 bytes.
    
- **LOOP** is at address **1012** (after 1000, 1004, 1008).
    
- **BGTZ** is at address **1020** (after 1012, 1016).
    
- The PC points to the _next_ instruction (**1024**) when BGTZ executes.
    
- **Offset** = Target - PC = $1012 - 1024 = \mathbf{-12}$.
    

### **(b.) PC Content when R1 is Zero**

- The loop runs 10 times (starts at 10).
    
- Once R1 becomes zero, the `BGTZ` (Branch Greater Than Zero) condition fails.
    
- The processor proceeds to the next instruction: **CALL SUB1**.
    
- The PC will be at address **1024**.
    

---

## 4.

Question 4: Machine Performance

**a) Calculations**

- **Clock Rate:** $200 \text{ MHz} \rightarrow \text{Cycle Time} = 5 \text{ ns}$.
    

|**Machine**|**Total Cycles (Millions)**|**Total Instructions**|**CPI**|**MIPS Rate**|**Execution Time**|
|---|---|---|---|---|---|
|**A**|$(8\times1)+(4\times3)+(2\times4)+(4\times3) = \mathbf{40}$|$18 \text{ M}$|$40/18 \approx \mathbf{2.22}$|$200/2.22 \approx \mathbf{90}$|$40\text{M} \times 5\text{ns} = \mathbf{0.2 \text{ s}}$|
|**B**|$(10\times1)+(8\times2)+(2\times4)+(4\times3) = \mathbf{46}$|$24 \text{ M}$|$46/24 \approx \mathbf{1.92}$|$200/1.92 \approx \mathbf{104}$|$46\text{M} \times 5\text{ns} = \mathbf{0.23 \text{ s}}$|

**b) Comment**

**Machine A is faster** for this specific benchmark set because it has a lower total cycle count (40M vs 46M), resulting in a shorter execution time (0.2s vs 0.23s), even though Machine B has a higher MIPS rate and lower CPI.

---

## **5. Question 5**

### **i) Status Bits for SUB R2, R1**

- **R1 = -16** ($1111 0000$), **R2 = 20** ($0001 0100$).
    
- **Operation:** $R1 - R2 \rightarrow (-16) - (+20) = \mathbf{-36}$.
    
- **Binary:** $1111 0000 + (2's \text{ comp of } 20: 1110 1100) = 1 1101 1100 \rightarrow \mathbf{1101 1 1 0 0}$.
    
- **V (Overflow):** **0** (-36 fits in 8-bit range).
    
- **N (Negative):** **1** (MSB is 1).
    
- **Z (Zero):** **0** (Result is not zero).
    
- **C (Carry):** **1** (Generated during subtraction of positive from negative).
    

### **ii) Stack Protection Routine**

Code snippet

```
; Stack range 1100 to 1500 [cite: 128]
PUSH: CMP SP, #1100    ; Check for Overflow
      BEQ OVERFLOW_ERR
      SUB SP, #4
      MOVE DATA, (SP)
      RET

POP:  CMP SP, #1500    ; Check for Underflow
      BEQ UNDERFLOW_ERR
      MOVE (SP), DATA
      ADD SP, #4
      RET
```

---

Would you like me to draw the **diagram for Harvard vs. Von Neumann** or the **Single-Bus CPU control steps** from the previous year's paper?

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[COA]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/COA/COA-MID-2023|COA-MID-2023]] · **Next:** [[04 - Academics & CS/Semester 4/COA/COA-MID-2025|COA-MID-2025]]
> **Related:** [[Operating Systems]] · [[Digital System Design]] · [[Mid-Semester]]
<!-- connections:end -->
