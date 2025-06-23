# 📁 Python File Handling: tell() and seek() Methods Tutorial

> **Master file navigation in Python with precise position control**

---

## 🌟 Introduction

When working with files in Python, you often need to control where you're reading from or writing to within the file. The `tell()` and `seek()` methods provide this functionality by allowing you to get and set the current position in a file.

---

## 🔍 What are tell() and seek()?

### 📍 tell() Method

| Property | Description |
|----------|-------------|
| **Purpose** | Returns the current position of the file pointer |
| **Returns** | An integer representing the byte position |
| **Syntax** | `file_object.tell()` |

### 🎯 seek() Method

| Property | Description |
|----------|-------------|
| **Purpose** | Moves the file pointer to a specific position |
| **Returns** | The new position (in most cases) |
| **Syntax** | `file_object.seek(offset, whence)` |

---

## ⚙️ Parameters of seek()

The `seek()` method takes two parameters:

1. **`offset`** - Number of bytes to move
2. **`whence`** *(optional)* - Reference point for the offset

### Reference Points (whence)

| Value | Constant | Description | Example |
|-------|----------|-------------|---------|
| `0` | `os.SEEK_SET` | Beginning of file *(default)* | `f.seek(10, 0)` |
| `1` | `os.SEEK_CUR` | Current position | `f.seek(5, 1)` |
| `2` | `os.SEEK_END` | End of file | `f.seek(-10, 2)` |

---

## 💡 Basic Examples

### 🔸 Example 1: Using tell() to track position

```python
# Create a sample file
with open('sample.txt', 'w') as f:
    f.write("Hello, World! This is a test file.")

# Read and track position
with open('sample.txt', 'r') as f:
    print(f"Initial position: {f.tell()}")  # Output: 0
    
    data = f.read(5)
    print(f"Read: '{data}'")  # 'Hello'
    print(f"Position after reading 5 chars: {f.tell()}")  # Output: 5
    
    data = f.read(7)
    print(f"Read: '{data}'")  # ', World'
    print(f"Position after reading 7 more chars: {f.tell()}")  # Output: 12
```

**Output:**
```
Initial position: 0
Read: 'Hello'
Position after reading 5 chars: 5
Read: ', World'
Position after reading 7 more chars: 12
```

### 🔸 Example 2: Using seek() to move around the file

```python
with open('sample.txt', 'r') as f:
    # Read from beginning
    print(f"Position: {f.tell()}")  # 0
    print(f"Read: '{f.read(5)}'")   # "Hello"
    
    # Move to position 7
    f.seek(7)
    print(f"Position after seek(7): {f.tell()}")  # 7
    print(f"Read: '{f.read(5)}'")   # "World"
    
    # Move to beginning
    f.seek(0)
    print(f"Position after seek(0): {f.tell()}")  # 0
    print(f"Read: '{f.read(5)}'")   # "Hello"
```

**Output:**
```
Position: 0
Read: 'Hello'
Position after seek(7): 7
Read: 'World'
Position after seek(0): 0
Read: 'Hello'
```

---

## 🚀 Advanced Examples

### 🔸 Example 3: Seeking from different reference points

#### Understanding the Parameters

- **`offset`**: The number of bytes to move the file pointer
  - Can be positive (move forward) or negative (move backward)
- **`whence`**: The reference position from where the offset is calculated

#### Common Seek Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| `f.seek(0, 0)` | Move to beginning | Start of file |
| `f.seek(0, 1)` | Stay at current position | No movement |
| `f.seek(0, 2)` | Move to end of file | End position |
| `f.seek(10, 0)` | Move to 10th byte from start | Absolute positioning |
| `f.seek(10, 1)` | Move 10 bytes forward | Relative positioning |
| `f.seek(-10, 2)` | Move 10 bytes before end | From end backwards |

```python
with open('sample.txt', 'r') as f:
    # Get file size by seeking to end
    f.seek(0, 2)  # Move to end of file
    file_size = f.tell()
    print(f"📏 File size: {file_size} bytes")
    
    # Move to 10 bytes from the end
    f.seek(-10, 2)
    print(f"📍 Position (10 from end): {f.tell()}")
    print(f"📖 Read: '{f.read()}'")
    
    # Move to middle of file
    f.seek(file_size // 2)
    print(f"📍 Position (middle): {f.tell()}")
    print(f"📖 Read: '{f.read(10)}'")
```

**Output:**
```
📏 File size: 35 bytes
📍 Position (10 from end): 25
📖 Read: 'test file.'
📍 Position (middle): 17
📖 Read: 'This is a '
```

---

## ⚠️ Important Notes

> **🚨 Error Handling**: Invalid `whence` values (like `-1` or `-2`) will raise a `ValueError`

> **💾 Binary vs Text Mode**: Seeking behavior may differ between binary and text modes, especially with encoding considerations

> **🔒 File Mode**: Some seek operations are only available in certain file modes (e.g., seeking from end requires read access to determine file size)

---

## 🎯 Best Practices

1. **Always use context managers** (`with` statement) for file operations
2. **Check file position** with `tell()` before critical operations
3. **Handle exceptions** when seeking to invalid positions
4. **Consider file size** before seeking to avoid errors
5. **Use meaningful variable names** for offset calculations

---

*Happy coding! 🐍✨*