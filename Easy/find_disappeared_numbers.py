class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(range(1, n + 1))
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)

        return list(nums_set)
