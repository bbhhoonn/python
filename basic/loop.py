#while
a=1
while a<5:
    print('hello world', a)
    if a > 9:
        break
    a+=1
else:
    print('done')

#for

l=[1,2,3,4]
s={1,2,3,4,1,1}
d={'one':1, 'two':2}
ll=[(1,10),(2,20),(3,30)]
for i in l:
    print(i)
for i in s:
    print(i)
for i in d:
    print(i)
for i in range(10):
    print(i)
for i,j in ll:
    print(i,j)
    

for i in 'hello world':
    print(i)

for i in range(10):
    print(i)
    if i==5:
        break
else:
    print('done')

