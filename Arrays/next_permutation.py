class Solution:
    def nextPermutation(self, arr):
        pivot = -1
        right_pointer = len(arr)-1
        
        while(right_pointer>0):
            if(arr[right_pointer-1]<arr[right_pointer]):
                pivot = right_pointer-1
                break
            right_pointer-=1

        # to pass the case like [2, 3, 1] we need pivot as -1
        if pivot==-1:
            arr[:]=arr[::-1]
            return arr
            # (remember, writing just arr = arr[::-1] won't work because it is not in place modification)
        else:
            right_pointer = len(arr)-1
            
            while(right_pointer>0):
                if arr[right_pointer]>arr[pivot]:
                    break
                right_pointer-=1
                
            smallest_element_greater_than_pivot = right_pointer
            
            arr[pivot], arr[smallest_element_greater_than_pivot] = arr[smallest_element_greater_than_pivot], arr[pivot]
            
            arr[pivot+1:] = arr[pivot+1:][::-1]
            
            return arr
