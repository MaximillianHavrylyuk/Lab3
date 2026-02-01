#Maximillian Havrylyuk
#Lab3f.py
#exploring list functions and 2 dimension table usage

#copied code from lab which is 3 lists in a 2 dimensional table
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
#returning the element from row 2 and column 3 into the variable element and printing the result
element = matrix[1][2]
print(element)
#returning the element from the 2nd row and 2nd column and printing the result
element1 = matrix[1][1]
print(element1)
#returning the element and printing it from the indexes 0 and 1
element2 = matrix[0][1]
print(element2)
#returning and printing the element from the 3rd row and column
element3 = matrix[2][2]
print(element3)
#printing the whole 2 dimensional table using a for loop
for l in matrix:
    print(l)
