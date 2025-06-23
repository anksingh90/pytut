# Chapter 5: File Handling - CSV Files

## Introduction to CSV Files

CSV (Comma-Separated Values) files are plain text files that store tabular data. Each line represents a record, and fields are separated by commas. CSV files are widely used for data exchange between different applications.

## Basic CSV Structure

```
Name,Age,City,Salary
John,25,New York,50000
Alice,30,London,60000
Bob,35,Paris,55000
```

## Python CSV Module

Python provides a built-in `csv` module for handling CSV files efficiently.

### Importing the CSV Module

```python
import csv
```

## Reading CSV Files

### Method 1: Using csv.reader()

```python
import csv

# Reading CSV file
with open('employees.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Read header
    header = next(csv_reader)
    print("Header:", header)
    
    # Read data rows
    for row in csv_reader:
        print(row)
```

**Output:**
```
Header: ['Name', 'Age', 'City', 'Salary']
['John', '25', 'New York', '50000']
['Alice', '30', 'London', '60000']
['Bob', '35', 'Paris', '55000']
```

### Method 2: Using csv.DictReader()

```python
import csv

# Reading CSV as dictionary
with open('employees.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")
```

**Output:**
```
Name: John, Age: 25, City: New York
Name: Alice, Age: 30, City: London
Name: Bob, Age: 35, City: Paris
```

## Writing CSV Files

### Method 1: Using csv.writer()

```python
import csv

# Sample data
data = [
    ['Name', 'Age', 'City', 'Salary'],
    ['John', 25, 'New York', 50000],
    ['Alice', 30, 'London', 60000],
    ['Bob', 35, 'Paris', 55000]
]

# Writing CSV file
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write all rows
    csv_writer.writerows(data)
    
    # Or write one row at a time
    # csv_writer.writerow(['Mike', 28, 'Tokyo', 45000])
```

### Method 2: Using csv.DictWriter()

```python
import csv

# Sample data as dictionaries
employees = [
    {'Name': 'John', 'Age': 25, 'City': 'New York', 'Salary': 50000},
    {'Name': 'Alice', 'Age': 30, 'City': 'London', 'Salary': 60000},
    {'Name': 'Bob', 'Age': 35, 'City': 'Paris', 'Salary': 55000}
]

# Writing CSV using DictWriter
with open('employees_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City', 'Salary']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write header
    csv_writer.writeheader()
    
    # Write data rows
    csv_writer.writerows(employees)
```

## Advanced CSV Operations

### Handling Different Delimiters

```python
import csv

# Reading CSV with semicolon delimiter
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        print(row)

# Writing CSV with tab delimiter
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['John', '25', 'New York'])
```

### Handling Quotes and Special Characters

```python
import csv

# Data with commas and quotes
data = [
    ['Name', 'Description', 'Price'],
    ['Product A', 'High-quality, durable item', '29.99'],
    ['Product B', 'Special "premium" edition', '49.99']
]

# Writing with proper quoting
with open('products.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    csv_writer.writerows(data)
```

### Error Handling

```python
import csv
import os

def read_csv_safe(filename):
    try:
        if not os.path.exists(filename):
            print(f"File {filename} not found!")
            return
            
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            
            for row_num, row in enumerate(csv_reader, start=1):
                try:
                    print(f"Row {row_num}: {row}")
                except Exception as e:
                    print(f"Error processing row {row_num}: {e}")
                    
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except PermissionError:
        print(f"Permission denied to read {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
read_csv_safe('employees.csv')
```

## Practical Examples

### Example 1: Processing Sales Data

```python
import csv

def process_sales_data(filename):
    total_sales = 0
    product_sales = {}
    
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            product = row['Product']
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            sales = quantity * price
            
            total_sales += sales
            product_sales[product] = product_sales.get(product, 0) + sales
    
    return total_sales, product_sales

# Sample usage
# total, products = process_sales_data('sales.csv')
# print(f"Total Sales: ${total:.2f}")
# print("Sales by Product:", products)
```

### Example 2: Data Filtering and Export

```python
import csv

def filter_employees_by_age(input_file, output_file, min_age):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_reader = csv.DictReader(infile)
        csv_writer = csv.DictWriter(outfile, fieldnames=csv_reader.fieldnames)
        
        csv_writer.writeheader()
        
        for row in csv_reader:
            if int(row['Age']) >= min_age:
                csv_writer.writerow(row)

# Usage
filter_employees_by_age('employees.csv', 'senior_employees.csv', 30)
```

### Example 3: CSV Data Validation

```python
import csv
import re

def validate_csv_data(filename):
    errors = []
    
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 (header is row 1)
            # Validate email format
            email = row.get('Email', '')
            if email and not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                errors.append(f"Row {row_num}: Invalid email format")
            
            # Validate age is numeric
            age = row.get('Age', '')
            if age and not age.isdigit():
                errors.append(f"Row {row_num}: Age must be numeric")
            
            # Validate required fields
            required_fields = ['Name', 'Email']
            for field in required_fields:
                if not row.get(field, '').strip():
                    errors.append(f"Row {row_num}: {field} is required")
    
    return errors

# Usage
validation_errors = validate_csv_data('users.csv')
if validation_errors:
    print("Validation Errors:")
    for error in validation_errors:
        print(f"  - {error}")
else:
    print("CSV data is valid!")
```

## Best Practices

1. **Always use context managers (`with` statement)** to ensure files are properly closed
2. **Specify `newline=''` when writing CSV files** to avoid extra blank lines
3. **Handle encoding issues** by specifying encoding: `open(file, 'r', encoding='utf-8')`
4. **Use DictReader/DictWriter** for better code readability when working with headers
5. **Implement error handling** for file operations and data validation
6. **Validate data types** when reading numeric data from CSV
7. **Use appropriate quoting** when data contains special characters

## Common CSV Parameters

| Parameter | Description | Options |
|-----------|-------------|---------|
| `delimiter` | Field separator | `','`, `';'`, `'\t'` |
| `quotechar` | Character used to quote fields | `'"'`, `"'"` |
| `quoting` | When to quote fields | `csv.QUOTE_ALL`, `csv.QUOTE_MINIMAL` |
| `skipinitialspace` | Skip whitespace after delimiter | `True`, `False` |
| `lineterminator` | Line ending character | `'\n'`, `'\r\n'` |

## Summary

CSV file handling in Python is straightforward with the built-in `csv` module. Key points to remember:

- Use `csv.reader()` and `csv.writer()` for basic operations
- Use `csv.DictReader()` and `csv.DictWriter()` for header-based operations
- Always handle exceptions and validate data
- Consider encoding and delimiter requirements
- Use context managers for proper file handling

This tutorial covers the essential aspects of CSV file handling in Python, providing you with the tools needed to read, write, and process CSV data effectively.