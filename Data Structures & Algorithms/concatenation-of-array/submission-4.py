class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        
        for n in list(nums):
            nums.append(n)
        return nums