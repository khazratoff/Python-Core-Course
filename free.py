

def foo(nums: list[int]) -> list[int]:
    l1 = []
    for i in range(len(nums)):
        count = 1
        for j in range(len(nums)):
            if i!=j:
                count*=nums[j]
        l1.append(count)
    return l1
print(foo([1,2,3,4,4,5]))