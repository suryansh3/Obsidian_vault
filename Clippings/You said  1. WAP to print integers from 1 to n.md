---
title: You said  1. WAP to print integers from 1 to n.  ...
source: https://gemini.google.com/app/2135e37464493a19
author:
  - "[[Gemini]]"
published:
created: 2026-02-22
description: Meet Gemini, Google’s AI assistant. Get help with writing, planning, brainstorming, and more. Experience the power of generative AI.
tags:
  - clippings
  - "#IPA"
---
1\. WAP to print integers from 1 to n.

2\. WAP to print even integers from 1 to n where n is user input.

3\. Take two numbers p and q where p < q and print from 1 to q but skip the iteration at p.

4\. WAP to take 10 different numbers as input. Print their sum and average.

5\. WAP to find out sum of digits of a number.

6\. WAP to find out reverse of a number.

7\. WAP to find out factors of a number.

8\. WAP to test whether a number is Armstrong Number or not.

(A number is said to be Armstrong when the sum of cubes of its digit is equal with the original number.

Ex-153)

9\. WAP to test whether a number is Palindrome Number or not.

(A number is said to be Palindrome when its reverse is equal with the original number.

Ex-121)

10\. WAP to print Fibonacci series up to n terms. Give solution for each question in bash

---

Here are the Bash scripts for each of your requirements. I've written these to be clean and easy to understand.

To run these, save them as `.sh` files (e.g., `script.sh`), give them execution permissions with `chmod +x script.sh`, and run them using `./script.sh`.

---

### 1\. Print Integers from 1 to

Bash

```
#!/bin/bash
read -p "Enter n: " n
for (( i=1; i<=n; i++ ))
do
    echo "$i"
done
```

### 2\. Print Even Integers from 1 to

Bash

```
#!/bin/bash
read -p "Enter n: " n
echo "Even numbers up to $n:"
for (( i=2; i<=n; i+=2 ))
do
    echo "$i"
done
```

### 3\. Print 1 to but Skip Iteration at

Bash

```
#!/bin/bash
read -p "Enter p: " p
read -p "Enter q (where q > p): " q

for (( i=1; i<=q; i++ ))
do
    if [ $i -eq $p ]; then
        continue
    fi
    echo "$i"
done
```

---

### 4\. Sum and Average of 10 Numbers

Bash

```
#!/bin/bash
sum=0
echo "Enter 10 numbers:"
for (( i=1; i<=10; i++ ))
do
    read -p "Number $i: " num
    sum=$((sum + num))
done

avg=$(echo "scale=2; $sum / 10" | bc)
echo "Sum: $sum"
echo "Average: $avg"
```

### 5\. Sum of Digits

Bash

```
#!/bin/bash
read -p "Enter a number: " n
sum=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    sum=$((sum + digit))
    n=$((n / 10))
done
echo "Sum of digits: $sum"
```

### 6\. Reverse of a Number

Bash

```
#!/bin/bash
read -p "Enter a number: " n
rev=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    rev=$((rev * 10 + digit))
    n=$((n / 10))
done
echo "Reversed number: $rev"
```

---

### 7\. Factors of a Number

Bash

```
#!/bin/bash
read -p "Enter a number: " n
echo "Factors of $n are:"
for (( i=1; i<=n; i++ ))
do
    if [ $((n % i)) -eq 0 ]; then
        echo "$i"
    fi
done
```

### 8\. Armstrong Number Check

An Armstrong number (for 3 digits) is where the sum of the cubes of its digits equals the number itself.

Bash

```
#!/bin/bash
read -p "Enter a number: " n
original=$n
sum=0

while [ $n -gt 0 ]
do
    digit=$((n % 10))
    sum=$((sum + (digit * digit * digit)))
    n=$((n / 10))
done

if [ $sum -eq $original ]; then
    echo "$original is an Armstrong number."
else
    echo "$original is not an Armstrong number."
fi
```

### 9\. Palindrome Number Check

Bash

```
#!/bin/bash
read -p "Enter a number: " n
original=$n
rev=0

while [ $n -gt 0 ]
do
    digit=$((n % 10))
    rev=$((rev * 10 + digit))
    n=$((n / 10))
done

if [ $original -eq $rev ]; then
    echo "$original is a Palindrome."
else
    echo "$original is not a Palindrome."
fi
```

### 10\. Fibonacci Series up to Terms

---

**Quick Tip:** For the average calculation in script #4, I used `bc` (Basic Calculator). If you don't have it installed, you can install it via `sudo apt install bc`, otherwise, Bash will only perform integer division (dropping the decimals).

Would you like me to explain the logic behind any specific script, like how the Armstrong check or Fibonacci loop works?

---

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

Conversation with Gemini

  

You said

  

1\. WAP to print integers from 1 to n.

2\. WAP to print even integers from 1 to n where n is user input.

3\. Take two numbers p and q where p < q and print from 1 to q but skip the iteration at p.

4\. WAP to take 10 different numbers as input. Print their sum and average.

