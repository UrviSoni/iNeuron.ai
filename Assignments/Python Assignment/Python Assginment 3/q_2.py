# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()


#### Solution

## Filter the even and odd number from list which are multiples  of 5

# Input 

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))


def myfilter(num_list):
    '''This function will filter even and odd numbers from list which are multiples of 5 '''
    num_even_list=[]
    num_odd_list=[]
    
    for i in num_list:
        if(i%5==0):
            if(i%2==0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)
                
    return num_even_list,num_odd_list


# Function Execution
output_value=myfilter(num_list)

# Output

print("Output:")
print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])


### Same solution can be approached by built-in filter() function

# Input 

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))

num_even_list=list(filter(lambda x: x%2==0,list(filter(lambda x: x%5==0 ,num_list))))
num_odd_list= list(filter(lambda x: x%2!=0,list(filter(lambda x: x%5==0 ,num_list))))

print("Output:")

print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",num_even_list)
print("List of Odd numbers, which are multiples of 5 are:",num_odd_list)
