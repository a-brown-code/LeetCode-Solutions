class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in indices.keys():
                return [indices[pair], i]
            else:
                indices[num] = i
                