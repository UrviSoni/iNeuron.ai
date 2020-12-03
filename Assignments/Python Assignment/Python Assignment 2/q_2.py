# Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:

# Input Word : ineuron
# Output Word : norueni

w = input("Write the word for the reverse: ") # taking 'w' as variable for getting input
# here char = (len(w) - 1, -1, -1) suppose w = ineuron so len(w) = 7 (7-1, -1, -1) char = (6, -1, -1) last -1 is step value.
for char in range(len(w) - 1, -1, -1): # loop for printing reverse word
	print(w[char], end="") # printing each word of character
print("\n")