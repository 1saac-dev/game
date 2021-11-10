from random import randrange
n = randrange(1000)
while True:
    v = int(input())
    if n == v:
       print("!!!Winner!!!")
       break
    print('Try Smaller' if (n < v) else 'Try Bigger')
