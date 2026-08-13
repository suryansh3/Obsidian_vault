
### 1. Complex Operation (a o1 b) o2 (c o3 d)

```bash

echo "Enter 4 operands (a b c d):"
read a
read b
read c
read d
echo "Enter 3 operators (o1 o2 o3):"
read o1
read o2
read o3
res1=$(($a $o1 $b))
res2=$(($c $o3 $d))
final=$(($res1 $o2 $res2))
echo "Result: $final"
```

**Output**

```
Enter 4 operands (a b c d):
10
5
2
3
Enter 3 operators (o1 o2 o3):
+
*
-
Result: -15
```

### 2. Swap Using Third Variable

```bash

echo "Enter two numbers:"
read a
read b
echo "Before Swap: a=$a, b=$b"
temp=$a
a=$b
b=$temp
echo "After Swap: a=$a, b=$b"
```

**Output**
```bash
Enter two numbers:
5
9
Before Swap: a=5, b=9
After Swap: a=9, b=5
```

### 3. Swap Without Third Variable

```bash

echo "Enter two numbers:"
read a
read b
echo "Before Swap: a=$a, b=$b"
a=$((a+b))
b=$((a-b))
a=$((a-b))
echo "After Swap: a=$a, b=$b"
```

**Output**
```
Enter two numbers:
10
20
Before Swap: a=10, b=20
After Swap: a=20, b=10
```

### 4. Average and Percentage Calculation

```bash

echo "Enter marks for 5 subjects:"
read m1
read m2
read m3
read m4
read m5
sum=$((m1+m2+m3+m4+m5))
avg=$(echo "scale=2; $sum/5" | bc)
percent=$(echo "scale=2; $sum/10" | bc)
echo "Average: $avg"
echo "Percentage: $percent%"
```

**Output**
```
Enter marks for 5 subjects:
150
160
140
180
170
Average: 160.00
Percentage: 80.00%
```

### 5. Paisa to Rupee and Paisa

```bash

echo "Enter amount in Paisa:"
read p
rupee=$((p/100))
paisa=$((p%100))
echo "$rupee Rupee and $paisa Paisa"
```

**Output**

```
Enter amount in Paisa:
1250
12 Rupee and 50 Paisa
```

### 6. Seconds to HH:MM:SS

```bash

echo "Enter seconds:"
read s
h=$((s/3600))
rem=$((s%3600))
m=$((rem/60))
sec=$((rem%60))
echo "$h:$m:$sec"
```

**Output**

```
Enter seconds:
3665
1:1:5
```

### 7. Meter to Kilometer and Meter


```bash

echo "Enter distance in meters:"
read dist
km=$((dist/1000))
m=$((dist%1000))
echo "$km KM and $m meters"
```

**Output**

```
Enter distance in meters:
2500
2 KM and 500 meters
```

### 8. Sum of First and Last Digit (6-digit number)

```bash

echo "Enter a six-digit number:"
read n
first=$((n/100000))
last=$((n%10))
sum=$((first+last))
echo "Sum of first and last digit: $sum"
```

**Output**

```
Enter a six-digit number:
123456
Sum of first and last digit: 7
```

### 9. Sum of All Digits (3-digit number)

```bash

echo "Enter a three-digit number:"
read n
d1=$((n%10))
n=$((n/10))
d2=$((n%10))
n=$((n/10))
d3=$((n))
sum=$((d1+d2+d3))
echo "Sum of digits: $sum"
```

**Output**

```
Enter a three-digit number:
456
Sum of digits: 15
```

### 10. Reverse a 3-digit Number

```bash

echo "Enter a three-digit number:"
read n
d1=$((n%10))
n=$((n/10))
d2=$((n%10))
n=$((n/10))
d3=$((n))
rev=$((d1*100 + d2*10 + d3))
echo "Reversed Number: $rev"
```

**Output**

```
Enter a three-digit number:
789
Reversed Number: 987
```