import math
user_input = int(input('some number: '))

square_root = math.sqrt(user_input)
n = 1
s = 0
if square_root == 1:
    print('1 is neither prime nor non-prime number')
else:
    while n <= square_root:
        if user_input % n == 0:
            s+=1
        n+=1

    if s > 1:
        print('This number is not prime')
    else:
        print('prime')