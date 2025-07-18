# movies = []
# mov1=input("enter 1sr movie")
# movies.append(mov1)
# mov2=input("enter 2nd movie")
# movies.append(mov2)
# mov3=input("enter 3rd movie")
# movies.append(mov3)

# print(movies)

# msg=('sanjay', 10, 20.30, 'boss',70)
# print(msg[2], msg[4])

# tpl=(10,20,30,40,50)
# i=0
# while i<len(tpl):
#     print(tpl[i])
#     i+=1
# # for n in tpl:
# #     print(n)
# for index, n in enumerate(tpl):
#     print(index, n)

num1=num2=(10,20,30,40,50)
print(id(num1), type(num2))
print(isinstance(num1, tuple))
print(num1 is num2)
print(20 not in num1)