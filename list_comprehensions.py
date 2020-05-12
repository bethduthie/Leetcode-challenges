mystring = 'hello'
mylist = []

for x in mystring:
    mylist.append(x)

# more condensed version:
mylist = [x for x in mystring]

mylist = [x for x in 'word']

mylist = [num**2 for num in range(0,11)]



# can use nested loops and else/if statements in list comprehensions
# but it sacrifices readability

print(mylist)