class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # 1-> 1
        # 2-> 2
        # ...
        # 9-> 9
        # -----
        # 1-> 11
        # 2-> 22
        # ...
        # 9-> 99
        # -----
        # 10-> 101
        # 11-> 111
        # 12-> 121
        # ...
        # 99-> 999
        # -----
        # 10-> 1001
        # 11-> 1111
        # ...
        # 99-> 9999
        # -----

        # Pattern:
        #   - start: 10^((intLength + 1)/2 - 1)
        #   - end:   10^((intLength + 1)/2)

        ans = []

        start = 10**((intLength+1)//2-1)
        end = 10**((intLength+1)//2)
        max_rank = end - start + 1

        for rank in queries:
            # no such palindrome rank exists
            if rank >= max_rank:
                ans.append(-1)
                continue
            # get "first half" by rank
            first_half = str(int(start + rank - 1))
            # create full from "first half"
            # if even, just duplicate "first half"
            if intLength % 2 == 0:
                full_number = first_half + first_half[::-1]
            # if odd, maintain middle and duplicate "half before middle"
            else:
                full_number = first_half + first_half[:-1][::-1]
            ans.append(int(full_number))

        return ans
