class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        for i in range(len(nums1)):
            index = len(nums1) - i - 1
            if pointer1 < 0:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            elif pointer2 < 0 or nums1[pointer1] >= nums2[pointer2]:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
                