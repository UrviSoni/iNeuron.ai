# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

#######  Solution

## Sum of First n Natural numbers by Asking user for Number.

def myreduce(num):
    ''' This functionm will return sum of n Natural numbers'''
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements

#Input 
print("Input:")
number=int(input("Please insert the number :"))

#Function Execution

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])


#### Same Solution can be approached by Built-in reduce() function

print("Input:")
number=int(input("Please insert the number :"))

num_list= list(range(1,(number+1)))
# Import reduce function 
from functools import reduce
sum_of_elements = reduce((lambda x, y: x + y), num_list)

#Output
print("Output:")
print("List of First n Natural numbers are:",num_list)
print("Sum of List elements are :",sum_of_elements)
