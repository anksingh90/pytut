# create a function cal_avg(num) that calculates avg of a list , use try and except to handle the error.

num=['a','b','c']
def cal_avg(num):
    print(num)
    try:
        x=num/3
        y=print(x)
        return y
    except TypeError:
        print("num cannot be divided by any character")

cal_avg(num)