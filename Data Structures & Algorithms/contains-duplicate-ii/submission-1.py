class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for r in range(len(nums)):
            if r - L > k:
                window.remove(nums[L])
                L += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False