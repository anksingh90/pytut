# write a  program to randomly choose additional subject for students from the list of subjects
# sub = Hindi, Geo, Sales, AI, French, Spanish, Accountacnce, Physical Ed

import random
print("WELCOME TO THE ADDITIONAL SUBJECTS !!")
sub=['Hindi', 'Geo' , 'Sales', 'AI', 'French' , 'Spanish' , 'Accountacnce', 'Physical Ed']
a=random.randint(1,8)
print("the additional subject chosen is :", sub[a])