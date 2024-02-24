class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def merge_score(stack, score):
            while stack and stack[-1] != '(':
                val = stack.pop()
                score += val
            return score

        stack = []
        ans = 0
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                # case: x x x (
                if stack[-1] == '(':
                    stack.pop()
                    score = merge_score(stack, 1)
                    stack.append(score)
                # case: x x x ( x
                else:
                    score = stack.pop() * 2
                    stack.pop()
                    score = merge_score(stack, score)
                    stack.append(score)
        return stack[-1]
