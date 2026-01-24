class Solution:
    def maxOnes(self, arr, k):
        # the question is actually : The length of the longest contiguous subarray that contains at most k zeroes
        left = 0
        right = 0
        zero_count=0
        max_len=0
        
        for right in range(len(arr)):
            if arr[right]==0:
                zero_count+=1
                
            while zero_count>k:
                if arr[left]==0:
                    zero_count-=1
                left+=1
            
            max_len = max(max_len, right-left+1)
            
        return max_len
