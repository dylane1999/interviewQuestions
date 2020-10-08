class Solution:
    results = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Solution.results = []
        if(len(nums) < 3):
            return []
        for index in range(len(nums)):
            temp = nums.copy()
            target = temp.pop(index)
            Solution.twoSum(self, temp, target)

        final = []
        sortedResults = []
        for result in Solution.results:
            sortedItem = sorted(result)
            if(sortedItem not in sortedResults):
                sortedResults.append(sortedItem)
                final.append(result)


        return final





    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] + target == 0):
                    Solution.results.append((target, nums[j], nums[i]))

