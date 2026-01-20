class Solution:
    def maxSubarraySum(self, arr):
        curr_sum = 0
        max_sum = -99999
        for i in arr:
            curr_sum = max(i, curr_sum+i) # 
            max_sum = max(curr_sum, max_sum)
        return max_sum

'''
Once curr_sum becomes negative:

It will only reduce future sums

Carrying it forward is pointless

That's why we pick max( current item , current item + prefix sum )

'''
