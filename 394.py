from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        stack = []
        ans = ''
        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                num_str = int(c)
                while i < len(s)-1 and s[i+1].isnumeric():
                    num_str = num_str * 10 + int(s[i+1])
                    i += 1
                num.append(num_str)
            elif c == '[':
                stack.append('[')
            elif c.isalpha():
                if stack and stack[-1].isalpha():
                    stack[-1] += c
                else:
                    stack.append(c)
            elif c == ']':
                tmp = deque([])
                while stack and stack[-1] != '[':
                    tmp.appendleft(stack.pop())
                stack.pop()
                stack += (list(tmp) * num.pop())
            i += 1

        return ''.join(stack)
