I’ve read the course PDFs (hazard, branch-penalty, dynamic-prediction, speedup-with-stalls, performance, and pipeline slides) and solved every question using **the slides’ own conventions**: 5-stage IF/ID/EX/MEM/WB pipeline (slide 8), register write in 1st half / read in 2nd half of a cycle (slide 13), no-forwarding ⇒ operand read in ID must wait for producer’s WB, load-use with forwarding ⇒ 1 stall (slide 13’s LD→DADD example), store needs no WB = 4 cycles, J/branch resolved in ID with 1-cycle penalty (slides 14, 16), Amdahl’s law Sp = 1/[(1−fₑ)+fₑ/Sₚₑ] (slide 12), and the 1-bit / 2-bit predictor state machines of slide 17. I verified the Q3 schedules and Q4 traces cycle-by-cycle (a script cross-check timed out, so the tables below were hand-traced against the slide rules).

---

# Q1. Maximum overall speedup (Amdahl’s Law) — [1]

**Given:** total time = 100 s; multiply = 80 s; only multiply can be enhanced.

From the slides (12-HPC-2026-6TH-AUG-Performance-Measurement.pdf):

$$S_{overall} = \frac{1}{(1-f_e) + \dfrac{f_e}{S_{pe}}}$$

- Fraction enhanced: fₑ = 80/100 = **0.8**; non-enhanced fraction = 1 − fₑ = 0.2 (the 20 s of non-multiply work)
- Best case: enhancement speedup Sₚₑ → ∞, so fₑ/Sₚₑ → 0

$$S_{max} = \frac{1}{(1-0.8) + 0} = \frac{1}{0.2} = \boxed{5}$$

**Justification:** even if multiplication were made infinitely fast, the 20 s of non-multiply work remains. New time ≥ 20 s, so speedup ≤ 100/20 = **5**. The performance gain is limited by the fraction of time the faster mode can be used (Amdahl’s law).

---

# Q2. Speedup of a pipelined computer considering stalls — [1]

Following 15-HPC-2026-18TH-AUG-pipeline-speed-up-stallls.pdf (same IC on both machines):

$$S_p=\frac{\text{avg. inst. time}_{unpipelined}}{\text{avg. inst. time}_{pipelined}}=\frac{CPI_{unpipelined}\times CT_{unpipelined}}{CPI_{pipelined}\times CT_{pipelined}}$$

**Case 1 — stages properly balanced (CT equal):** unpipelined CPI = d (pipeline depth k), and with stalls

$$CPI_{pipelined}=1+\text{stall cycles/inst}$$

$$\boxed{S_p=\frac{d}{1+\text{stall cycles per instruction}}}$$

**Case 2 — stages not balanced** (unpipelined takes 1 long cycle; CT_pipe = CT_unpipelined/k):

$$S_p=\frac{1\times CT_{unpipelined}}{[1+\text{stall/inst}]\times \frac{CT_{unpipelined}}{k}}=\frac{k}{1+\text{stall cycles/inst}}$$

In MIPS the ideal CPI = 1, and stalls/instruction = branch frequency × branch penalty + data-hazard stalls per instruction, giving Sp = k / (1 + stalls per instruction).

---

# Q3. Clock cycles with and without operand forwarding — [1.5]

Program (registers R1–R13 = 1–13 initially; `LD Ra, off(Rb)` = Ra ← DM[[Rb]+off], `SD Ra, off(Rb)` = DM[[Rb]+off] ← Ra):

```
I1: LD   R1, 09(R10)     I5: LD  R4, 11(R7)
I2: LD   R2, 10(R9)      I6: J   4        ← jump; [PC] = [NPC] + 4 ⇒ skips I7
I3: DADD R3, R1, R2      I7: SD  R5, 12(R4)   (skipped dead code)
I4: SD   R3, 08(R8)      I8: OR  R6, R4, R5   (target; executes)
```

`J` is resolved in ID (slide 14: “target address is known at end of ID stage”) → the sequential fetch made in that cycle (I7) is flushed and refetch starts at the target ⇒ **1-cycle branch penalty** (slide 16). So 7 instructions execute. R5 is never written (its producer I7 is skipped), so OR’s R5 source creates no hazard. RAW dependencies: I3←(I1,I2), I4←I3 (store data), I8←I5.

### (a) WITHOUT operand forwarding — read in ID, must be ≥ producer’s WB (write in WB; slide 13 example)

