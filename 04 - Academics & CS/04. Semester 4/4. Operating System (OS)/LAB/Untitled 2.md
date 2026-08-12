Based on the mention of **"echo or bash"** in the final question, I have solved these problems using **Bash scripting**.

Here are the solutions for each task.

### 1) Swap two integers using a temporary variable

Bash

```
#!/bin/bash
a=10
b=20

echo "Before: a=$a, b=$b"

# Logic
temp=$a
a=$b
b=$temp

echo "After:  a=$a, b=$b"
```

---

### 3) Swap two integers without using a temporary variable

We use arithmetic operations (Sum and Difference) to achieve this.

Bash

```
#!/bin/bash
a=10
b=20

echo "Before: a=$a, b=$b"

# Logic
a=$((a + b))  # a becomes 30
b=$((a - b))  # b becomes 10 (original a)
a=$((a - b))  # a becomes 20 (original b)

echo "After:  a=$a, b=$b"
```

---

### 4) Cyclic Swap of three variables

Requirement: $a \to b$, $b \to c$, $c \to a$.

(If $a=1, b=2, c=3$ becomes $a=3, b=1, c=2$)

Bash

```
#!/bin/bash
a=1
b=2
c=3

echo "Before: a=$a, b=$b, c=$c"

# Logic: Store 'c' (the last one) in temp, shift right
temp=$c
c=$b
b=$a
a=$temp

echo "After:  a=$a, b=$b, c=$c"
```

---

### 5) Find the largest of three distinct integers

Bash

```
#!/bin/bash
a=10
b=25
c=15

if [[ $a -gt $b && $a -gt $c ]]; then
    echo "Largest is $a"
elif [[ $b -gt $a && $b -gt $c ]]; then
    echo "Largest is $b"
else
    echo "Largest is $c"
fi
```

---

### 6) Find the middle of three distinct integers

Bash

```
#!/bin/bash
a=10
b=50
c=30

# Logic: Check if a number is between the other two
if [[ ($a -gt $b && $a -lt $c) || ($a -lt $b && $a -gt $c) ]]; then
    echo "Middle is $a"
elif [[ ($b -gt $a && $b -lt $c) || ($b -lt $a && $b -gt $c) ]]; then
    echo "Middle is $b"
else
    echo "Middle is $c"
fi
```

---

### 7) Display all values from `a` to `b` (inclusive)

Condition: $a < b$.

Bash

```
#!/bin/bash
a=5
b=10

# Using Brace Expansion (only works if a and b are constants/literals)
# For variables, we use `seq` or a C-style for loop:

for ((i=a; i<=b; i++)); do
    echo -n "$i "
done
echo ""
```

---

### 8) Display all even numbers from 0 to `n`

Bash

```
#!/bin/bash
n=10

for ((i=0; i<=n; i+=2)); do
    echo -n "$i "
done
echo ""
```

---

### 9) Display integers if even and not divisible by 3

Range assumed from 0 to `n`.

Bash

```
#!/bin/bash
n=20

for ((i=0; i<=n; i++)); do
    # Check if even (i%2==0) AND not divisible by 3 (i%3!=0)
    if (( i % 2 == 0 && i % 3 != 0 )); then
        echo -n "$i "
    fi
done
echo ""
```

_Output for n=20: 2 4 8 10 14 16 20 (Skips 0, 6, 12, 18)_

---

### 10) Display values from $2^{(a-b)}$ to $2^{(a+b)}$ (Float)

Bash does not handle floating point math natively, so we use `bc` for calculation and `seq` to generate the range.

Bash

```
#!/bin/bash
a=3
b=5

# Calculate powers using bc
# power(a-b) = 3-5 = -2 -> 2^-2 = 0.25
# power(a+b) = 3+5 = 8  -> 2^8  = 256

start=$(echo "scale=4; 2^($a - $b)" | bc -l)
end=$(echo "2^($a + $b)" | bc)

echo "Range: $start to $end"

# Use seq to print values. 
# Step is 1 by default.
seq $start 1 $end
```

**Would you like me to wrap any of these into a single executable script file for you to run?**