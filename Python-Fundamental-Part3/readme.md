<!-- ---------- PREMIUM GRAPHIC BANNER ---------- -->
<p align="center">
  <img src="https://img.shields.io/badge/Python%20Fundamentals%20(Part--3)-8A2BE2?style=for-the-badge&logo=python&logoColor=yellow" />
</p>

<h1 align="center">🐍 Python Fundamentals — Part 3
<br> <span style="font-size:16px;">Strings • Lists • Tuples • Dictionaries • Sets</span></h1>

<p align="center">
  <b>Ultra-Premium Notes + Full Assignment from Provided PDFs</b>
</p>

---

# 🎛️ **Table of Contents**
- [🔡 Strings](#-1-strings)
- [🧵 String Indexing & Slicing](#-2-string-indexing--slicing)
- [🎨 String Formatting](#-3-string-formatting)
- [📦 Lists](#-4-lists)
- [✂️ List Slicing & Methods](#-5-list-slicing--methods)
- [🔍 Linear Search & Loops](#-6-loops--linear-search)
- [🧊 Tuples](#-7-tuples)
- [🧮 Tuple Methods](#-8-tuple-methods)
- [🗂 Dictionaries](#-9-dictionary)
- [🧰 Dictionary Methods](#-10-dictionary-methods)
- [🔁 Dictionary Looping](#-11-looping-dictionaries)
- [🌀 Sets](#-12-sets)
- [⚙️ Set Methods](#-13-set-methods)
- [📝 Assignment-3](#assignment-3)
- [✨ Author](#author)

---

# 🔡 **1. Strings**
> 📄 *From PDF Page 1*

A string is a sequence of characters enclosed in quotes.

```python title="Creating Strings"
s1 = "hello world"
s2 = 'Python'
```

### 🧠 Key Notes
- Strings are **immutable**
- Use `len()` to get length

```python
len("Prime")   # 5
```

---

# 🧵 **2. String Indexing & Slicing**
> 📄 *From PDF Page 2*

Python uses **0-based indexing**

```python
s = "python"
s[0]    # p
s[-1]   # n
```

### 📌 Slicing
```
string[start : end : step]
```

```python title="Examples"
s = "python"
print(s[1:4])    # yth
print(s[::-1])   # reverse
print(s[::2])    # pto
```

---

# 🎨 **3. String Formatting**
> 📄 *From PDF Page 2–3*

### ✔ Using `.format()`
```python
name = "Rahul"
age = 25
f = "My name is {} and I am {} years old".format(name, age)
```

### ✔ Using f-strings (BEST)
```python
f = f"My name is {name} and I am {age} years old"
```

---

# 📦 **4. Lists**
> 📄 *From PDF Page 3–4*

Lists are **ordered**, **mutable**, allow **duplicates**, and **heterogeneous**.

```python
my_list = [1, 2, 3, 4]
mix = [10, "Hello", 3.14, True]
```

---

# ✂️ **5. List Slicing & Methods**
> 📄 *From PDF Page 4–5*

```python title="Slicing Lists"
nums = [0,1,2,3,4,5,6]
print(nums[2:5])    # [2,3,4]
print(nums[::-1])   # reverse
```

### ⭐ Important Methods
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`

---

# 🔍 **6. Loops & Linear Search**
> 📄 *From PDF Page 6*

### Looping on List
```python
for num in [10, 20, 30]:
    print(num)
```

### Linear Search
```python
x = 7
for num in [5, 12, 7, 3]:
    if num == x:
        print("Found:", x)
```

---

# 🧊 **7. Tuples**
> 📄 *From PDF Page 6–7*

Tuples are like lists but **immutable**.

```python
t = (10, 20, 30)
t[1]    # 20
```

### Characteristics
- Ordered
- Immutable
- Allows duplicates
- Heterogeneous

---

# 🧮 **8. Tuple Methods**
> 📄 *From PDF Page 7*

```python
t = (5, 12, 25)
t.index(12)
t.count(5)
```

---

# 🗂 **9. Dictionaries**
> 📄 *From PDF Page 8*

Dictionary = **key-value pairs**

```python title="Dictionary Example"
student = {
  "name": "Bob",
  "age": 20
}
```

### Key Notes
- Keys must be **unique**
- Mutable
- Values can be any type

---

# 🧰 **10. Dictionary Methods**
> 📄 *From PDF Page 8*

- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`
- `pop()`

---

# 🔁 **11. Looping Dictionaries**
> 📄 *From PDF Page 9*

```python
for key, value in student.items():
    print(key, value)
```

---

# 🌀 **12. Sets**
> 📄 *From PDF Page 9*

```python
s = {1,2,2,3}
# output: {1,2,3}
```

### Characteristics
- Unique elements
- Unordered
- No indexing or slicing

---

# ⚙️ **13. Set Methods**
> 📄 *From PDF Page 10*

```python
s.add(40)
s.remove(20)
s.clear()
```

### Union & Intersection
```python
a = {1,2,3}
b = {2,3,4}

a.union(b)
a.intersection(b)
```

---

# 📝 **Assignment-3**
> 📄 *From Assignment PDF (All Questions Included)*

Below are the assignment questions exactly from the PDF:

---

## **🟪 Q1 — Create a string & print its length**

---

## **🟪 Q2 — Count occurrences of a character in a string**

---

## **🟪 Q3 — Check if a string is palindrome**

---

## **🟪 Q4 — Perform: append, insert, remove, pop on list**

---

## **🟪 Q5 — Linear search on list**

---

## **🟪 Q6 — Count occurrences of a number in a list**

---

## **🟪 Q7 — Find index of value in tuple**

---

## **🟪 Q8 — Print all keys & values of dictionary**

---

## **🟪 Q9 — Add subject inside student dictionary list**

---

## **🟪 Q10 — Union & Intersection of two sets**

---

# ✨ **Author**
### 👤 Suraj Kumar
MERN Stack Developer | Python Learner
📍 India

<p align="center">Made with ❤️ by Suraj</p>

