'''
Assignment: Student Information and Marks Management
Objective:
Create a Python program to manage student information and their marks in different subjects.
Task:
Write a Python program that performs the following tasks:
Asks the user to enter the number of students in a class.
Creates a dictionary to store student information with roll numbers as keys and student names as values.
For each student, asks the user to enter the number of subjects and the marks scored in each subject.
Creates another dictionary to store subject-wise marks for each student with student names as keys and subject marks as values.
'''
stu_info={}
stu = {}
stu_no = int(input("enter the no. of students in a class :"))

for i in range(stu_no):
     roll_no=int(input("enter the roll no. :"))
     name=input("enter the student name :")
     stu_info[roll_no]=name # dictionary with students rollno, name
     stu[f"stu_{roll_no}"] = {} # blank dictionary with rollno

