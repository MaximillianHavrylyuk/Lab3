#Maximillian Havrylyuk
#Lab3a.py
#exploring list functions and 2 dimension table usage

#importing the random module so I can generate random numbers usuing the randint() function
import random
#creating empty list
list_a = []
#creating for loop that will generate random numbers between 0-99 and will generate and print 20 of those random numbers and sort the,
for a in range(20):
    list_a.append(random.randint(0,99))
    list_a.sort()
print(list_a)
