class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in seen:
                return [seen[answer], i]
            seen[nums[i]] = i
