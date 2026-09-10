class ValidParentheses:
    def isValid(self, s: str) -> bool:
        # Dictionary to store matching brackets
        brackets = {')': '(', '}': '{', ']': '['}

        # Stack to keep the track of opening brackets
        stack = []

        # Iterate through each character in the String
        for char in s:
            # If it's closing parentheses
            if char in brackets:
                # Check if stack is empty or stack's top doesn't match
                if not stack or stack[-1] != brackets[char]:
                    return False
                # Pop the matching opening bracket
                stack.pop()
            else:
                # Push the opening bracket onto stack
                stack.append(char)
        # Return True if stack is empty, otherwise False
        return len(stack) == 0
      
