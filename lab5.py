'''
lab5 if statement
'''
#3.1
alien_color = 'red'

if alien_color == 'blue':
    print('you just earned 5 points')

#3.2
alien_color = 'red'

if alien_color == 'blue':
    print('you just earned 5 points')
    
else: 
    print('you just earned 10 points')
    
    
#3.3
favorite_fruits = ['rasberries', 'apples', 'kiwi']

if 'kiwi' in favorite_fruits:
    print('you really like kiwi')
    
if 'apples' in favorite_fruits:
    print('you really like apples') #changed from strawberries to apples to appear in statement
    
if 'banannas' in favorite_fruits:
    print('you really like banannas')
    
#3.4
age = 22 #able to change number 

#if age < 10:
    #print('you are a kid')
    
#elif age < 20:
    #print('you are a teenager')
    
#else:
   # print('you are an adult')
  #  if age > 65:
       # print('you are an elder')

if age >= 20: #greater than or equal to is what we are looking for
    print('you are an adult')
    if age >65:
        print('you are an elder')
        
elif age >10:
    print('you are a teenager')
else:
    print('you are a kid')