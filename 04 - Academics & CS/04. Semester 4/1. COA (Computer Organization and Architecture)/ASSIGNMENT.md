## Gemini said

Booth’s Algorithm is specifically designed to handle signed multiplication efficiently by reducing the number of additions required.

To multiply these values using 4-bit registers (plus a sign bit where necessary), let's establish the constants:

- **M (+7):** 0111
    
- **-M (-7):** 1001 (2's complement of 0111)
    

---

### **i. 7×3 (Positive × Positive)**

- **M:** 0111 | **-M:** 1001 | **Q (Multiplier):** 0011 | **n:** 4
    

| Count    | A (Accumulator) | Q (Multiplier) | Q−1​  | Action (Q0​,Q−1​)                 |
| -------- | --------------- | -------------- | ----- | --------------------------------- |
| **Init** | 0000            | 0011           | 0     | Initial State                     |
| **1**    | 1001            | 0011           | 0     | 1,0→A=A−M                         |
|          | **1100**        | **1001**       | **1** | **ASHR** (Arithmetic Shift Right) |
| **2**    | 1110            | 0100           | **1** | 1,1→ **ASHR only**                |
| **3**    | 0101            | 0100           | 1     | 0,1→A=A+M                         |
|          | **0010**        | **1010**       | **0** | **ASHR**                          |
| **4**    | **0001**        | **0101**       | **0** | 0,0→ **ASHR only**                |

**Result:** 000101012​=21

---

### **ii. −7×3 (Negative × Positive)**

- **M:** 1001 (−7) | **-M:** 0111 (+7) | **Q:** 0011 (3)
    

|Count|A|Q|Q−1​|Action|
|---|---|---|---|---|
|**Init**|0000|0011|0|Initial State|
|**1**|0111|0011|0|1,0→A=A−M (Subtracting −7 is +7)|
||**0011**|**1001**|**1**|**ASHR**|
|**2**|**0001**|**1100**|**1**|1,1→ **ASHR only**|
|**3**|1010|1100|1|0,1→A=A+M (0001+1001)|
||**1101**|**0110**|**0**|**ASHR**|
|**4**|**1110**|**1011**|**0**|0,0→ **ASHR only**|

**Result:** 111010112​. In 2's complement, this is **−21**.

---

### **iii. 7×−3 (Positive × Negative)**

- **M:** 0111 (7) | **-M:** 1001 (−7) | **Q:** 1101 (−3)
    

| Count    | A        | Q        | Q−1​  | Action                |
| -------- | -------- | -------- | ----- | --------------------- |
| **Init** | 0000     | 1101     | 0     | Initial State         |
| **1**    | 1001     | 1101     | 0     | 1,0→A=A−M             |
|          | **1100** | **1110** | **1** | **ASHR**              |
| **2**    | 0011     | 1110     | 1     | 0,1→A=A+M (1100+0111) |
|          | **0001** | **1111** | **0** | **ASHR**              |
| **3**    | 1010     | 1111     | 0     | 1,0→A=A−M             |
|          | **1101** | **0111** | **1** | **ASHR**              |
| **4**    | **1110** | **1011** | **1** | 1,1→ **ASHR only**    |

**Result:** 111010112​=−21

---

### **iv. −7×−3 (Negative × Negative)**

- **M:** 1001 (−7) | **-M:** 0111 (+7) | **Q:** 1101 (−3)
    

|Count|A|Q|Q−1​|Action|
|---|---|---|---|---|
|**Init**|0000|1101|0|Initial State|
|**1**|0111|1101|0|1,0→A=A−M (Add +7)|
||**0011**|**1110**|**1**|**ASHR**|
|**2**|1100|1110|1|0,1→A=A+M (Add −7)|
||**1110**|**0111**|**0**|**ASHR**|
|**3**|0101|0111|0|1,0→A=A−M (Add +7)|
||**0010**|**1011**|**1**|**ASHR**|
|**4**|**0001**|**0101**|**1**|1,1→ **ASHR only**|

**Result:** 000101012​=21

Would you like me to explain how to convert these binary results back to decimal using the 2's complement method?