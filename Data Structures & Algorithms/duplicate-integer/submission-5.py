class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeSet = set()
        dupeSet.update(nums)

        if (len(dupeSet) == len(nums)):
            return False
        else:
            return True

        