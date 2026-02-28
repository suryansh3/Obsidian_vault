



```bash

read -p "Enter a number: " num
sum=0
for (( i=1; i<num; i++ )); do
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


```

read -p "Enter a number: " n
if [ $n -lt 2 ]; then
    echo "$n is not prime."
    exit
fi
for ((i=2; i*i<=n; i++)); do
    if (( n % i == 0 )); then
        echo "$n is not a prime number."
        exit
    fi
done
echo "$n is a prime number."
```

### 3. Generate $n$ Prime Numbers



```

read -p "How many prime numbers to generate? " n
count=0
num=2
while [ $count -lt $n ]; do
    is_prime=1
    for ((i=2; i*i<=num; i++)); do
        if (( num % i == 0 )); then
            is_prime=0
            break
        fi
    done
    if [ $is_prime -eq 1 ]; then
        echo -n "$num "
        ((count++))
    fi
    ((num++))
done
echo ""
```

### 4. Lucas Sequence

The Lucas sequence starts with $1$ and $3$, where each subsequent number is the sum of the previous two ($L_n = L_{n-1} + L_{n-2}$).



```

read -p "Enter number of terms: " n
a=1
b=3
for (( i=0; i<n; i++ )); do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done
echo ""
```

### 5. Factorial of a Number



```

read -p "Enter a number: " n
fact=1
for (( i=1; i<=n; i++ )); do
    fact=$((fact * i))
done
echo "Factorial of $n is: $fact"
```

---

## Part 2: Nested Loop Patterns

### 1. Constant Number Rows



```

read -p "Enter n: " n
for (( i=1; i<=n; i++ )); do
    for (( j=1; j<=n; j++ )); do
        echo -n "$i "
    done
    echo ""
done
```

### 2. Sequential Numbers up to $n$ in $r$ Rows

This script distributes $n$ numbers evenly across $r$ rows.



```

read -p "Enter total numbers (n - even): " n
read -p "Enter number of rows (r): " r
cols=$(( n / r ))
current=1
for (( i=1; i<=r; i++ )); do
    for (( j=1; j<=cols; j++ )); do
        if [ $current -le $n ]; then
            echo -n "$current "
            ((current++))
        fi
    done
    echo ""
done
```

### 3. Increasing Number Triangle



```

read -p "Enter rows: " n
for (( i=1; i<=n; i++ )); do
    for (( j=1; j<=i; j++ )); do
        echo -n "$j "
    done
    echo ""
done
```

### 4. Asterisk Triangle



```

read -p "Enter rows: " n
for (( i=1; i<=n; i++ )); do
    for (( j=1; j<=i; j++ )); do
        echo -n "* "
    done
    echo ""
done
```

### 5. Alternating Ascending/Descending Triangle



```

read -p "Enter rows: " n
for (( i=1; i<=n; i++ )); do
    if (( i % 2 != 0 )); then
        # Odd row: Ascending
        for (( j=1; j<=i; j++ )); do
            echo -n "$j "
        done
    else
        # Even row: Descending
        for (( j=i; j>=1; j-- )); do
            echo -n "$j "
        done
    fi
    echo ""
done
```

### 6. Complex Asterisk-Number Pattern

This logic follows a decreasing row length, alternating between starting with an asterisk (odd rows) or starting with the number (even rows).



```

read -p "Enter n: " n
for (( i=n; i>=1; i-- )); do
    if (( i % 2 != 0 )); then
        # Start with asterisk
        for (( j=1; j<=i; j++ )); do
            echo -n "* $j "
        done
    else
        # Start with number
        for (( j=i; j>=1; j-- )); do
            echo -n "$j * "
        done
    fi
    echo ""
done
```

---
