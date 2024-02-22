from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for t in time:
            num = t%60
            target1 = 60-num
            target2 = -num
            if target1 in count:
                ans += count[target1]
            elif target2 in count:
                ans += count[target2]
            count[num] += 1
        return ans