# tuple1 = (3,4,9,2)
# list1 = [6,2,9,6,1]

#print(tuple1,str(list1))
#list1+=tuple1
#print(list1) 

# result = tuple(list(tuple1)+(list1))
# print(result)

# list1.extend(list(tuple1))
# print(list1)

# tuple1 = list(tuple1)
# tuple1.extend(list1)
# tuple1 = tuple(tuple1)
# print(tuple1)

# index=5
# list1.insert(index,tuple1)
# print(list1)

# print(list1)
# print(tuple1)
# list_with_tuple = list(sum(zip(list1, tuple1),()))
# print(list_with_tuple)

# tuple_with_list = tuple(sum(zip(list1,list(tuple1)),()))
# print(tuple_with_list)

# string1 = "Alexander"
# c = ['A','l','e','x','a','n','d','e','r','U','z','o','w']
# joined_list = ''.join(c)
# result =  string1 in joined_list
# print(result)

# list1= ['a',4,1,0,'b']
# list2=['c',6,3,1,'d']
# list1.extend(list2)
# print(list1)

# tuple1 = 3,52,44,22
# sum=0
# for num in tuple1:
#     sum+=num

# print(sum)
# import sys

# tuple1=(1,4,2,5,2)
# tuple2=('a','f','l','b')
# tuple3=('a',3,1,'k','p',10)
# print('size of tuple1 '+ str(sys.getsizeof(tuple1))+' bytes')
# print('size of tuple2 '+ str(sys.getsizeof(tuple2))+' bytes')
# print('size of tuple3 '+ str(sys.getsizeof(tuple3))+' bytes')

# print('size of tuple1 '+ str(tuple1.__sizeof__())+' bytes')
# print('size of tuple2 '+ str(tuple2.__sizeof__())+' bytes')
# print('size of tuple3 '+ str(tuple3.__sizeof__())+' bytes')

numbers = 1, 2, 3, 4, 5
result = []
for num in numbers:
    cube = num ** 3
    pair = (num, cube)
    result.append(pair)

print(tuple(result))

tuples = 2, 4, 3, 6, 8, 10, 12, 1, 2, 3, 14, 16
result = []
for tup in tuples:
    if tup % 2 ==0:
        result.append(tup)
print(tuple(result))

