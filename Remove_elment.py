from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for c in range(len(nums)):
            if val in nums:
                nums.remove(val)
        ans = len(nums)
        return ans