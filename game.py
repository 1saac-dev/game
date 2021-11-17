from random import randrange
n = randrange(500)
while True:   
    v = int(input())
    if n == v:
       print("!!!!!!YOU WON!!!!!!!")
       break
    print('Try Smaller, Please' if (n < v) else 'Try Bigger, Please')