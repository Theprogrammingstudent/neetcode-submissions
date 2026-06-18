class Solution:
        def isValid(self, s: str) -> bool:
            stack = []
            brackets = {')':'(', ']':'[', '}':'{'}

            for char in s:

                if char in '({[':
                    stack.append(char)
                
                else:
                    if not stack or stack.pop() != brackets[char]:
                        return False
            
            #return len(stack) == 0
            return not stack