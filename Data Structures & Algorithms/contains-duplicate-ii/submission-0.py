class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
        
        # Maintain window size: remove the element that fell out of bounds
            if len(window) > k:
                window.remove(nums[i - k])
            
        return False