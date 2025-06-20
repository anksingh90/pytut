# Conditional and Looping Constructs in Python

## 5.1 Introduction

Conditional and looping constructs are fundamental programming concepts that allow you to control the flow of your program. They enable your code to make decisions and repeat actions based on certain conditions.

**Conditional constructs** allow your program to execute different blocks of code based on whether certain conditions are true or false. **Looping constructs** allow your program to repeat a block of code multiple times, either for a specified number of iterations or while a condition remains true.

These constructs are essential for creating dynamic, interactive programs that can respond to different inputs and situations.

## 5.2 Types of Statements in Python

Python has several types of statements that control program execution:

### Sequential Statements
These are statements that execute one after another in order:
```python
print("First statement")
print("Second statement")
print("Third statement")
```

### Conditional Statements
These statements execute based on conditions:
- `if` statement
- `if-else` statement
- `if-elif-else` statement

### Looping Statements
These statements repeat code blocks:
- `for` loop
- `while` loop

### Jump Statements
These statements alter the normal flow of execution:
- `break` statement
- `continue` statement
- `pass` statement

## 5.3 Program Control and Flow

Program control refers to the order in which statements are executed in a program. By default, Python executes statements sequentially from top to bottom. However, control flow statements allow you to:

- **Branch**: Execute different code paths based on conditions
- **Loop**: Repeat code blocks multiple times
- **Jump**: Skip or exit from loops and functions

```python
# Sequential flow
x = 10
y = 20
z = x + y
print(z)

# Conditional flow
if z > 25:
    print("z is greater than 25")
else:
    print("z is not greater than 25")

# Looping flow
for i in range(3):
    print(f"Iteration {i}")
```

## 5.4 Use of Indentation

Python uses indentation to define code blocks instead of curly braces `{}` like other languages. This makes Python code more readable and enforces good coding practices.

### Rules for Indentation:
1. Use 4 spaces per indentation level (recommended)
2. Be consistent throughout your code
3. All statements at the same level must have the same indentation
4. Nested blocks must be indented further than their parent blocks

```python
# Correct indentation
if True:
    print("This is indented")
    if True:
        print("This is further indented")
    print("Back to first level")

# Incorrect indentation (will cause IndentationError)
# if True:
# print("This will cause an error")
```

## 5.5 Conditional Constructs/Statements

### 5.5.1 if Statement

The `if` statement is the most basic conditional statement. It executes a block of code only if a specified condition is true.

**Syntax:**
```python
if condition:
    # code to execute if condition is True
    statement1
    statement2
```

**Examples:**
```python
# Basic if statement
age = 18
if age >= 18:
    print("You are eligible to vote")

# if statement with multiple conditions
temperature = 25
if temperature > 30:
    print("It's hot outside")

# if statement with logical operators
username = "admin"
password = "123456"
if username == "admin" and password == "123456":
    print("Login successful")
```

### 5.5.2 if-else Statement

The `if-else` statement provides an alternative block of code to execute when the condition is false.

**Syntax:**
```python
if condition:
    # code to execute if condition is True
    statement1
else:
    # code to execute if condition is False
    statement2
```

**Examples:**
```python
# Basic if-else
number = 15
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# if-else with user input
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# if-else with string comparison
weather = "sunny"
if weather == "rainy":
    print("Take an umbrella")
else:
    print("Enjoy the weather")
```

### 5.5.3 if-elif-else Statement

The `if-elif-else` statement allows you to check multiple conditions in sequence.

**Syntax:**
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
elif condition3:
    # code for condition3
else:
    # code if none of the conditions are true
```

**Examples:**
```python
# Grade calculator
marks = 85
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Traffic light system
light = "yellow"
if light == "green":
    print("Go")
elif light == "yellow":
    print("Caution")
elif light == "red":
    print("Stop")
else:
    print("Invalid light color")
```

### 5.5.4 Nested if-elif-else Statement

You can nest conditional statements inside other conditional statements to handle complex decision-making scenarios.

**Examples:**
```python
# Nested if statements
age = 25
income = 50000

if age >= 18:
    print("You are an adult")
    if income >= 30000:
        print("You are eligible for a loan")
        if income >= 50000:
            print("You qualify for a premium loan")
        else:
            print("You qualify for a standard loan")
    else:
        print("Your income is too low for a loan")
else:
    print("You must be 18 or older")

# Complex nested example
weather = "sunny"
temperature = 25

if weather == "sunny":
    if temperature > 30:
        print("Perfect beach weather!")
    elif temperature > 20:
        print("Great weather for outdoor activities")
    else:
        print("Sunny but a bit cool")
elif weather == "rainy":
    if temperature > 15:
        print("Warm rain, might be pleasant")
    else:
        print("Cold and rainy, stay inside")
else:
    print("Check the weather forecast")
```

## 5.6 Iteration

Iteration allows you to repeat a block of code multiple times. Python provides two main types of loops:

### 5.6.1 for Loop

The `for` loop is used to iterate over a sequence (like a list, tuple, string, or range).

**Syntax:**
```python
for variable in sequence:
    # code to execute for each item
    statement1
    statement2
```

**Examples:**
```python
# Iterating over a range
for i in range(5):
    print(f"Count: {i}")

# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating over a string
word = "Python"
for letter in word:
    print(letter)

