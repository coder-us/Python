# MAP
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,3,4,5,6,7]

# newl=list(map(cube,l))
# print(newl)


# FILTER

# def filter_function(a):
#     return a>4

# l=[1,2,3,4,5,6,7,8,9]
# newl=list(filter(filter_function,l))
# print(newl)

# REDUCE
from functools import reduce

number=[1,2,3,4,5]
sum=reduce(lambda x,y : x+y,number)
print(sum)


# l=[1,2,3,4,5,6,7,8,9,0]
# sum=reduce(lambda x,y:x+y,l)
# print(sum)
