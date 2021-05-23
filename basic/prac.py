#%%
print(type(0))
print(type(2.2))    
print(type('hello world!'))
print(type(0b1001))
print(type(2+3j))

help(0)
print(dir('hello world'))

#string
a='hello world'
print(a[0])
print(a[0:5]) #before the last one
print(a[6:11])
print(a[::2])
print(a[::-1])
print(a[10:5:-1])
print(a[-1])

b='   Too much !'
c=b.strip()
print(c.lower())
print(c.upper())
print(c.count('o'))
d=c.split(' ')
print('@'.join(d))


# %%
