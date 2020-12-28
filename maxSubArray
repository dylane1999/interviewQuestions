from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArray = []
        for i in range(len(nums)):
            remainingNums = nums[i:]
            for j in range(len(remainingNums)):
                subArray.append(remainingNums[0:j+1])

        max = sum(subArray[0])
        for array in subArray:
            arraySum = sum(array)
            if (arraySum > max):
                max = arraySum


        return max
