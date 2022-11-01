from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        valid = False
        for i in range(len(nums)):
            for k in range(len(nums)):
                for o in range(len(nums)):
                    if i<k and k<o:
                        if nums[i]<nums[k] and nums[k]<nums[o]:
                            valid = True
                            break
        return valid

o = Solution()
print(o.increasingTriplet([1,2,0,9,5,1]))
    


