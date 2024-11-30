#set is collection of no duplicates 

list_number=[1,1,2,3,3,3,4,4,5,5,5,5,6]
unique_num=set(list_number)
print(unique_num)

#current set has below values without duplicates 
second_set={1,4}
#adding elemnt to set 
second_set.add(5)
second_set.add(9)
print(second_set)

#In order to get the union of two set put the operation "|"
print(unique_num|second_set)

#we can perform and operations also bit operation
print(unique_num&second_set)
print(unique_num-second_set)
print(unique_num^second_set)

if 1 in second_set:
    print("yes")
else:
    print("no")