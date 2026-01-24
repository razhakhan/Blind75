class Solution:
    def singleDigit(self, n):
    # 	#code here 
        if n % 9 == 0:
            return 9
        else:
            return n % 9
            

        '''
        or use formula
        
        ans = 1+(n-1)%9
        this formula is called digital sum formula
        the ans here is digital sum
        
        Adding digits over and over is the same as asking:
        ‘What’s left if I keep removing groups of 9?’
        but modulo gives answers 0 to 9
        but answers are always  1 to 9
        “Repeated digit summation leads to the digital root, which can be computed in O(1) using modulo 9 because base-10 numbers preserve their remainder mod 9 under digit summation.”
        '''
