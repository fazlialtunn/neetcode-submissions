class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = 0
        count = 0

        for n in nums:
            if count == 0:
                val = n
            if n == val:
                count += 1
            else:
                count -= 1
        return val
