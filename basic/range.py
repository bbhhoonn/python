print(type(range(10)))
print(1,list(range(10)))
print(2,list(range(5,10)))
print(3,list(range(2,10,2)))
print(4,list(range(10,5,-1)))
print(5,list(range(-10)))


# l=[]
# for i in range(10):
#     l.append(i)
# print(l)

l=[i for i in range(10)]
print(l)

#구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print('{} × {} = {}'.format(i,j,i/j))
ll=['{} × {} = {}'.format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
print(ll)

for i,j in enumerate(range(100,1000,100),1):
    print(i,j)