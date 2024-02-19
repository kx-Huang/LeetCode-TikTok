from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # count each tasks
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        # get the highest task count
        highest_freq = max(count.values())

        # group different tasks in a group of n+1
        # put idle if no different task remaining
        # Note: we don't need to fill the last group as the tasks are done
        # e.g.     [A, A, A, B, B, B, C]  n = 2 (high = 3)
        # group 1: (A, B, C) ...
        # group 2: (A, B, /)
        # group 3: (A, B)

        # compute group 1 ~ "highest_freq-1"
        ans = (highest_freq - 1) * (n + 1)
        # compute group "highest_freq"
        for freq in count.values():
            if freq == highest_freq:
                ans += 1

        # if more tasks are given, it's always lenth of tasks with no idle time
        return max(len(tasks), ans)
