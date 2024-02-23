class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        left = 0 # left stack count
        i = 0
        while (i < len(s)):
            c = s[i]
            if c == '(':
                left += 1
            elif c == ')':
                # if no left, add left to stack and continue
                if left == 0:
                    ans += 1
                    left += 1
                # if right comes in pair, remove left from stack
                if i < len(s) - 1 and s[i+1] == ')':
                    i += 1
                    left -= 1
                # else if not comes in pair, add right to match left and decrease left in stack
                else:
                    ans += 1
                    left -= 1
            i += 1
        # match remaining left with double right
        ans += (left * 2)
        return ans