|Instr|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1 LD R1|IF|ID|EX|M|**WB**||||||||||||
|I2 LD R2||IF|ID|EX|M|**WB**|||||||||||
|I3 DADD R3|||IF|ID|s|s|EX|M|**WB**||||||||
|I4 SD R3||||IF|s|s|s|s|ID|EX|M||||||
|I5 LD R4|||||IF|s|s|s|s|ID|EX|M|**WB**||||
|I6 J 4||||||IF||||ID|||||||
|I7 SD R5|||||||IF|—|—|—|✕ flushed||||||
|I8 OR R6||||||||||||IF|ID|EX|M|WB|

- I3 stalls 2 cycles (R1 ready WB-5, R2 ready WB-6 → ID at 6)
- I4 stalls until R3 is written (WB-9 → ID at 9)
- I8 stalls until R4 is written (WB-13 → ID at 13); jump penalty absorbed before it

**Total = 16 clock cycles**

### (b) WITH operand forwarding (slides 13/16: EX→EX/MEM forwarding for ALU results ⇒ 0 stalls; load-use ⇒ 1 stall; store data forwarded EX/MEM→MEM ⇒ 0 stalls)

|Instr|1|2|3|4|5|6|7|8|9|10|11|12|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|I1 LD R1|IF|ID|EX|M|WB|||||||||
|I2 LD R2||IF|ID|EX|M|WB||||||||
|I3 DADD R3|||IF|ID|**s**|EX|M|WB||||||
|I4 SD R3||||IF|s|ID|EX|M||||||
|I5 LD R4|||||IF|s|ID|EX|M|WB||||
|I6 J 4||||||IF||ID||||||
|I7 SD R5|||||||IF|✕ flushed||||||
|I8 OR R6|||||||||IF|ID|EX|M|WB|

- Only **1 stall**: load-use on I3 (R2 from I2’s MEM/WB forwarded to I3’s EX in cycle 6)
- I4’s data R3 forwarded from I3’s EX/MEM to I4’s MEM (cycle 8) — no stall
- I8’s R4 forwarded from I5’s MEM/WB (M-9 → EX at 11) — no stall

**Total = 13 clock cycles** (7 + 5 − 1 = 11 base + 1 load-use stall + 1 jump penalty)

> _Note on interpretation:_ this takes `J 4` as PC-relative ([NPC]+4), so it skips the unreachable store `SD R5,12(R4)` — consistent with R5 never being produced. If instead your class convention treats the jump as targeting I7 (all 8 instructions execute), the same rules give **18 cycles without forwarding and 14 cycles with forwarding**; the hazard analysis above is unchanged either way.

---

# Q4. Branch outcome and 1-bit / 2-bit prediction — [1.5]

```
for (int i=0; i<15; i=i+2)      // reading "i<15,i=i+2" as the intended i<15, i=i+2
    s[i] = s[i] + 5;
```

**Actual outcome of the branch (i<15):** the loop body runs for i = 0,2,4,6,8,10,12,14 — the branch is **TAKEN 7 times**; then i = 16 makes the condition false — **NOT TAKEN once**.

**Actual sequence (8 branch evaluations):** T, T, T, T, T, T, T, NT

### 1-bit predictor, initial state NT (slide 17: prediction flips after every miss)

|Eval|Actual|Predicted|Result|State after|
|---|---|---|---|---|
|1|T|NT|**MISS**|T|
|2|T|T|hit|T|
|3|T|T|hit|T|
|4|T|T|hit|T|
|5|T|T|hit|T|
|6|T|T|hit|T|
|7|T|T|hit|T|
|8|NT|T|**MISS**|NT|

**1-bit: Misses = 2, Correct predictions = 6**

### 2-bit predictor, initial state 00 = strong NT (slide 17 state machine: 00,01 predict NT; 10,11 predict T; state moves one step per outcome, prediction flips only after **two** consecutive misses)

|Eval|Actual|State (before)|Predicted|Result|State (after)|
|---|---|---|---|---|---|
|1|T|00|NT|**MISS**|01|
|2|T|01|NT|**MISS**|10|
|3|T|10|T|hit|11|
|4|T|11|T|hit|11|
|5|T|11|T|hit|11|
|6|T|11|T|hit|11|
|7|T|11|T|hit|11|
|8|NT|11|T|**MISS**|10|

**2-bit: Misses = 3, Correct predictions = 5**

**Comparison:** for this loop the 1-bit predictor (2 misses) beats the 2-bit predictor (3 misses), because the 2-bit scheme needs two mispredictions to learn the taken behavior after starting in strong-NT, while the single final NT only costs each scheme one miss.