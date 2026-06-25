class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - k
        
        while low < high:
            mid = (low + high) // 2
            
            # Compare the distance of arr[mid] and arr[mid + k] from x
            if x - arr[mid] > arr[mid + k] - x:
                # arr[mid + k] is closer to x than arr[mid], move window right
                low = mid + 1
            else:
                # arr[mid] is closer to x (or equal distance), move window left/stay
                high = mid
                
        # Return the contiguous window of size k starting at index 'low'
        return arr[low:low + k]