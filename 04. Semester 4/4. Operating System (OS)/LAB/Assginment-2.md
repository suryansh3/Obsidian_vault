

### 1. 

```bash

echo "Enter two integers:"
read a
read b
res=$(echo "scale=2; $a/$b" | bc)
echo "Result: $res"
```

**Output**

```
Enter two integers:
25
4
Result: 6.25
```

### 2. 


```sh

echo "Enter Centigrade temperature:"
read c
f=$(echo "scale=2; $c * 9/5 + 32" | bc)
echo "Fahrenheit: $f"
```
**Output**

```
Enter Centigrade temperature:
37
Fahrenheit: 98.60
```

### 3. 

```sh

echo "Enter Area of circle:"
read area
pi=3.14159
r=$(echo "scale=2; sqrt($area/$pi)" | bc -l)
echo "Radius: $r"
```

**Output**

```
Enter Area of circle:
50.27
Radius: 4.00
```

### 4. 

```sh
echo "Enter base and height:"
read b
read h
area=$(echo "scale=2; 0.5 * $b * $h" | bc)
echo "Area: $area"
```

**Output**

```
Enter base and height:
10
15
Area: 75.0
```

### 5. 


```sh
echo "Enter three sides:"
read a
read b
read c
s=$(echo "scale=4; ($a+$b+$c)/2" | bc)
area=$(echo "scale=2; sqrt($s*($s-$a)*($s-$b)*($s-$c))" | bc -l)
echo "Area: $area"
```

**Output**

```
Enter three sides:
3
4
5
Area: 6.00
```