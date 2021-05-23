# list (변경 가능, 순서 있는 자료형)
l=[100,200,300,400]
print(l)
print(type(l))
print(l[1])
l[1]=1000
print(l)
print(dir(l))
l.append(300)
print(l)
l.extend([100,200,300])
print(l)
#l.clear
print(l.count(300))
l.pop()
print(l)
l.remove(100)
print(l)
l.reverse()
print(l)

#tuple (변경 불가, 순서 있는 자료형)
t=(l,1,2)
print(t)
print(type(t))
print(dir(t))
#t[0]=1000 -> error
l[0]=1
print(l)

#set (중복 허용x, 순서 없는 자료형
s={100,200,300,300,200}
print(s)
print(type(s))
print(dir(s))
s.add(500)
print(s)
print(set('abbcccddddeeeee'))

#dictionary (중복 허용x, 순서 없는 자료형 key:value)
d={'one':1, 'two':2}
print(d['one'])
print(type(d))
print(dir(d))
print(d.keys())
print(d.values())
print(d.items())
li=list(d.items())
print(li[0][1])
first_store={'apple':5000,'orange':10000}
second_store=first_store.copy()
first_store['orange']=20000
print(second_store)

