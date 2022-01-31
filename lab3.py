"""
lab 3 list and set
"""
#3.1
str_list = ['a','d','e','b','c']

print(str_list)

str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2])
print(str_list[3])

#3.5
my_list = ['a','123', 123,'b','B','False', False, 123, None, 'none']
print(my_list) #just printing out the list as is 
print(len(my_list)) #printing out the number of items in my given list
print(len(set(my_list))) #shows how many unique items are in the list 

#3.6
print(len("This is my third python lab.")) #prints the number of characters in function but we want number of words
print(len("This is my third python lab.".split())) #each word is an item in list, counts number of words in function

#3.7
num_list = [12,32,43,35]
num_list.sort()
print(num_list)
print(num_list[0]) #min
print(num_list[-1]) #max

#3.8
game_board = [ [0,0,0],
                [0,0,0],
               [0,0,0]]
             
'''
[ [0,0,0],
 [0,1,0],
 [0,0,0]] 
 '''
game_board[1][1]=1
print(game_board)