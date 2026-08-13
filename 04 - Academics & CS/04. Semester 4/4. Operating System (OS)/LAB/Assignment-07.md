
1.

``` bash
read -p "Enter n: " n
for ((i = 1; i <= n; i++)); do
  echo "$i"
done
```

``` text
kitt@kiit in ~/Documents/OS-LAB/LAB7 took 3m35s940ms
 󰛓 ❯ sh 1.sh
Enter n: 7
1
2
3
4
5
6
7

```

---

2.

``` bash
read -p "Enter n: " n
echo "Even numbers up to $n:"
for ((i = 2; i <= n; i += 2)); do
  echo "$i"
done

```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 29s929ms
 󰛓 ❯ sh 2.sh
Enter n: 10
Even numbers up to 10:
2
4
6
8
10

```

---

3.
```bash
read -p "Enter p: " p
read -p "Enter q (where q > p): " q

for ((i = 1; i <= q; i++)); do
  if [ $i -eq $p ]; then
    continue
  fi
  echo "$i"
done
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 2s107ms
 󰛓 ❯ sh 3.sh
Enter p: 3
Enter q (where q > p): 7
1
2
4
5
6
7
```

---

4.
```bash
sum=0
echo "Enter 10 numbers:"
for ((i = 1; i <= 10; i++)); do
  read -p "Number $i: " num
  sum=$((sum + num))
done

avg=$(echo "scale=2; $sum / 10" | bc)
echo "Sum: $sum"
echo "Average: $avg"
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 19s913ms
 󰛓 ❯ sh 4.sh
Enter 10 numbers:
Number 1: 1
Number 2: 3
Number 3: 4
Number 4:
Number 5: 2
Number 6: 5
Number 7: 6
Number 8: 7
Number 9: 12
Number 10: 3
Sum: 43
Average: 4.30
```

---

5.
```bash
read -p "Enter a number: " n
sum=0
while [ $n -gt 0 ]; do
  digit=$((n % 10))
  sum=$((sum + digit))
  n=$((n / 10))
done
echo "Sum of digits: $sum"
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 10s133ms
 󰛓 ❯ sh 5.sh
Enter a number: 12
Sum of digits: 3
```

---
6.

```bash
read -p "Enter a number: " n
rev=0
while [ $n -gt 0 ]; do
  digit=$((n % 10))
  rev=$((rev * 10 + digit))
  n=$((n / 10))
done
echo "Reversed number: $rev"
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 25s241ms
 󰛓 ❯ sh 6.sh
Enter a number: 12
Reversed number: 21
```

---

7.

```bash
read -p "Enter a number: " n
echo "Factors of $n are:"
for ((i = 1; i <= n; i++)); do
  if [ $((n % i)) -eq 0 ]; then
    echo "$i"
  fi
done
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 17s369ms
 󰛓 ❯ sh 7.sh
Enter a number: 12
Factors of 12 are:
1
2
3
4
6
12
```

---

8.

```bash
read -p "Enter a number: " n
original=$n
sum=0

while [ $n -gt 0 ]; do
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

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 17s285ms
 󰛓 ❯ sh 8.sh
Enter a number: 12
12 is not an Armstrong number.

 kitt@kiit in ~/Documents/OS-LAB/LAB7
 󰛓 ❯ sh 8.sh
Enter a number: 153
153 is an Armstrong number.

```

---

9.

```bash
read -p "Enter a number: " n
original=$n
rev=0

while [ $n -gt 0 ]; do
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

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 15s607ms
 󰛓 ❯ sh 9.sh
Enter a number: 12
12 is not a Palindrome.

 kitt@kiit in ~/Documents/OS-LAB/LAB7
 󰛓 ❯ sh 9.sh
Enter a number: 121
121 is a Palindrome.
```

---
10.

```bash
read -p "Enter number of terms: " n
a=0
b=1
echo -n "Fibonacci Series: "
for (( i=0; i<n; i++ ))
do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done
echo ""
```

```text
 kitt@kiit in ~/Documents/OS-LAB/LAB7 took 21s980ms
 󰛓 ❯ sh 10.sh
Enter number of terms: 6
Fibonacci Series: 0 1 1 2 3 5
```