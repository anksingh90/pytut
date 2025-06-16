# Python File Handling: tell() and seek() Methods Tutorial

## Introduction

When working with files in Python, you often need to control where you're reading from or writing to within the file. The `tell()` and `seek()` methods provide this functionality by allowing you to get and set the current position in a file.

## What are tell() and seek()?

### tell() Method
- **Purpose**: Returns the current position of the file pointer
- **Returns**: An integer representing the byte position
- **Syntax**: `file_object.tell()`

### seek() Method
- **Purpose**: Moves the file pointer to a specific position
- **Returns**: The new position (in most cases)
- **Syntax**: `file_object.seek(offset, whence)`

## Parameters of seek()

The `seek()` method takes two parameters:

1. **offset**: Number of bytes to move
2. **whence** (optional): Reference point for the offset
   - `0` (default): Beginning of file
   - `1`: Current position
   - `2`: End of file

## Basic Examples

### Example 1: Using tell() to track position

```python
# Create a sample file
with open('sample.txt', 'w') as f:
    f.write("Hello, World! This is a test file.")

# Read and track position
with open('sample.txt', 'r') as f:
    print(f"Initial position: {f.tell()}")  # Output: 0
    
    data = f.read(5)
    print(f"Read: '{data}'")
    print(f"Position after reading 5 chars: {f.tell()}")  # Output: 5
    
    data = f.read(7)
    print(f"Read: '{data}'")
    print(f"Position after reading 7 more chars: {f.tell()}")  # Output: 12
```

### Example 2: Using seek() to move around the file

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

## Advanced Examples

### Example 3: Seeking from different reference points

```python
with open('sample.txt', 'r') as f:
    # Get file size by seeking to end
    f.seek(0, 2)  # Move to end of file
    file_size = f.tell()
    print(f"File size: {file_size} bytes")
    
    # Move to 10 bytes from the end
    f.seek(-10, 2)
    print(f"Position (10 from end): {f.tell()}")
    print(f"Read: '{f.read()}'")
    
    # Move to middle of file
    f.seek(file_size // 2)
    print(f"Position (middle): {f.tell()}")
    print(f"Read: '{f.read(10)}'")
```

### Example 4: Binary file handling

```python
# Create a binary file
data = b"Binary data example for seek and tell"
with open('binary_sample.bin', 'wb') as f:
    f.write(data)

# Read binary file with seek and tell
with open('binary_sample.bin', 'rb') as f:
    print(f"Initial position: {f.tell()}")
    
    # Read first 6 bytes
    chunk = f.read(6)
    print(f"Read: {chunk}")
    print(f"Position: {f.tell()}")
    
    # Seek to byte 12
    f.seek(12)
    chunk = f.read(7)
    print(f"Read from position 12: {chunk}")
    
    # Seek relative to current position
    f.seek(4, 1)  # Move 4 bytes forward from current position
    chunk = f.read(4)
    print(f"Read after relative seek: {chunk}")
```

### Example 5: Practical use case - Reading file in chunks

```python
def read_file_in_chunks(filename, chunk_size=10):
    """Read a file in chunks and show position tracking"""
    with open(filename, 'r') as f:
        chunk_number = 1
        
        while True:
            position_before = f.tell()
            chunk = f.read(chunk_size)
            
            if not chunk:  # End of file
                break
                
            position_after = f.tell()
            print(f"Chunk {chunk_number}: '{chunk}'")
            print(f"Position before: {position_before}, after: {position_after}")
            chunk_number += 1

# Example usage
with open('large_sample.txt', 'w') as f:
    f.write("This is a longer text file that we will read in chunks to demonstrate the tell and seek methods.")

read_file_in_chunks('large_sample.txt', 15)
```

## Important Notes and Best Practices

### 1. Text vs Binary Mode
- In text mode, `tell()` and `seek()` work with character positions
- In binary mode, they work with byte positions
- Some operations (like seeking from current position) may not work in text mode on all platforms

### 2. File Mode Considerations
```python
# Text mode - may have limitations
with open('file.txt', 'r') as f:
    f.seek(10, 1)  # May not work in text mode

# Binary mode - full functionality
with open('file.txt', 'rb') as f:
    f.seek(10, 1)  # Works in binary mode
```

