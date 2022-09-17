dictionary = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}

list1 = []
list2 = []
user_input = input('Some roman number: ')
roman = user_input.upper()
for letter in roman:
    list1.append(letter)
    list2.append(letter)

def check_order():


    
    for c in list2:
        size=len(list2)
        s=0
        for k in list2:
            if s <= dictionary.get(k):
                s = dictionary.get(k)
        max = list(dictionary.keys())[list(dictionary.values()).index(s)]
        max_index = list2.index(max)
        if max_index+1==size or max_index==0:
            if max_index==0:
                countMax=0
                for n in list2:
                    if n == max:
                        countMax+=1
                if (max == 'M' and countMax > 4) or ((max == 'X' or max == 'C' or max == 'I') and countMax > 3) or((max=='V' or max=='D' or max=='L') and countMax>1):
                    print("Out of limit")
                    return False
                    break
                list2.remove(max)
            elif max_index==1:
                if list2[max_index-1]=='V' or list2[max_index-1]=='L' or list2[max_index-1]=='D':
                    print("There cannot be V,L or D before max number(")
                    return False
                    break
                list2.remove(max)
                list2.remove(list2[max_index-1])
            else:
                print("There is more than a number before max number(")
                return False
                break
        else:
            if dictionary.get(list2[max_index-1])<=dictionary.get(list2[max_index+1]):
                print("Pre max number cannot be greater than after max number")
                return False
                break
            else:
                if max_index==0:

                    list2.remove(max)
                elif max_index==1:
                    if list2[max_index-1]=='V' or list2[max_index-1]=='L' or list2[max_index-1]=='D':
                        print("There cannot be V,L or D before max number(")
                        return False
                        break
                    list2.remove(max)
                    list2.remove(list2[max_index-1])
                else:
                    print("There is more than a number before max number(")
                    return False
                    break
    return True









def calculate():


    n=0
    sum = 0
    size = len(list1)
    for h in range(size):
        if size != n+1 and size != n:
            if dictionary.get(list1[n])<dictionary.get(list1[n+1]):
                sum=sum+(dictionary.get(list1[n+1])-dictionary.get(list1[n]))
                n=n+2  
            elif dictionary.get(list1[n])>=dictionary.get(list1[n+1]):  
                sum=sum+dictionary.get(list1[n])
                n=n+1

        if size == n+1: 
            sum=sum+dictionary.get(list1[n])
            n+=1
    print(sum)
    
if check_order():
    calculate()