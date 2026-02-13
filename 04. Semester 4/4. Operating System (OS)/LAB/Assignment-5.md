
### 1. 

```bash

read -p "Enter a digit (-9 to 9): " num
case $num in
    -[1-9])
        echo "The number is Negative."
        ;;
    0)
        echo "The number is Zero."
        ;;
    [1-9])
        echo "The number is Positive."
        ;;
    *)
        echo "Invalid input."
        ;;
esac
```

**Output:**

```
Enter a digit (-9 to 9): -5
The number is Negative.
```

---

### 2. 

```bash

read -p "Enter a digit (0-3): " digit
case $digit in
    0)
        echo "North"
        ;;
    1)
        echo "East"
        ;;
    2)
        echo "South"
        ;;
    3)
        echo "West"
        ;;
    *)
        echo "Invalid direction code."
        ;;
esac
```

**Output:**

```
Enter a digit (0-3): 1
East
```

---

### 7. 
```bash

read -p "Enter weekday number (0-6): " day
case $day in
    0)
        echo "Sunday"
        ;;
    1)
        echo "Monday"
        ;;
    2)
        echo "Tuesday"
        ;;
    3)
        echo "Wednesday"
        ;;
    4)
        echo "Thursday"
        ;;
    5)
        echo "Friday"
        ;;
    6)
        echo "Saturday"
        ;;
    *)
        echo "Invalid weekday number."
        ;;
esac
```

**Output:**

```
Enter weekday number (0-6): 3
Wednesday
```

---

### 8. 
```bash

read -p "Enter month number (0-11): " month
case $month in
    0) echo "Jan" ;;
    1) echo "Feb" ;;
    2) echo "March" ;;
    3) echo "Apr" ;;
    4) echo "May" ;;
    5) echo "Jun" ;;
    6) echo "Jul" ;;
    7) echo "Aug" ;;
    8) echo "Sep" ;;
    9) echo "Oct" ;;
    10) echo "Nov" ;;
    11) echo "Dec" ;;
    *) echo "Invalid month number." ;;
esac
```

**Output:**

```
Enter month number (0-11): 4
May
```

---

### 3. 

```bash

read -p "Enter a digit (0-9): " digit
case $digit in
    0|2|4|6|8)
        echo "The digit is Even."
        ;;
    1|3|5|7|9)
        echo "The digit is Odd."
        ;;
    *)
        echo "Invalid input."
        ;;
esac
```

**Output:**

```
Enter a digit (0-9): 7
The digit is Odd.
```

---

### 4. 
```bash

read -p "Enter a single character: " char
case $char in
    [a-z])
        echo "It is a Lowercase letter."
        ;;
    [A-Z])
        echo "It is an Uppercase letter."
        ;;
    [0-9])
        echo "It is a Digit."
        ;;
    *)
        echo "It is a Special Character."
        ;;
esac
```

**Output:**

```
Enter a single character: @
It is a Special Character.
```

---

### 5. 

```bash

read -p "Enter an alphabet: " char
case $char in
    [aeiou])
        echo "Lowercase Vowel"
        ;;
    [a-z])
        echo "Lowercase Consonant"
        ;;
    [AEIOU])
        echo "Uppercase Vowel"
        ;;
    [A-Z])
        echo "Uppercase Consonant"
        ;;
    *)
        echo "Not an alphabet"
        ;;
esac
```

**Output:**

```
Enter an alphabet: E
Uppercase Vowel
```

---

### 6. 

```bash

read -p "Enter first number: " a
read -p "Enter second number: " b
echo "1:Add, 2:Sub, 3:Mul, 4:Div, 5:Rem"
read -p "Enter operation choice (1-5): " op

case $op in
    1)
        echo "Result: $((a + b))"
        ;;
    2)
        echo "Result: $((a - b))"
        ;;
    3)
        echo "Result: $((a * b))"
        ;;
    4)
        result=$(echo "scale=2; $a / $b" | bc)
        echo "Result: $result"
        ;;
    5)
        echo "Result: $((a % b))"
        ;;
    *)
        echo "Invalid operation"
        ;;
esac
```

**Output:**

```
Enter first number: 10
Enter second number: 4
1:Add, 2:Sub, 3:Mul, 4:Div, 5:Rem
Enter operation choice (1-5): 4
Result: 2.50
```

---

### 9. 

```bash

digit=$((RANDOM % 10))
echo "Generated Digit: $digit"
case $digit in
    0|1|2|3|4)
        echo "Result: Head"
        ;;
    5|6|7|8|9)
        echo "Result: Tail"
        ;;
esac
```

**Output:**

```
Generated Digit: 3
Result: Head
```

---

### 10. 

```bash

char=$(tr -dc 'a-zA-Z' < /dev/urandom | head -c 1)
echo "Generated Letter: $char"

case $char in
    [a-dA-D])
        echo "Dice Roll: 1"
        ;;
    [e-hE-H])
        echo "Dice Roll: 2"
        ;;
    [i-lI-L])
        echo "Dice Roll: 3"
        ;;
    [m-pM-P])
        echo "Dice Roll: 4"
        ;;
    [q-tQ-T])
        echo "Dice Roll: 5"
        ;;
    [u-zU-Z])
        echo "Dice Roll: 6"
        ;;
esac
```

**Output:**

```
Generated Letter: k
Dice Roll: 3
```