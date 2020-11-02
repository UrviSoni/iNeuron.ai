# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.

n = [] # Taking empty list

for i in range(2000,3201): # Here, 2000 and 3200 both are included
    if (i%7==0) and [(i%5!=0)]: # numbers are divisible by 7 and are not multiole of 5
        n.append(str(i)) # append those numbers in list
print(",".join(n)) # join those numbers with comma-separated sequence