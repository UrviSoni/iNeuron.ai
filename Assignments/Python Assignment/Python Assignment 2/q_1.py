# Create the below pattern using nested for loop in Python.
#
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

r = 5 # Here taking r = rows = 5 because as we can see we have maximum 5 times * is printing
for i in range(0, r): # i = (0, 5)
    for j in range(0, i + 1): # j = (0, 1), j = (1,2) ....
        print("*", end=' ') # printing '*'
    print("\r")
# Loop for reverse printing
for i in range(r, 0, -1): # i = (5, 0, -1) here -1 is step value
    for j in range(0, i - 1): # j = (0, 5 - 1), j = (0, 4 - 1) ...
        print("*", end=' ') # printing '*'
    print("\r")