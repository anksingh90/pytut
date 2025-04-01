import csv
data1 = [['Name','Age','city'],['Alice','31','Delhi'],['Eisha','36','Delhi']]
with open('data.csv','w',newline = '')as file: # connection made with csv file.
    obj = csv.writer(file) # write data in csv file
    obj.writerows(data1) # writes single or multiple lines into CSV file.