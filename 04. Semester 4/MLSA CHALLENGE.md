
# DEFCON 3301 Challenge 1 - Solution Documentation

## Challenge Discovery

**Date:** January 18, 2026  
**Source:** MLSA KIIT Instagram Story  
**Challenge Name:** DEFCON 3301 Challenge 1  
**Solver:** Suryansh Mithu

---

## Initial Observations

While scrolling through Instagram stories, I came across a post from MLSA KIIT featuring what appeared to be a cryptographic challenge. The story contained strange symbols that immediately caught my attention.

### What I Saw:

```
Hello

ᛏᚱᚢᛋᛏ ᛒᛖᚷᛁᚾᛋ ᚹᛁᚦ ᚦᚩᛋᛖ ᚹᚻᚩ ᚢᛖᛋᛏᛁᚩᚾ ᚪᛋᛋᚢᛗᛈᛏᛁᚩᚾᛋ...
(and more runic text)

Good luck.

DEFCON 3301
MLSA
```

**First Thoughts:**

- These aren't standard letters or numbers
- They look like ancient symbols or runes
- The challenge mentions "DEFCON 3301" - possibly inspired by Cicada 3301
- MLSA = Microsoft Learn Student Ambassadors at KIIT

---

## Step 1: Identifying the Script

### Hypothesis Formation

The symbols appeared to be some form of runic alphabet. I needed to identify which specific runic system was being used.

### Research Process

1. **Visual Analysis:** The symbols had vertical lines with branches
2. **Google Search:** "runic alphabet symbols"
3. **Comparison:** Matched symbols against known runic systems

### Finding: Elder Futhark Runes

After comparing with different runic alphabets, I identified these as **Elder Futhark runes** - the oldest form of runic alphabets used by Germanic peoples from around 2nd to 8th centuries CE.

**Key Characteristics:**

- 24 runes in total
- Each rune represents a letter or sound
- Used by ancient Germanic tribes
- Popular in modern cryptography puzzles

---

## Step 2: Creating a Translation Key

I found an Elder Futhark translation chart online and created my reference:

| Rune | Letter | Rune | Letter | Rune | Letter |
| ---- | ------ | ---- | ------ | ---- | ------ |
| ᚠ    | F      | ᚻ    | H      | ᛏ    | T      |
| ᚢ    | U      | ᚾ    | N      | ᛒ    | B      |
| ᚦ    | TH     | ᛁ    | I      | ᛖ    | E      |
| ᚪ    | A      | ᛡ    | J      | ᛗ    | M      |
| ᚱ    | R      | ᛇ    | EI     | ᛚ    | L      |
| ᚳ    | C/K    | ᛈ    | P      | ᛝ    | NG     |
| ᚷ    | G      | ᛉ    | Z      | ᛞ    | D      |
| ᚹ    | W      | ᛋ    | S      | ᚩ    | O      |

---

## Step 3: Manual Translation Process

I began translating each line character by character:

### Line 1:

```
ᛏᚱᚢᛋᛏ ᛒᛖᚷᛁᚾᛋ ᚹᛁᚦ ᚦᚩᛋᛖ ᚹᚻᚩ ᚢᛖᛋᛏᛁᚩᚾ ᚪᛋᛋᚢᛗᛈᛏᛁᚩᚾᛋ...
```

Breaking it down:

- ᛏᚱᚢᛋᛏ = T-R-U-S-T = **TRUST**
- ᛒᛖᚷᛁᚾᛋ = B-E-G-I-N-S = **BEGINS**
- ᚹᛁᚦ = W-I-TH = **WITH**
- ᚦᚩᛋᛖ = TH-O-S-E = **THOSE**
- ᚹᚻᚩ = W-H-O = **WHO**
- ᚢᛖᛋᛏᛁᚩᚾ = Q-U-E-S-T-I-O-N = **QUESTION**

_Note: 'Q' sound is represented by combining runes_

Continuing this process for the entire first line...

### Line 2:

```
ᚦᛁᛋ ᛁᛋ ᚾᚩᛏ ᛗᛖᚪᚾᛏ ᚠᚩᚱ ᛖᚢᛖᚱᚣᚩᚾᛖ
```

- ᚦᛁᛋ = TH-I-S = **THIS**
- ᛁᛋ = I-S = **IS**
- ᚾᚩᛏ = N-O-T = **NOT**
- ᛗᛖᚪᚾᛏ = M-E-A-N-T = **MEANT**
- ᚠᚩᚱ = F-O-R = **FOR**
- ᛖᚢᛖᚱᚣᚩᚾᛖ = E-V-E-R-Y-O-N-E = **EVERYONE**

---

## Step 4: Complete Decryption

After translating all the runic text, here's the complete deciphered message:

### **DECRYPTED MESSAGE:**

**Paragraph 1:**

> "Trust begins with those who question assumptions verify before believing and persist when others withdraw"

**Paragraph 2:**

> "This is not meant for everyone"

**Paragraph 3:**

> "What follows is a test of patience reasoning and independent thought"

**Paragraph 4:**

> "Trust nothing without verification assume nothing without proof"

---

## Step 5: Message Analysis

### Thematic Elements:

1. **Critical Thinking** - Question assumptions, verify information
2. **Persistence** - Keep going when others give up
3. **Selectivity** - "Not meant for everyone" suggests this is a recruitment puzzle
4. **Skepticism** - Trust nothing without verification

### Challenge Philosophy:

The message itself is meta-commentary about how to approach puzzles:

- Don't assume the obvious answer
- Verify every step
- Think independently
- Be patient and persistent

### Connection to Cicada 3301:

This challenge clearly draws inspiration from the infamous Cicada 3301 internet puzzle mystery that began in 2012. Similar characteristics include:

- Cryptographic puzzles
- Philosophical messaging about intelligence and persistence
- Multi-layered challenges
- Recruitment-focused narrative

---

## Tools & Resources Used

1. **Identification:**
    
    - Google Image Search for runic alphabets
    - Wikipedia: Elder Futhark alphabet
2. **Translation:**
    
    - Online Elder Futhark translation charts
    - Manual character-by-character mapping
3. **Documentation:**
    
    - Text editor for organizing findings
    - Screenshot of original challenge

---

## Conclusion

This first challenge served as a filter - testing whether participants could:

- ✓ Recognize an unfamiliar writing system
- ✓ Research and identify Elder Futhark runes
- ✓ Patiently translate the entire message
- ✓ Understand the meta-message about puzzle-solving methodology

The decrypted message essentially provides the **rules of engagement** for future challenges in this series.

### Next Steps:

Based on the message "What follows is a test...", I anticipate:

- More challenges to be released by MLSA KIIT
- Increasing difficulty levels
- Possibly multi-stage puzzles requiring various skills (cryptography, steganography, programming, etc.)

---

## Reflection

**Time Taken:** Approximately 25-30 minutes  
**Difficulty Level:** Beginner to Intermediate  
**Skills Developed:**

- Pattern recognition
- Research methodology
- Ancient alphabet knowledge
- Patience and attention to detail

**Key Takeaway:** The challenge itself embodies its own message - I had to question my assumptions (What are these symbols?), verify my hypothesis (Check Elder Futhark charts), and persist through the tedious translation process.

---

_Challenge solved by: Suryansh Mithu
_Date: January 18, 2026_  
_Institution: KIIT University_  
_Event: DEFCON 3301 by MLSA KIIT_