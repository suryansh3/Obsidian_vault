### 1. 

```bash
echo "Random Integer (1-100)"
echo "Result: $(( (RANDOM % 100) + 1 ))"
```

**Output**

```
Random Integer (1-100)
Result: 54
```

---

### 2. 
```bash
echo "Random Integer (min to max)"
read -p "Enter min: " min
read -p "Enter max: " max
if [ $min -lt $max ]; then
res=$(( (RANDOM % (max - min + 1)) + min ))
echo "Random number between $min and $max: $res"
else
echo "Error: min must be less than max."
fi
```

**Output**
```
Random Integer (min to max)
Enter min: 12
Enter max: 29
Random number between 12 and 29: 25
```

---

### 3.
```bash
echo "Random Float (0 to 1)"
echo "Result $(echo "scale=4; $RANDOM / 32767" | bc)"
```

**Output**

```
Random Float (0 to 1)
Result .0292
```

---
### 4.

```bash
echo "Random Float (min to max)"
read -p "Enter min: " fmin
read -p "Enter max: " fmax
if (( $(echo "$fmin < $fmax" | bc -l) )); then
diff=$(echo "$fmax - $fmin" | bc)
rand_val=$(echo "scale=4; $fmin + (($RANDOM / 32767) * $diff)" | bc)
echo "Result: $rand_val"
else
echo "Error: min must be less than max."
fi
```

**Output**

```
Random Float (min to max)
Enter min: 12
Enter max: 33
Result: 21.6600
```

---

### 5. 

```bash
echo "Arithmetic Operations"
a=$(( (RANDOM % 50) + 1 ))
b=$(( (RANDOM % 10) + 1 ))
echo "a=$a, b=$b"
echo "Addition: $a+$b=$((a+b))"
echo "Subtraction: $a-$b=$((a-b))"
echo "Multiplication: $a*$b=$((a*b))"
echo "Division: $a / $b=$(echo "scale=2; $a / $b" | bc)"
echo "Remainder: $a % $b=$((a%b))"
echo "Exponent: $a^$b=$((a**b))"
```

**Output**

```
Arithmetic Operations
a=36, b=8
Addition: 36+8=44
Subtraction: 36-8=28
Multiplication: 36*8=288
Division: 36 / 8=4.50
Remainder: 36 % 8=4
Exponent: 36^8=2821109907456
```

---
### 6.

```bash
echo "Coin Toss (5 times)"
for i in {1..5}; do
toss=$((RANDOM % 2))
if [ $toss -eq 0 ]; then 
echo "Toss $i: Heads" 
else 
echo "Toss $i: Tails" 
fi
done
```

**Output**

```
Coin Toss (5 times)
Toss 1: Heads
Toss 2: Heads
Toss 3: Heads
Toss 4: Heads
Toss 5: Tails
```

---

### 7. 

```bash
echo "D6 Dice Roll (5 times)"
for i in {1..5}; do
echo "Roll $i: $(( (RANDOM % 6) + 1 ))"
done
```

**Output**

```
D6 Dice Roll (5 times)
Roll 1: 3
Roll 2: 5
Roll 3: 2
Roll 4: 2
Roll 5: 3
```

---

### 8. 
```bash
echo "Rock, Paper, Scissor"
choices=("ROCK" "PAPER" "SCISSOR")
p=$((RANDOM % 3))
c=$((RANDOM % 3))
echo "Player: ${choices[$p]} vs Computer: ${choices[$c]}"
if [ $p -eq $c ]; then
echo "Result: It's a tie!"
elif [[ ($p -eq 0 && $c -eq 2) || ($p -eq 1 && $c -eq 0) || ($p -eq 2 && $c -eq 1) ]]; then
echo "Result: Player Wins!"
else
echo "Result: Computer Wins!"
fi
```

**Output**

```
Rock, Paper, Scissor
Player: SCISSOR vs Computer: PAPER
Result: Player Wins!
```

---

### 9. Simulation: Simplified DnD Round

```bash
echo "DnD Simplified Round"
P_H_D20=$(( (RANDOM % 20) + 1 ))
M_D_D20=$(( (RANDOM % 20) + 1 ))
echo "Player rolls Hit Chance (D20): $P_H_D20"
echo "Monster rolls Dodge Chance (D20): $M_D_D20"
if [ $M_D_D20 -gt $P_H_D20 ]
then
echo "Outcome: Monster dodged the hit! MONSTER WINS."
else
echo "Hit lands! Proceeding to damage phase..."
P_A_D10=$(( (RANDOM % 10) + 1 ))
M_B_D10=$(( (RANDOM % 10) + 1 ))
echo "Player rolls Attack (D10): $P_A_D10"
echo "Monster rolls Block (D10): $M_B_D10"
if [ $M_B_D10 -gt $P_A_D10 ]; then
echo "Outcome: Monster blocked the attack! MONSTER WINS."
else
echo "Outcome: Player breaks through the block! PLAYER WINS."
fi
fi
```

**Output**

```
DnD Simplified Round
Player rolls Hit Chance (D20): 18
Monster rolls Dodge Chance (D20): 12
Hit lands! Proceeding to damage phase...
Player rolls Attack (D10): 9
Monster rolls Block (D10): 9
Outcome: Player breaks through the block! PLAYER WINS.
```