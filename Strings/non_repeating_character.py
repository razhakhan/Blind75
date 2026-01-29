class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for i in s:
            if i in freq:
                if freq[i] == 1:
                    return i
        
        return '$'
