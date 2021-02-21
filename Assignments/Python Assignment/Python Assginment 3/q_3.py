# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


# Solution

# Section 1
word_1=list('xyz')
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

# Section 2
word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

# Section 3
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

# Section 4
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

# Section 5
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)
