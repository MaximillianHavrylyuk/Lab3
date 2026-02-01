#Maximillian Havrylyuk
#Lab3d.py
#exploring list functions and 2 dimension table usage

#making a new list with natural elements
mylist = [1,2,3,4,5,6]
#adding the element 7 to the right side of the list
mylist.append(7)
#inserting the element 0 at index 0/the very first number in the list
mylist.insert(0,0)
#removing an element from the index 2 or the third number
mylist.pop(2)
#printing the outcome
print(mylist)
#printing a string to display the number that is at index 7 in a readable and understandable format
print("The element",mylist.index(7),"is present at the index 7")
