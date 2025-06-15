# File Handling Practice Questions
## Menu-Driven Programs with write(), writelines(), read(), and readlines()

---

## Question 1: Personal Diary Application

Create a **menu-driven program** to manage a personal diary with the following features:

### 📋 Requirements
- **Menu Options:**
  1. Write diary entry
  2. Read all diary entries
  3. Exit

### Implementation Details
- Use `write()` to save diary entries to `diary.txt`
- Each entry should include date and content
- Use `read()` to display all diary entries
- Handle file not found exception

---

## Question 2: Shopping List Manager

Develop a **menu-driven program** to manage shopping lists:

### 📋 Requirements
- **Menu Options:**
  1. Add items to shopping list  
  2. View shopping list
  3. Clear shopping list
  4. Exit

### Implementation Details
- Use `writelines()` to save multiple items at once
- Store items in `shopping_list.txt`
- Use `readlines()` to display all items with numbering
- Allow adding multiple items in one session

---

## Question 3: Student Report Card System

Create a **menu-driven program** for student report management:

### 📋 Requirements
- **Menu Options:**
  1. Add student marks
  2. View all student reports
  3. Calculate and save class average
  4. Exit

### Implementation Details
- Use `write()` to save student data to `reports.txt`
- Store: Name, Subject, Marks (one per line)
- Use `read()` to display all reports
- Calculate average from saved data

---

## Question 4: Movie Collection Database

Build a **menu-driven program** to manage movie collection:

### 📋 Requirements
- **Menu Options:**
  1. Add multiple movies
  2. View movie collection
  3. Search for a movie
  4. Exit

### Implementation Details
- Use `writelines()` to add movie list to `movies.txt`
- Include: Title, Genre, Year, Rating
- Use `readlines()` to read and display movies
- Implement basic search functionality

---

## Question 5: Employee Attendance Tracker

Develop a **menu-driven program** for attendance management:

### 📋 Requirements
- **Menu Options:**
  1. Mark attendance for multiple employees
  2. View attendance records
  3. Generate attendance summary
  4. Exit

### Implementation Details
- Use `writelines()` to save attendance data to `attendance.txt`
- Format: Employee_ID, Name, Date, Status
- Use `readlines()` to read and process attendance
- Count present/absent days

---

## Question 6: Recipe Book Manager

Create a **menu-driven program** to manage cooking recipes:

### 📋 Requirements
- **Menu Options:**
  1. Add new recipe
  2. View all recipes
  3. Add ingredients to existing recipe
  4. Exit

### Implementation Details
- Use `write()` and `writelines()` for recipe storage in `recipes.txt`
- Store recipe name, ingredients list, and instructions
- Use `read()` to display complete recipe book
- Format recipes clearly with separators

---

## Question 7: Library Book Catalog

Build a **menu-driven program** for library management:

### 📋 Requirements
- **Menu Options:**
  1. Add multiple books to catalog
  2. View complete catalog
  3. Check book availability
  4. Update book status
  5. Exit

### Implementation Details
- Use `writelines()` to add book details to `library.txt`
- Include: Book_ID, Title, Author, Status (Available/Issued)
- Use `readlines()` to search and display books
- Implement status update functionality

---

## Question 8: Daily Expense Tracker

Develop a **menu-driven program** for expense tracking:

### 📋 Requirements
- **Menu Options:**
  1. Add daily expenses
  2. View all expenses
  3. Calculate total expenses
  4. View expenses by category
  5. Exit

### Implementation Details
- Use `writelines()` to save expense data to `expenses.txt`
- Format: Date, Category, Amount, Description
- Use `readlines()` to read and categorize expenses
- Calculate totals and category-wise breakdown

---

## Question 9: Contact Book Application

Create a **menu-driven program** for contact management:

### 📋 Requirements
- **Menu Options:**
  1. Add multiple contacts
  2. View all contacts
  3. Search contact by name
  4. Update contact information
  5. Exit

### Implementation Details
- Use `writelines()` to save contacts to `contacts.txt`
- Include: Name, Phone, Email, Address
- Use `readlines()` to search and display contacts
- Implement contact update functionality

---

## Question 10: Inventory Management System

Build a **menu-driven program** for inventory tracking:

### 📋 Requirements
- **Menu Options:**
  1. Add multiple products
  2. View complete inventory
  3. Update product quantity
  4. Check low stock items
  5. Exit

### Implementation Details
- Use `writelines()` to save inventory to `inventory.txt`
- Format: Product_ID, Name, Quantity, Price, Category
- Use `readlines()` to read and process inventory data
- Identify products with quantity below threshold
- Implement quantity update functionality

---

## 🎯 General Implementation Guidelines

### File Operations Best Practices
- Always use **try-except** blocks for file operations
- Handle **FileNotFoundError** gracefully
- Close files properly or use **with** statement
- Provide clear user feedback after operations

### Menu System Requirements
- Use **while** loops for continuous menu display
- Implement input validation for menu choices
- Provide option to return to main menu
- Clear and user-friendly interface

### Data Format Consistency
- Maintain consistent data format in files
- Use appropriate separators (comma, pipe, etc.)
- Include headers or clear data structure
- Handle empty files appropriately

### Function Organization
- Create separate functions for each major operation
- Use meaningful function names
- Implement proper error handling in functions
- Keep code modular and readable

---

*Focus on creating robust, user-friendly applications with proper file handling and error management!*