5\. WAP to find out sum of digits of a number.

6\. WAP to find out reverse of a number.

7\. WAP to find out factors of a number.

8\. WAP to test whether a number is Armstrong Number or not.

(A number is said to be Armstrong when the sum of cubes of its digit is equal with the original number.

Ex-153)

9\. WAP to test whether a number is Palindrome Number or not.

(A number is said to be Palindrome when its reverse is equal with the original number.

Ex-121)

10\. WAP to print Fibonacci series up to n terms. Give solution for each question in bash.

And also give random input to give output after each question solution.

---

Building logic in Bash is a great way to understand how shell scripting handles arithmetic and loops. Below are the solutions for each of your requests, followed by a sample input and output for each.

I have used the `bc` utility for the average calculation to ensure you get decimal precision.

---

### 1\. Print Integers from 1 to

Bash

```
#!/bin/bash
read -p "Enter the value of n: " n
for (( i=1; i<=n; i++ ))
do
    echo -n "$i "
done
echo ""
```

**Sample Input:**`n = 5`

**Sample Output:**`1 2 3 4 5`

---

### 2\. Print Even Integers from 1 to

Bash

```
#!/bin/bash
read -p "Enter the value of n: " n
for (( i=1; i<=n; i++ ))
do
    if [ $((i % 2)) -eq 0 ]; then
        echo -n "$i "
    fi
done
echo ""
```

**Sample Input:**`n = 10`

**Sample Output:**`2 4 6 8 10`

---

### 3\. Print 1 to and Skip

Bash

```
#!/bin/bash
read -p "Enter p (to skip): " p
read -p "Enter q (limit): " q
for (( i=1; i<=q; i++ ))
do
    if [ $i -eq $p ]; then
        continue
    fi
    echo -n "$i "
done
echo ""
```

**Sample Input:**`p = 3, q = 7`

**Sample Output:**`1 2 4 5 6 7`

---

### 4\. Sum and Average of 10 Numbers

Bash

```
#!/bin/bash
sum=0
echo "Enter 10 numbers:"
for (( i=1; i<=10; i++ ))
do
    read -p "Num $i: " num
    sum=$((sum + num))
done
avg=$(echo "scale=2; $sum / 10" | bc)
echo "Sum: $sum"
echo "Average: $avg"
```

**Sample Input:**`1, 2, 3, 4, 5, 6, 7, 8, 9, 10`

**Sample Output:**`Sum: 55`

`Average: 5.50`

---

### 5\. Sum of Digits

To extract digits, we use the modulo operator (`%`) to get the last digit and integer division (`/`) to remove it.

Bash

```
#!/bin/bash
read -p "Enter a number: " n
sum=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    sum=$((sum + digit))
    n=$((n / 10))
done
echo "Sum of digits: $sum"
```

**Sample Input:**`456`

**Sample Output:**`Sum of digits: 15`

---

### 6\. Reverse of a Number

Bash

```
#!/bin/bash
read -p "Enter a number: " n
rev=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    rev=$((rev * 10 + digit))
    n=$((n / 10))
done
echo "Reversed number: $rev"
```

**Sample Input:**`1234`

**Sample Output:**`Reversed number: 4321`

---

### 7\. Factors of a Number

Bash

```
#!/bin/bash
read -p "Enter a number: " n
echo -n "Factors: "
for (( i=1; i<=n; i++ ))
do
    if [ $((n % i)) -eq 0 ]; then
        echo -n "$i "
    fi
done
echo ""
```

**Sample Input:**`12`

**Sample Output:**`Factors: 1 2 3 4 6 12`

---

### 8\. Armstrong Number Check

An Armstrong number is one where the sum of the cubes of its digits equals the number itself.

Bash

```
#!/bin/bash
read -p "Enter a number: " n
original=$n
sum=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    sum=$((sum + (digit * digit * digit)))
    n=$((n / 10))
done
if [ $sum -eq $original ]; then
    echo "$original is an Armstrong number"
else
    echo "$original is NOT an Armstrong number"
fi
```

**Sample Input:**`153`

**Sample Output:**`153 is an Armstrong number` (Since )

---

### 9\. Palindrome Number Check

Bash

```
#!/bin/bash
read -p "Enter a number: " n
original=$n
rev=0
temp=$n
while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    rev=$((rev * 10 + digit))
    temp=$((temp / 10))
done
if [ $original -eq $rev ]; then
    echo "$original is a Palindrome"
else
    echo "$original is NOT a Palindrome"
fi
```

**Sample Input:**`121`

**Sample Output:**`121 is a Palindrome`

---

### 10\. Fibonacci Series up to terms

The logic involves keeping track of the current number and the previous number, then sliding them forward.

**Sample Input:**`n = 6`

**Sample Output:**`Fibonacci Series: 0 1 1 2 3 5`

---

**Next Step:** Would you like me to explain how to make these scripts more robust by adding **input validation** (e.g., checking if the user actually entered a number)?