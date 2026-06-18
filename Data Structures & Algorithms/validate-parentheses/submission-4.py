class Solution:
        def isValid(self, s: str) -> bool:
            stack = []

            if not s:
                return False

            for char in s:

                if char in '({[':
                    stack.append(char)

                
                if stack:
                    #pop = stack.pop()
                    if char == ')' and stack.pop() != '(':
                        return False

                    if char == ']' and stack.pop() != '[':
                        return False

                    if char == '}' and stack.pop() != '{':
                        return False
                else:
                    return False
            
            return len(stack) == 0