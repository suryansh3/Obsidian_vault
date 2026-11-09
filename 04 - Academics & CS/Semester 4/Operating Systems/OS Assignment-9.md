---
course: "Operating Systems"
semester: 4
tags:
  - course/operating-systems
up: "[[Operating Systems]]"
---
## 1.

```bash
read -p "Enter number of elements (N): " n
for ((i=0; i<n; i++)); do
    read -p "Element $((i+1)): " arr[$i]
done
echo "Array contents: [${arr[*]}]"
```

**Output:**

```
Enter number of elements (N): 3
Element 1: 45
Element 2: 12
Element 3: 89
Array contents: [45 12 89]
```

---
## 2. 


```bash
read -p "Enter N: " n
sum=0
for ((i=0; i<n; i++)); do
    read -p "Enter number: " val
    arr[$i]=$val
    sum=$((sum + val))
done
echo "The total sum is: $sum"
```

**Output:**

```
Enter N: 4
Enter number: 10
Enter number: 20
Enter number: 5
Enter number: 15
The total sum is: 50
```

---

## 3.

```bash
read -p "Enter total numbers: " n
sum=0
for ((i=0; i<n; i++)); do
    read -p "Num $((i+1)): " num
    sum=$((sum + num))
done
avg=$(echo "scale=2; $sum / $n" | bc)
echo "The average is: $avg"
```

**Output:**

```
Enter total numbers: 3
Num 1: 10
Num 2: 15
Num 3: 12
The average is: 12.33
```

---

## 4.

```bash
#!/bin/bash
read -p "How many numbers? " n
for ((i=0; i<n; i++)); do read -p "> " arr[$i]; done

max=${arr[0]}
for i in "${arr[@]}"; do
    [[ $i -gt $max ]] && max=$i
done
echo "Largest number is: $max"
```

**Output:**

```
How many numbers? 5
> 12
> 99
> 45
> 102
> 3
Largest number is: 102
```

---

## 5.


```bash
#!/bin/bash
arr=(10 25 30 45 50)
echo "Array: ${arr[*]}"
read -p "Enter element to find: " key
found=0
for i in "${!arr[@]}"; do
    if [[ ${arr[$i]} -eq $key ]]; then
        echo "Found $key at index $i"
        found=1; break
    fi
done
[[ $found -eq 0 ]] && echo "Element not in array."
```

**Output:**

```
Array: 10 25 30 45 50
Enter element to find: 30
Found 30 at index 2
```

---

## 6.

```bash
#!/bin/bash
read -p "Enter N: " n
prod=1
for ((i=0; i<n; i++)); do
    read -p "Enter value: " v
    prod=$((prod * v))
done
echo "The product is: $prod"
```

**Output:**

```
Enter N: 3
Enter value: 2
Enter value: 5
Enter value: 4
The product is: 40
```

---
## 7.


```bash
#!/bin/bash
arr=(12 45 2 99 99 78) # Sample with duplicates
max=-99999; sec=-99999
for i in "${arr[@]}"; do
    if ((i > max)); then
        sec=$max; max=$i
    elif ((i > sec && i != max)); then
        sec=$i
    fi
done
echo "Array: ${arr[*]}"
echo "Second Largest: $sec"
```

**Output:**


```
Array: 12 45 2 99 99 78
Second Largest: 78
```

---

## 8.


```bash
#!/bin/bash
arr=(5 1 4 2 8)
n=${#arr[@]}
for ((i=0; i<n; i++)); do
    for ((j=0; j<n-i-1; j++)); do
        if ((arr[j] > arr[j+1])); then
            t=${arr[j]}; arr[j]=${arr[j+1]}; arr[j+1]=$t
        fi
    done
done
echo "Sorted Array: ${arr[*]}"
```

**Output:**

```
Sorted Array: 1 2 4 5 8
```

---

## 9.

```bash
#!/bin/bash
read -a arr -p "Enter numbers separated by space: "
evens=""; odds=""
for i in "${arr[@]}"; do
    ((i % 2 == 0)) && evens="$evens $i" || odds="$odds $i"
done
echo "Evens: $evens"
echo "Odds: $odds"
```

**Output:**

```
Enter numbers separated by space: 1 2 3 4 5 6
Evens:  2 4 6
Odds:  1 3 5
```

---
## 10.

```bash
#!/bin/bash
arr=(Alpha Beta Gamma Delta)
echo "Original: ${arr[*]}"
rev=()
for ((i=${#arr[@]}-1; i>=0; i--)); do
    rev+=("${arr[i]}")
done
echo "Reversed: ${rev[*]}"
```

**Output:**

```
Original: Alpha Beta Gamma Delta
Reversed: Delta Gamma Beta Alpha
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Operating Systems]] · **Semester:** [[Semester 4]] · **Map:** [[MOC]]
> **Prev:** - · **Next:** -
> **Related:** [[OOPJ (Java)]] · [[COA]] · [[CN]]
<!-- connections:end -->
