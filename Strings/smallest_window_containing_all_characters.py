class Solution:
    def smallestWindow(self, s, p):
        # code here
        n = len(s)
        left=0
        right=n
        
        need = {}       # frequency counts of p
        window = {}     # frequency counts of characters in current window
        formed = 0
        
        # get frequency counts of p
        for char in p:
            if char not in need:
                need[char] = 1
            else:
                need[char] += 1
                
        required = len(need)
        
        min_window_len = 999999
        ans = ""
        
        for right in range(n):
            # update character counts of current window
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
                
            # if a char's char count in window matches char count in p
            if s[right] in need and window[s[right]]==need[s[right]]:
                formed += 1
            
            # shrink from left
            while left<=right and formed==required:
                
                curr_window_len = right-left+1
                # find min window
                if curr_window_len < min_window_len:
                    min_window_len = curr_window_len
                    ans = s[left:right+1]
                
                # update window char counts
                if s[left] in need:
                    window[s[left]] -= 1
                    
                # update formed count
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                
                left+=1
            
        return ans
            
            
'''

Optimized Idea

We need:

Window contains ALL chars of p

Including duplicates

So we track:

Need Map

Frequency required from p

Window Map

Frequency currently in window

Important Variable (THE KEY)

formed = number of chars whose required freq is satisfied
required = number of unique chars in p

Window valid when:

formed == required

Sliding Window Algorithm
Expand Right

Add char to window

If requirement satisfied → formed++
While window valid:

Try shrinking from left to minimize window

'''
            
            
            
            
            
