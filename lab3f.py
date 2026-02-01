#Maximillian Havrylyuk
#Lab3f.py
#exploring list functions and 2 dimension table usage

#creating a new list calle list4
list4 = [1,2,3,4,5]
#creating a user input and using the append() function to store it in the list
listadd = int(input("enter a number to add to list: "))
list4.append(listadd)
#multiplying every number by 10 after the append() from the user input so every number is multiplied by ten
list4 = [x * 10 for x in list4]
#sorting the list4 in descending order and printing the result
for p in list4:
    list4.sort(reverse=True)
print(list4)
