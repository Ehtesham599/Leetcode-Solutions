class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        res = []
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in my_map:
                return [my_map[comp], i]
            else:
                my_map[nums[i]] = i
