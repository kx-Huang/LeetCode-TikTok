from collections import defaultdict

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            depth, pos = num//100, (num//10) % 10
            val = num % 10
            dic[depth, pos] += dic[depth-1, (pos+1)//2] + val
        res = 0
        for depth, pos in dic.keys():
            if (depth+1, pos*2-1) not in dic and (depth+1, pos*2) not in dic:
                res += dic[depth, pos]
        return res
