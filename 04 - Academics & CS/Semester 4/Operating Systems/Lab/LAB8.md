---
course: "Operating Systems"
semester: 4
tags:
  - course/operating-systems
up: "[[Operating Systems]]"
---

### 1. Perfect Number Test

```bash
# perfect.sh
read -p "Enter a number: " num
sum=0
for (( i=1; i<num; i++ ))
do
    if (( num % i == 0 )); then
        sum=$((sum + i))
    fi
done

if [ $sum -eq $num ]; then
    echo "$num is a Perfect Number."
else
    echo "$num is not a Perfect Number."
fi
```

**Terminal Output:**

```
kiit@linux:~$ sh perfect.sh
Enter a number: 6
6 is a Perfect Number.
```

---

### 2. Prime Number Check

```bash
# check_prime.sh
read -p "Enter n: " n
if [ $n -lt 2 ]
 then
    echo "$n is not prime."
    exit
fi
for (( i=2; i*i<=n; i++ ))
do
    if (( n % i == 0 ))
     then
        echo "$n is not a Prime Number."
        exit
    fi
done
echo "$n is a Prime Number."
```

**Terminal Output:**

```
kiit@linux:~$ sh check_prime.sh
Enter n: 17
17 is a Prime Number.
```

---

### 3. Generate $n$ Prime Numbers

```bash
# gen_primes.sh
read -p "Enter count (n): " n
count=0
num=2
while [ $count -lt $n ]
do
    is_prime=1
    for (( i=2; i*i<=num; i++ ))
    do
        if (( num % i == 0 ))
         then
            is_prime=0
            break
        fi
    done
    if [ $is_prime -eq 1 ]
     then
        echo -n "$num "
        ((count++))
    fi
    ((num++))
done
echo ""
```

**Terminal Output:**

```
kiit@linux:~$ sh gen_primes.sh
Enter count (n): 6
2 3 5 7 11 13 
```

---
### 4. Lucas Sequence

```bash
# lucas.sh
read -p "Enter number of terms: " n
a=1
b=3
for (( i=0; i<n; i++ ))
do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done
echo ""
```

**Terminal Output:**

```
kiit@linux:~$ sh lucas.sh
Enter number of terms: 7
1 3 4 7 11 18 29 
```

---
### 5. Factorial of a Number

```bash
# fact.sh
read -p "Enter a number: " n
fact=1
for (( i=1; i<=n; i++ ))
do
    fact=$((fact * i))
done
echo "Factorial is: $fact"
```

**Terminal Output:**

```
kiit@linux:~$ sh fact.sh
Enter a number: 5
Factorial is: 120
```

---
### 1. Constant Row Pattern

```bash
# pattern1.sh
read -p "Enter rows: " n
for (( i=1; i<=n; i++ ))
do
    for (( j=1; j<=n; j++ ))
    do
        echo -n "$i "
    done
    echo ""
done
```

**Terminal Output:**

```
kiit@linux:~$ sh pattern1.sh
Enter rows: 4
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 
```

---
### 2. Sequential Grid with Custom Rows

```bash
# pattern2.sh
read -p "Enter total n: " n
read -p "Enter rows r: " r
cols=$((n / r))
count=1
for (( i=1; i<=r; i++ ))
do
    for (( j=1; j<=cols; j++ ))
    do
        echo -n "$count "
        ((count++))
    done
    echo ""
done
```

**Terminal Output:**

```
kiit@linux:~$ sh pattern2.sh
Enter total n: 12
Enter rows r: 2
1 2 3 4 5 6 
7 8 9 10 11 12 
```

---

### 3 & 4. Right-Angled Triangles (Numbers and Stars)

```bash
# pattern3.sh
read -p "Enter n: " n
for (( i=1; i<=n; i++ ))
do
    for (( j=1; j<=i; j++ ))
    do
        echo -n "$j "
    done
    echo ""
done
```

**Terminal Output:**

```
kiit@linux:~$ sh pattern3.sh
Enter n: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

---

### 5. Alternating Reverse Pattern

```bash
# pattern5.sh
read -p "Enter rows: " n
for (( i=1; i<=n; i++ ))
do
    if (( i % 2 != 0 )); then
        for (( j=1; j<=i; j++ )); do echo -n "$j "
         done
    else
        for (( j=i; j>=1; j-- )); do echo -n "$j "
         done
    fi
    echo ""
done
```

**Terminal Output:**

```
kiit@linux:~$ sh pattern5.sh
Enter rows: 5
1 
2 1 
1 2 3 
4 3 2 1 
1 2 3 4 5 
```

---

### 6. Complex Inverted Pattern

```bash
# pattern6.sh
read -p "Enter starting row count: " n
for (( i=n; i>=1; i-- ))
do
    if (( i % 2 != 0 )); then
        for (( j=1; j<=i; j++ )); do echo -n "* $j "
         done
    else
        for (( j=i; j>=1; j-- )); do echo -n "$j * "
         done
    fi
    echo ""
done
```

**Terminal Output:**

```
kiit@linux:~$ sh pattern6.sh
Enter starting row count: 5
* 1 * 2 * 3 * 4 * 5 
4 * 3 * 2 * 1 * * 1 * 2 * 3 
2 * 1 * * 1 
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Operating Systems]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 4/Operating Systems/Lab/Assignment-07|Assignment-07]] · **Next:** [[04 - Academics & CS/Semester 4/Operating Systems/Lab/OS Assignment-5|OS Assignment-5]]
> **Related:** [[OOPJ (Java)]] · [[COA]] · [[CN]]
<!-- connections:end -->
