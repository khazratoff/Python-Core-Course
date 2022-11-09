number = int(input("Number: "))
init = 0
sum = 0
while init < number:
    if init % 2:
        continue
    sum = sum + init
    init = init + 1
print(sum)
