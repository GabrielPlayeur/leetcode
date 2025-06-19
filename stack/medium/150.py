class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    result = b + a
                    stack.append(result)
                elif c == "-":
                    result = b - a
                    stack.append(result)
                elif c == "*":
                    result = a * b
                    stack.append(result)
                elif c == "/":
                    result = int(b / a)
                    stack.append(result)
            else:
                stack.append(int(c))
        return int(stack.pop())
