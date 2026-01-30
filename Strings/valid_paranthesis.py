class Solution:
    def isBalanced(self, s):
        # code here
        
        stack = []
        
        mappings = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        
        for i in s:
            if i not in mappings:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    last_item = stack.pop()
                    if mappings[i] != last_item:
                        return False
        if stack:
            return False
        else:
            return True


'''
4️⃣ The algorithm (step-by-step)

Create an empty stack

Traverse the string character by character

If it’s an opening bracket → push onto stack

If it’s a closing bracket:

Stack empty? ❌ → invalid

Pop top of stack

If types don’t match ❌ → invalid

After traversal:

Stack empty? ✅ balanced

Stack not empty ❌ unbalanced
'''
