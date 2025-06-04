
# File Handling in Python

File handling is an essential part of many Python programs. It allows your code to read from and write to files stored on your computer.

---

## 1.1 File Handling in Text

### Basic File Operations

Python provides built-in functions for file operations:

- `open()`
- `read()`, `readline()`, `readlines()`
- `write()`, `writelines()`
- `close()`

### Opening a File

```python
file = open("example.txt", "mode")
```

**Modes:**

| Mode | Description |
|------|-------------|
| `'r'` | Read (default). File must exist. |
| `'w'` | Write. Creates file or truncates. |
| `'a'` | Append. Creates file if not exists. |
| `'x'` | Create new file, error if exists. |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |
| `'+'` | Read and write mode |

---

### Reading from a File

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

#### Other Read Methods

```python
file.readline()   # Reads a single line
file.readlines()  # Returns a list of all lines
```

---

### Writing to a File

```python
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("Python is awesome!")
file.close()
```

> Note: `'w'` mode will **overwrite** the file if it exists.

---

### Appending to a File

```python
file = open("example.txt", "a")
file.write("\nThis is a new line.")
file.close()
```

---

### Using `with` Statement

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

---

### Checking If File Exists

```python
import os
if os.path.exists("example.txt"):
    print("The file exists")
else:
    print("The file does not exist")
```

---

## 1.2 Exercise

### Reading from File (10 Questions)

1. Read the content of a file named `data.txt` and print it to the console.  
2. Read only the first line of `info.txt` and display it.  
3. Print the number of words in the file `story.txt`.  
4. Read `students.txt` and display all student names that start with the letter 'A'.  
5. Count how many lines are in `report.txt`.  
6. Read `marks.txt` and calculate the total of all numbers written line by line.  
7. Read a file `notes.txt` and print each line in uppercase.  
8. Check if the word 'Python' exists in `course.txt`. If yes, print “Found”.  
9. Display the last line from the file `summary.txt`.  
10. Read all lines from `logs.txt` into a list and print that list.  

---

### Reading + Writing to File (10 Questions)

1. Read `data.txt` and write all lines containing the word “error” into a new file `errors.txt`.  
2. Read numbers from `input.txt`, square each number, and write the results to `squares.txt`.  
3. Read names from `names.txt`, sort them alphabetically, and write to `sorted_names.txt`.  
4. Read text from `paragraph.txt`, count the number of characters, and write the count to `charcount.txt`.  
5. Copy content of `source.txt` to `destination.txt`.  
6. Read sentences from `input.txt`, reverse each sentence, and write to `reversed.txt`.  
7. Read a file `students.txt` and write names longer than 5 characters to `longnames.txt`.  
8. Read all lines from `notes.txt`, remove blank lines, and save cleaned content in `cleaned_notes.txt`.  
9. Read lines from `sales.txt`, convert each number to float, sum them up, and write the total in `total_sales.txt`.  
10. Read an input file and write only the first 5 lines to a new file.  

---

### Appending + Reading/Writing (10 Questions)

1. Append a new student name to `students.txt` and then print the entire updated file.  
2. Read `log.txt`, then append the current date and time at the end of the file.  
3. Append a user-provided sentence to `diary.txt` and then read and print all content.  
4. Check if a file `score.txt` exists. If it does, append “New score recorded.” Otherwise, create and write it.  
5. Append 5 random numbers to `numbers.txt`, then read and display the full file.  
6. Add a new entry to `inventory.txt` in the format “item,quantity” and then show all items.  
7. Write initial data to `data.txt`, then append “End of file.” Finally, print the entire file.  
8. Append 3 user input lines to `feedback.txt`, and display the last 3 lines of the file.  
9. Read from `old.txt`, append all content to `archive.txt` with a heading “Archived Content:”.  
10. Append a line to `log.txt` every time the program runs, saying "Program executed", then display total lines.  
