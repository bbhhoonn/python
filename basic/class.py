class Car(object):
    maxSpeed=200
    maxPeople=5
    def start(self):
        print('출발')
    def stop(self):
        print('정지')
    def __str__(self):
        print('hello world')
    def __init__(self):
        print('인스턴트 생성')

class Hybrid(Car):
    battery=1000
    batteryKM=300

k9=Car()
k5=Hybrid()
print(k9.maxPeople)
print(k5.maxPeople)
print(type(k9))
print(dir(k9))