class validParentheses():
    def isVaid(self, s: str) -> bool:
        # balanced parenthesis in an expression 
        pchar = {"(":")", "{":"}", "[":"]"}
        stack=[]                                        # Initialize stack to store the checked parenthesis from string

        # Function to check parenthesis

        for parenthesis in s:
            if parenthesis in pchar:
                stack.append(parenthesis)
            elif len(stack)==0 or pchar[stack.pop()] != parenthesis:
                return False
        return len(stack)==0


print(validParentheses().isVaid("{}[()"))

# Refer https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-3.php 