# Python File Handling Programming Assignment

## Instructions
Complete **ALL THREE** programs below. You may write the programs with or without using functions - both approaches are acceptable. Focus on implementing the core functionality: menu-driven interface, file operations, and edit capabilities.

## Learning Objectives
- Implement file handling operations (read, write, append)
- Create menu-driven programs with user interaction
- Handle exceptions for file operations
- Work with string manipulation and list operations
- Implement edit/update functionality for file data

---

## Program 1: Daily Task Logger with Edit Option

### Description
Create a task management program that allows users to log daily tasks, view all tasks, and edit existing tasks.

### Requirements
1. **Add Task Function**: Allow users to input a task and save it to `tasks.txt`
2. **View Tasks Function**: Display all tasks with numbering (1, 2, 3...)
3. **Edit Task Function**: Allow users to select a task by number and modify its description
4. **Menu System**: Implement a loop with options:
   - 1. Add Task
   - 2. View All Tasks  
   - 3. Edit a Task
   - 4. Exit

### Technical Specifications
- File name: `tasks.txt`
- Each task should be stored on a new line
- Handle file not found errors gracefully
- Validate user input for task selection
- Use appropriate success/error messages with emojis

### Sample Output
```
--- Task Manager Menu ---
1. Add Task
2. View All Tasks
3. Edit a Task
4. Exit
Enter your choice (1-4): 2

📋 Your Tasks:
1. Complete Python assignment
2. Buy groceries
3. Call mom
```

---

## Program 2: Guest Entry Logger with Date Edit

### Description
Create a guest registration system that logs visitor information with timestamps and allows editing of check-in dates.

### Requirements
1. **Add Guest Function**: Record guest name with current date/time
2. **View Guests Function**: Display all registered guests with numbers
3. **Edit Check-in Date Function**: Allow modification of a guest's check-in date only
4. **Menu System**: Implement options:
   - 1. Add Guest
   - 2. View Guest List
   - 3. Edit Guest Check-in Date
   - 4. Exit

### Technical Specifications
- File name: `guests.txt`
- Format: `"Name - Checked in at YYYY-MM-DD HH:MM:SS"`
- Import and use `datetime` module for timestamps
- Parse existing entries to separate name from timestamp
- Validate date format input during editing

### Sample Output
```
--- Guest Log Menu ---
1. Add Guest
2. View Guest List
3. Edit Guest Check-in Date
4. Exit
Enter your choice (1-4): 2

📒 Guest List:
1. John Smith - Checked in at 2024-03-15 14:30:25
2. Sarah Johnson - Checked in at 2024-03-15 15:45:12
```

---

## Program 3: Temperature Logger with Edit Capability

### Description
Develop a temperature monitoring system that logs temperature readings with timestamps and allows temperature value editing.

### Requirements
1. **Log Temperature Function**: Record temperature with current date/time
2. **View Logs Function**: Display all temperature entries with numbering  
3. **Edit Temperature Function**: Allow modification of temperature values while preserving timestamps
4. **Menu System**: Provide options:
   - 1. Log Temperature
   - 2. View Logs
   - 3. Edit Temperature
   - 4. Exit

### Technical Specifications
- File name: `temp_log.txt`
- Format: `"Temp: [value] - Logged at: YYYY-MM-DD HH:MM AM/PM"`
- Use 12-hour time format with AM/PM
- Parse entries to separate temperature from timestamp during editing
- Preserve original timestamp when editing temperature values

### Sample Output
```
--- Temperature Logger Menu ---
1. Log Temperature
2. View Logs  
3. Edit Temperature
4. Exit
Enter your choice (1-4): 2

🌡️ Temperature Log:
1. Temp: 36.5°C - Logged at: 2024-03-15 02:30 PM
2. Temp: 37.1°C - Logged at: 2024-03-15 06:45 PM
```

---

## Common Implementation Guidelines

### Error Handling
- Use try-except blocks for file operations
- Handle `FileNotFoundError` when files don't exist
- Validate user input for menu choices and edit selections
- Provide meaningful error messages

### Code Structure Options

**Option 1: With Functions**
```python
def function_name():
    # Implementation here
    pass

# Main program loop
while True:
    # Menu and function calls
```

**Option 2: Without Functions**  
```python
# Main program loop with inline code
while True:
    print("Menu options...")
    choice = input("Enter choice: ")
    if choice == '1':
        # Direct implementation
    elif choice == '2':
        # Direct implementation
```

### File Operations Required
- **Append mode ('a')**: Adding new entries
- **Read mode ('r')**: Viewing existing data  
- **Write mode ('w')**: Updating entire file after edits

### Input Validation
- Check for valid menu choices
- Validate numeric input for item selection
- Handle invalid list indices gracefully
- Confirm successful operations with appropriate messages

## Submission Requirements
1. Three separate Python files or one file with all three programs
2. Test each program thoroughly with various inputs
3. Ensure all menu options work correctly
4. Verify file operations create/update files properly
5. Include appropriate comments explaining key sections

## Evaluation Criteria
- **Functionality (40%)**: All features work as specified
- **Error Handling (25%)**: Proper exception handling and input validation  
- **Code Organization (20%)**: Clean, readable code structure
- **User Experience (15%)**: Clear menus, helpful messages, intuitive interface

---

**Note**: Focus on implementing the core functionality first, then enhance with better error handling and user experience features. Test your programs with edge cases like empty files, invalid inputs, and out-of-range selections.