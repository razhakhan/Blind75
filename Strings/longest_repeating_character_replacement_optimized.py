'''
In this approach we don't calculate max freq for every iteration, because theoritically it doesn't affect the result
This is O(N)
'''

#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        left = 0
        freq = {} # stores frequency of items in current window
        max_window_size = 1
        max_freq_of_any_item_noticed = 0
        
        for right in range(len(s)):
            
            # update count of each char
            item = s[right]
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
                
            #update the highest frequency value noticed till now since start
            max_freq_of_any_item_noticed = max(max_freq_of_any_item_noticed, freq[item])
            
            window_size = right-left+1
            
            # shrink window from left
            while window_size-max_freq_of_any_item_noticed>k:
                freq[s[left]]-=1
                left+=1
                window_size-=1
                
            max_window_size = max(max_window_size, window_size)
            
        return max_window_size


'''
For those who are struggling to understand the optimisation with maxf, here is how i understood it: 

For a substring to be valid, we need window_length - maxf <= k. Here, maxf is the frequency of the most common character in the current window. The difference window_length - maxf tells us how many characters we'd need to change to make the whole window the same character.

The biggest valid substring we can get is of size maxf + k. So, the larger maxf is, the better. If maxf doesn't change or goes down, our potential best answer doesn't change. We don't need to update maxf in this case.

On the other hand, if maxf goes up, it means we've found a character in the current window that appears more often than in previous windows. This means we might be able to get a longer valid substring, so we update maxf.

Hope this helps! And thank you neetcode for the wonderful video as always.
'''
            
