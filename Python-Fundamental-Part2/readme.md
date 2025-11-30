<!-- ---------- BANNER ---------- -->
<p align="center">
  <img src="https://img.shields.io/badge/Python_Fundamentals_Part_2-blue?style=for-the-badge&logo=python" />
</p>


<h1 align="center">🐍 Python Fundamentals (Part-2) — Conditionals, Loops & Functions</h1>

<p align="center">
  <b>Complete Notes + Full Assignment (From Provided PDF)</b><br/>
  <i>Concepts: Conditionals • Logical Ops • Loops • Range • Break/Continue • Functions • Lambda</i>
</p>

---

# 📚 **Table of Contents**

### ⭐ NOTES (From PDF)
1. [Conditional Statements](#1-conditional-statements)
2. [Logical Operators](#2-logical-operators)
3. [Nesting in Conditionals](#3-nesting-in-conditionals)
4. [Ternary Operator](#4-ternary-operator)
5. [Match–Case](#5-match-case)
6. [Loops (while & for)](#6-loops)
7. [Infinite Loops](#7-infinite-loops)
8. [Break & Continue](#8-break--continue)
9. [for Loop & Membership Operator](#9-for-loop--membership)
10. [Nested Loops](#10-nested-loops)
11. [range() Function](#11-range-function)
12. [Functions](#12-functions)
13. [Functions with Parameters](#13-functions-with-parameters)
14. [Return Keyword](#14-return-keyword)
15. [Default Parameters](#15-default-parameters)
16. [Built-In Functions](#16-built-in-functions)
17. [Lambda Functions](#17-lambda-functions)

### 📝 ASSIGNMENT-2 (From Provided PDF)
18. [Assignment-2 Problems](#assignment-2-problems)

---

# 🧠 **1. Conditional Statements**
(PDF: Part-2 Page 1)
Python me decisions lene ke liye conditional statements use hoti hain.

### ✔ Types:
- `if`
- `else`
- `elif` (multiple conditions)

Example:
```python
age = int(input("Enter age: "))

if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")
```

---

# 🔍 **2. Logical Operators**
Use inside conditions:
`and`, `or`, `not`
(PDF: Page-2)

Example:
```python
age = int(input())
if age < 13:
    print("Child")
elif age > 13 and age < 18:
    print("Teenager")
else:
    print("Adult")
```

---

# 🏗️ **3. Nesting in Conditionals**
(PDF Page-2)
Condition ke andar condition.

Example:
```python
username = input("username: ")
password = input("password: ")

if username == "admin":
    if password == "1234":
        print("Welcome")
    else:
        print("Wrong password")
else:
    print("Invalid user")
```

---

# ⚡ **4. Ternary Operator**
(PDF Page-2)
```python
status = "Adult" if age >= 18 else "Not Adult"
```

---

# 🎯 **5. Match-Case (Python 3.10+)**
(PDF Page-3)
```python
color = input("Enter color: ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Color")
```

---

# 🔁 **6. Loops**
(PDF Page-4)

### ✔ Two types:
- `while`
- `for`

### Example:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

# 🛑 **7. Infinite Loops**
(PDF Page-4)
```python
while True:
    print("Prime")
```

---

# ⛔ **8. break & continue**
(PDF Page-5)

### break example:
```python
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
```

### continue example:
```python
i = 1
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)
```

---

# 🔄 **9. for Loop & Membership Operator**
(PDF Page-6)

```python
word = "Prime"
for ch in word:
    if ch == "i":
        print("i is present")
```

---

# 🔀 **10. Nested Loops**
(PDF Page-6)

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# 🎚️ **11. range() Function**
(PDF Page-7)

Syntax:
`range(start, stop, step)`

```python
for i in range(1, 6):
    print(i)
```

---

# 🧩 **12. Functions (def)**
(PDF Page-8)

```python
def hello():
    print("Hello from Python")

hello()
```

---

# 📥 **13. Functions with Parameters**
(PDF Page-8)

```python
def sum(a, b):
    print(a + b)
```

---

# 🔙 **14. return Keyword**
(PDF Page-8)

```python
def avg(a, b, c):
    return (a + b + c) / 3
```

---

# 🎛️ **15. Default Parameters**
(PDF Page-8)

```python
def hello(name="Suraj"):
    print("Hello", name)
```

---

# 🏗️ **16. Built-In Functions**
(PDF Page-9)

- `print()`
- `input()`
- `type()`
- `len()`
- `range()`

---

# ⚡ **17. Lambda Functions**
(PDF Page-9)

```python
square = lambda x : x * x
print(square(5))
```

---

# 📝 **ASSIGNMENT-2 Problems (Direct from PDF)**
(PDF: Assignment-2 Page 1-2)

### **Q1. Salary Input → Tax Rate**
Rules:
- `< 30,000` → 5%
- `30k–70k` → 15%
- `> 70k` → 25%

---

### **Q2. Function to print all even numbers between a & b**

---

### **Q3. Function to print digits of a number (312 → 3,1,2)**

---

### **Q4. Count digits of a number**

---

### **Q5. Sum of digits of a number**

---

### **Q6. Numbers from 1-100 divisible by both 3 and 5**

---

### **Q7. Infinite input loop → tell positive / negative until user enters Quit**

---

### **Q8. Create a Simple Calculator function ( + , - , * , / )**

---

### **Q9. Function is_prime(n) using loops**
Rules from PDF:
- Only prime for 2 or numbers >2
- Divide check range → `2 to n-1`

---

### **Q10. Number Guessing Game**
Output:
- “Too high”
- “Too low”
- “Correct”

---

# ✨ Author

### 👤 **Suraj Kumar**
🔥 MERN Stack Developer | Python Learner
📍 India
📫 Email: kumarsurajverma6001@gmail.com
💻 GitHub: [*your GitHub link here*](https://github.com/SurajVerma8825/Python-Practice)

---

<p align="center">
  ⭐ If this README helped you, give a star on GitHub! ⭐
</p>

