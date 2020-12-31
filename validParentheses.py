class Solution:
    def isValid(self, message: str) -> bool:
        # possibleValues = dict([('(', 0), (')', 0), ]) use of dict constructor
        mappedValues = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for char in message:
            if char in mappedValues and len(stack) > 0 and mappedValues[char] == stack[-1]:
                stack.pop()
            elif char in mappedValues.values():
                stack.append(char)
            else:
                return False


        if len(stack) == 0:
            return True
