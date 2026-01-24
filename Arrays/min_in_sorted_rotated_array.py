#User function Template for python3

class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr)-1
        
        while low<high:
            mid = (low + high)//2
            
            if arr[mid]<arr[high]:
                high = mid
            
            else:
                low = mid+1
      
        return arr[low]  # we return arr [low] not arr [mid]
        
        
'''
Compare mid with end — sorted side is useless.

The BIG question to ask at mid

At any mid, ask:

Which side is already sorted?

This tells you where the minimum cannot be.

'''
