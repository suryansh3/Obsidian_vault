
### 1.

```bash

echo "Enter two numbers:"
read a
read b
if [ $a -gt $b ]; then
echo "$a is largest"
else
echo "$b is largest"
fi
```

**Output**

```
Enter two numbers:
45
89
89 is largest
```

### 2.

```bash

echo "Enter three numbers:"
read a
read b
read c
if [ $a -le $b ] && [ $a -le $c ]; then
echo "$a is smallest"
elif [ $b -le $a ] && [ $b -le $c ]; then
echo "$b is smallest"
else
echo "$c is smallest"
fi
```

**Output**

```
Enter three numbers:
12
5
20
5 is smallest
```
### 3. 
```bash

echo "Enter a number:"
read n
if [ $n -gt 0 ]; then
echo "Positive"
elif [ $n -lt 0 ]; then
echo "Negative"
else
echo "Zero"
fi
```

**Output**

```
Enter a number:
-10
Negative
```

### 4. 
```bash
echo "Enter a number:"
read n
if [ $((n%2)) -eq 0 ]; then
echo "Even"
else
echo "Odd"
fi
```

**Output**

```
Enter a number:
7
Odd
```
### 5. 
```bash
echo "Enter a year:"
read y
if [ $((y%400)) -eq 0 ]; then
echo "Leap Year"
elif [ $((y%100)) -eq 0 ]; then
echo "Not a Leap Year"
elif [ $((y%4)) -eq 0 ]; then
echo "Leap Year"
else
echo "Not a Leap Year"
fi
```

**Output**
```
Enter a year:
2023
Not a Leap Year
```

### 6. 

```bash

echo "Enter three numbers:"
read a
read b
read c
if [ $a -le $b ] && [ $b -le $c ]; then
echo "$b is middle"
elif [ $a -le $c ] && [ $c -le $b ]; then
echo "$c is middle"
elif [ $b -le $a ] && [ $a -le $c ]; then
echo "$a is middle"
elif [ $b -le $c ] && [ $c -le $a ]; then
echo "$c is middle"
elif [ $c -le $a ] && [ $a -le $b ]; then
echo "$a is middle"
else
echo "$b is middle"
fi
```

**Output**
```
Enter three numbers:
50
10
30
30 is middle
```

### 7. 

```bash

echo "Enter three sides:"
read s1
read s2
read s3
if [ $s1 -eq $s2 ] && [ $s2 -eq $s3 ]; then
echo "Equilateral"
elif [ $s1 -eq $s2 ] || [ $s2 -eq $s3 ] || [ $s1 -eq $s3 ]; then
echo "Isosceles"
else
echo "Scalene"
fi
```

**Output**

```
Enter three sides:
5
5
8
Isosceles
```

### 8. 

```bash

echo "Enter total marks:"
read m
if [ $m -ge 90 ] && [ $m -le 100 ]; then
echo "Grade: O"
elif [ $m -ge 80 ] && [ $m -lt 90 ]; then
echo "Grade: E"
elif [ $m -ge 70 ] && [ $m -lt 80 ]; then
echo "Grade: A"
elif [ $m -ge 60 ] && [ $m -lt 70 ]; then
echo "Grade: B"
elif [ $m -ge 50 ] && [ $m -lt 60 ]; then
echo "Grade: C"
elif [ $m -ge 40 ] && [ $m -lt 50 ]; then
echo "Grade: D"
else
echo "Grade: F"
fi
```

**Output**

```
Enter total marks:
85
Grade: E
```

### 9. 

```bash

echo "Enter two numbers and operation code (1-5):"
read a
read b
read op
if [ $op -eq 1 ]; then
echo "Sum: $((a+b))"
elif [ $op -eq 2 ]; then
echo "Difference: $((a-b))"
elif [ $op -eq 3 ]; then
echo "Product: $((a*b))"
elif [ $op -eq 4 ]; then
echo "Quotient: $(echo "scale=2; $a/$b" | bc)"
elif [ $op -eq 5 ]; then
echo "Remainder: $((a%b))"
else
echo "Invalid operation"
fi
```

**Output**

```
Enter two numbers and operation code (1-5):
20
6
5
Remainder: 2
```

### 10.

```bash

echo "Enter two 3-digit integers:"
read n1
read n2
mid1=$(( (n1/10)%10 ))
last2=$(( n2%10 ))
echo "Middle digit of first: $mid1"
echo "Last digit of second: $last2"
if [ $mid1 -gt $last2 ]; then
echo "Bigger"
elif [ $mid1 -lt $last2 ]; then
echo "Smaller"
else
echo "Equal"
fi
```

**Output**

```
Enter two 3-digit integers:
159
204
Middle digit of first: 5
Last digit of second: 4
Bigger
```