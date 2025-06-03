# Python f-strings Tutorial

## Introduction

f-strings (formatted string literals) were introduced in Python 3.6. They provide a concise and efficient way to embed Python expressions inside string literals, using curly braces `{}`.

---

## Basic Syntax

To create an f-string, prefix the string with the letter `f` or `F`:

```python
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # Output: Hello, Alice!

Embedding Expressions
You can embed any valid Python expression inside {}:
a = 10
b = 5
result = f"Sum: {a + b}, Product: {a * b}"
print(result)  # Output: Sum: 15, Product: 50

Using Functions and Methods
You can call functions or methods directly inside f-strings:
def greet(name):
    return f"Hi, {name.title()}!"

print(f"{greet('bob')}")  # Output: Hi, Bob!


Formatting Numbers
f-strings support the same formatting options as the str.format() method:
pi = 3.14159265
print(f"Pi rounded to 2 decimals: {pi:.2f}")  # Output: Pi rounded to 2 decimals: 3.14

Using f-strings with Dates and Times
from datetime import datetime
now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}")  # Output: Current date: 2025-06-03

Nested f-strings
adj = "awesome"
print(f"{f'This is {adj}'}")  # Output: This is awesome

Multi-line f-strings
You can use f-strings with triple quotes for multi-line strings:
x, y = 5, 10
print(f"""
Coordinates:
    x = {x}
    y = {y}
""")
