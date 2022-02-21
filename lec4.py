'''
lec4
dict
tuple
'''

my_tuple = 'a', 'b', 'c', 'd', 'e'
print(my_tuple)

my_second_tuple = ('a', 'b', 'c', 'd', 'e')
print(my_second_tuple)

not_a_tuple= ('a') #not a tuple because function has just parenteses 
print(type(not_a_tuple))

is_a_tuple = ('a',) #comma makes a function a tuple
print(type(is_a_tuple))

print(my_tuple[-1])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])
print(my_tuple[:])

my_car = { 
    'color':'blue',
    'maker':'subaru',
    'year':2014
}

print(my_car)
print(my_car['year'])
print(my_car['color'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('year'))

my_car['model'] = 'outback'
print(my_car)

my_car['year'] = 2020
print(my_car)

print(len(my_car))

print(2020 in my_car)





