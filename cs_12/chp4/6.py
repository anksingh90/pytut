'''You have a list my_list = [10, 20, 30]. Ask the user for an index. Try to access and print the
element at that index. Handle the IndexError if the index is out of bounds.
a. Input : Output :
Enter an index (0-2): 1 Element at index 1: 20
Enter an index (0-2): 5 Error: Index out of range.'''

try:
    my_list=[10,20,30]
    print('List : ',my_list)
    x=int(input("enter index value :"))
    print(my_list[x])
except IndexError:
    print("index out of the range !")
    
