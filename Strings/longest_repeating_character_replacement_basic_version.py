# O(26*n)

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        left = 0
        freq = {} # stores frequency of items in current window
        max_window_size = 1
        
        for right in range(len(s)):
            
            # update count of each char
            item = s[right]
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
                
            #find the highest frequency value in the dictionary
            max_frequency_value = max(freq.values())
            
            window_size = right-left+1
            
            # shrink window from left
            while window_size-max_frequency_value>k:
                freq[s[left]]-=1
                # optional : you can delete item in freq if freq is 0 because it is no longer a char in the window
                left+=1
                window_size-=1
                # recompute max frequency item for current new window
                max_frequency_value = max(freq.values())
                
            max_window_size = max(max_window_size, window_size)
            
        return max_window_size

'''
You’re allowed to:

Take any substring
Change at most k characters
So that all characters in that substring become the same

You need:
The maximum possible length of such a substring

Key rephrase (THIS unlocks it):

Find the longest substring where
(window length − count of most frequent character) ≤ k
That sentence is the whole problem.
'''
            
            
            
