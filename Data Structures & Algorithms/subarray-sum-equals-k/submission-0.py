class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix_sum=0
        count = 0
        for n in nums:
            prefix_sum+= n
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]   
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        return count
