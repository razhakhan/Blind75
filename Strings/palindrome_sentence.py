class Solution:
	def isPalinSent(self, s):
		# code here
		left = 0
		right = len(s)-1
		while left<right:

		    while (left < right) and not (s[left].isdigit() or s[left].isalpha()):
                left+=1
            
		    while (left < right) and not (s[right].isdigit() or s[right].isalpha()):
                right-=1
            
            if (left < right) and s[left].lower()!=s[right].lower():
                return False

            left+=1
            right-=1
        return True