# Using range with start, stop, and step
for i in range(2, 10, 2):
    print(f"Even number: {i}")

# Iterating over a dictionary
student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
```

### 5.6.2 while Loop

The `while` loop continues to execute as long as a specified condition is true.

**Syntax:**
```python
while condition:
    # code to execute while condition is True
    statement1
    statement2
```

**Examples:**
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# while loop with user input
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password != "secret":
        print("Wrong password, try again")
print("Access granted!")

# while loop with break condition
number = 1
while True:
    if number > 10:
        break
    print(number)
    number += 1
```

## 5.7 Nested Loops

Nested loops are loops inside other loops. The inner loop completes all its iterations for each iteration of the outer loop.

**Examples:**
```python
# Nested for loops
for i in range(3):
    print(f"Outer loop iteration: {i}")
    for j in range(2):
        print(f"  Inner loop iteration: {j}")

# Multiplication table using nested loops
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each table

# Pattern printing with nested loops
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line after each row

# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
```

## 5.8 Jump Statements

Jump statements are used to alter the normal flow of execution in loops.

### 5.8.1 break Statement

The `break` statement immediately exits the current loop.

**Examples:**
```python
# break in for loop
for i in range(10):
    if i == 5:
        break
    print(i)
print("Loop ended")

# break in while loop
count = 0
while True:
    if count == 3:
        break
    print(f"Count: {count}")
    count += 1

# break in nested loops (only breaks inner loop)
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i = {i}, j = {j}")
```

### 5.8.2 continue Statement

The `continue` statement skips the rest of the current iteration and moves to the next iteration.

**Examples:**
```python
# continue in for loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

# continue in while loop
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:
        continue
    print(count)

# continue with nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"i = {i}, j = {j}")
```

### 5.8.3 pass Statement

The `pass` statement is a null operation - it does nothing when executed. It's used as a placeholder.

**Examples:**
```python
# pass in if statement
x = 10
if x > 5:
    pass  # TODO: implement this later
else:
    print("x is not greater than 5")

# pass in loop
for i in range(5):
    if i == 2:
        pass  # placeholder for future code
    else:
        print(i)

# pass in function definition
def future_function():
    pass  # will implement later

# pass in class definition
class MyClass:
    pass  # will add methods later
```

## Programming Exercises

### Exercise 1: Basic Conditionals
Write a program that takes a number as input and determines if it's positive, negative, or zero.

```python
# Solution
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

### Exercise 2: Grade Calculator
Create a program that calculates letter grades based on numerical scores:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

```python
# Solution
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Exercise 3: Factorial Calculator
Write a program to calculate the factorial of a number using a while loop.

```python
# Solution
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} is {factorial}")
```

### Exercise 4: Prime Number Checker
Create a program that checks if a given number is prime.

```python
# Solution
num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
```

### Exercise 5: Multiplication Table
Write a program that prints the multiplication table for a given number.

```python
# Solution
num = int(input("Enter a number: "))
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
```

### Exercise 6: Number Guessing Game
Create a number guessing game where the user has to guess a number between 1 and 100.

```python
# Solution
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"You have {remaining} attempts left.")
    else:
        print(f"Game over! The number was {secret_number}")
```

### Exercise 7: Pattern Printing
Write programs to print various patterns:

```python
# Pattern 1: Right triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Pattern 2: Number pyramid
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# Pattern 3: Diamond
n = 5
# Upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
```

### Exercise 8: Menu-Driven Calculator
Create a calculator program with a menu system.

```python
# Solution
def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero!")
        else:
            print("Invalid choice! Please try again.")

calculator()
```

### Exercise 9: Fibonacci Series
Generate the Fibonacci series up to n terms.

```python
# Solution
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series:")
    print(0)
else:
    print("Fibonacci series:")
    a, b = 0, 1
    print(a)
    print(b)
    
    for i in range(2, n):
        c = a + b
        print(c)
        a, b = b, c
```

### Exercise 10: Nested Loop Challenge
Create a program that prints a calendar for a given month (assume 30 days).

```python
# Solution
def print_calendar(month_name, start_day):
    print(f"\n{month_name} Calendar")
    print("Sun Mon Tue Wed Thu Fri Sat")
    
    # Print spaces for days before the first day
    for i in range(start_day):
        print("    ", end="")
    
    # Print days of the month
    day = 1
    while day <= 30:
        print(f"{day:3d} ", end="")
        
        # If it's Saturday, start a new line
        if (day + start_day - 1) % 7 == 6:
            print()
        
        day += 1
    
    print()  # Final newline

# Example usage
month = input("Enter month name: ")
start = int(input("Enter starting day (0=Sunday, 1=Monday, ..., 6=Saturday): "))
print_calendar(month, start)
```

## Practice Challenges

1. **Password Validator**: Create a program that validates passwords based on multiple criteria (length, uppercase, lowercase, digits, special characters).

2. **ATM Simulator**: Build a simple ATM program with options to check balance, deposit, withdraw, and exit.

3. **Rock Paper Scissors**: Implement the classic game with score tracking and multiple rounds.

4. **Prime Number Generator**: Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.

5. **Palindrome Checker**: Check if a given string or number is a palindrome using loops.

Remember to practice these concepts regularly to master conditional and looping constructs in Python!