### 3. Error Handling
```python
try:
    with open('nonexistent.txt', 'r') as f:
        f.seek(100)
        position = f.tell()
except FileNotFoundError:
    print("File not found!")
except OSError as e:
    print(f"OS Error: {e}")
```

## Common Use Cases

1. **Log file analysis**: Jump to specific positions in large log files
2. **Database files**: Navigate to specific records
3. **Binary file parsing**: Read headers, skip sections, parse structured data
4. **File validation**: Check file size, read specific portions
5. **Resume interrupted downloads**: Continue from last known position

## Programming Questions

### Question 1: Basic Position Tracking
Write a function that reads a file and returns a list of tuples, where each tuple contains:
- The word read
- The position before reading the word
- The position after reading the word

```python
def track_word_positions(filename):
    # Your code here
    pass

# Expected output format: [('Hello', 0, 5), ('World', 6, 11), ...]
```

### Question 2: File Reverser
Create a function that reads a file backwards (from end to beginning) using seek() and tell(). The function should print each character in reverse order.

```python
def read_file_backwards(filename):
    # Your code here
    pass
```

### Question 3: Binary File Header Reader
Write a function that reads the first 16 bytes of a binary file as a header, then seeks to a specific offset and reads a data chunk. The function should return both the header and the data chunk.

```python
def read_binary_with_offset(filename, data_offset, data_size):
    # Your code here
    # Should return (header_bytes, data_bytes)
    pass
```

### Question 4: File Position Bookmarker
Create a class that allows you to bookmark positions in a file and return to them later.

```python
class FileBookmarker:
    def __init__(self, filename, mode='r'):
        # Your code here
        pass
    
    def bookmark(self, name):
        # Save current position with a name
        pass
    
    def goto_bookmark(self, name):
        # Seek to a saved bookmark
        pass
    
    def list_bookmarks(self):
        # Return list of bookmark names and positions
        pass
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Your code here
        pass

# Usage example:
# with FileBookmarker('data.txt') as fb:
#     fb.bookmark('start')
#     # read some data
#     fb.bookmark('middle')
#     # read more data
#     fb.goto_bookmark('start')
```

### Question 5: File Comparison Tool
Write a function that compares two files byte by byte and reports the first position where they differ, using seek() and tell() efficiently.

```python
def find_file_difference(file1, file2, chunk_size=1024):
    # Your code here
    # Should return the byte position where files first differ, or -1 if identical
    pass
```

### Question 6: Log File Analyzer
Create a function that analyzes a log file by:
1. Finding the position of the last occurrence of a specific pattern
2. Reading the last N lines from that position
3. Returning both the position and the lines

```python
def analyze_log_file(filename, pattern, num_lines=10):
    # Your code here
    # Should return (position, lines_list)
    pass
```

### Question 7: File Pagination
Implement a file pagination system that can display a file in pages using seek() and tell().

```python
class FilePaginator:
    def __init__(self, filename, page_size=100):
        # Your code here
        pass
    
    def get_page(self, page_number):
        # Return the content of specified page
        pass
    
    def total_pages(self):
        # Return total number of pages
        pass
    
    def current_position(self):
        # Return current file position
        pass

# Usage:
# paginator = FilePaginator('large_file.txt', 50)
# page1 = paginator.get_page(1)
# page2 = paginator.get_page(2)
```

## Solutions Hints

1. **Question 1**: Use split() to get words, track position before and after each read operation
2. **Question 2**: Start from file end, seek backwards one character at a time
3. **Question 3**: Read header first, then seek to offset and read data chunk
4. **Question 4**: Use a dictionary to store bookmarks, implement context manager
5. **Question 5**: Read both files in chunks, compare byte by byte, track positions
6. **Question 6**: Search for pattern throughout file, remember last position, read backwards for lines
7. **Question 7**: Calculate page boundaries, use seek to jump to page start positions

## Conclusion

The `tell()` and `seek()` methods are powerful tools for file manipulation in Python. They provide precise control over file positioning, enabling efficient file processing for various applications. Practice with these methods will help you handle large files, implement file-based algorithms, and create efficient file processing utilities.

Remember to always handle exceptions appropriately and consider the differences between text and binary modes when using these methods in your applications.