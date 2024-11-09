class Solution:
    def isValid(self, s: str) -> bool:
        store = {"(": ")", "[": "]", "{": "}", ")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            reversedChar = store[char]
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            elif char == ")" or char == "}" or char == "]":
                if len(stack) != 0 and stack[-1] == reversedChar: 
                    stack.pop()
                else: return False

        return len(stack) == 0
