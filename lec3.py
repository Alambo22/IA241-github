'''
lec3
'''

my_list = [1, 2, 3, 4, 5 ]
print(my_list)

#my_nested_list = [1,2,3 , [1,2,3 ] ]
#print(my_nested_list)

my_nested_list = [1,2,3, my_list]
print(my_nested_list)

my_list[0] = 6
print(my_list)

print(my_list)
print(my_list[1:3])
print(my_list[:3])
print(my_list[3:])
print(my_list[:])

x,y = ['a','b']
print(x)
print(y)
print(x,y)
print(y,x)
print(x,y,y,x)

print(my_list)

my_list.append(7) #add
print(my_list)

my_list.append(1)
print(my_list)

my_list.remove(7) #remove
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse() #reverses values
print(my_list)

print(my_list + [8,9]) #list + list
my_list.extend(['a','b']) #adding more items to list
print(my_list)

print('a' in my_list) #check whether item is IN list 

print(len(my_list)) #tells you how many items in list

print('hello\tworld') #\t is a space (tab)

print('hello\nworld') #\n is a new line

print(len( 'hello world'))

print( 'hello world'[2])

my_letters = ['a', 'a', 'b', 'b', 'c']
print(my_letters) #allowed to have the same values in a list
print(set(my_letters)) #set gets rid of the same values in the list 

my_unique_letters = set(my_letters) #turned into a variable
print(my_unique_letters) 
print(len(my_unique_letters))
print('e' in my_unique_letters)
print(list(my_unique_letters)[2])
