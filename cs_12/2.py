# Calculate tax as per user input salary.

basic_pay = int(input("enter the basic pay : "))

ca = 5/100*basic_pay
hra = 10/100*basic_pay
da = 40/100*basic_pay

print("city allowance : ", ca)
print("da : ", da)
print("hra : ", hra)

total_sal = basic_pay + ca + hra + da
print('Total Salary',total_sal)

annual_sal = total_sal * 12

# Tax calculate

if annual_sal <= 300000:
    print('No Salary !')
elif 300000 < annual_sal < 600000:
    tax = annual_sal*5/100

print('Tax : ', tax)
print('Net Salary : ', annual_sal - tax)

elif 600000 < annual_sal < 1000000: