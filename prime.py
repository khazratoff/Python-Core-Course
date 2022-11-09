n = int(input("Type any number: "))
divisor = 2
is_prime = True
while divisor < n:
    if not n % divisor:
        is_prime = False
        break
    divisor+=divisor

ans = "Prime" if is_prime == True else "Not prime"
print(ans)