def f():
    print('1')
    print('2')
    return None
print('3')
print(f())

a=10
def aplus():
    global a # 피치 못하게 전역 변수 사용시 global
    a+=10
    return a
print(aplus())