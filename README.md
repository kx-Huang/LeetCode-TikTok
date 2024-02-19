# LeetCode Cheat Sheet for TikTok

## Problem List

### 2217: Kth Palindrome
- find pattern in half and build whole

### 666: Path Sum

- from top to bottom using: `dp[current] += dp[parent] + current_val`
- then find nodes with no child and sum them

### 210: Course Schedule II

- topology sort
- build graph and in_degree
- start from in_degree 0
- if queue, pop left queue to ans, loop neighbour, update in_degree (-1), if down to 0, add neighbour to queue
- return ans

### 621: Task Scheduler

- Group by most frequency task

### 694: Number of Distinct Island

- store list with coordinates which are related to the starting point representing an Island
- add island list to set and count

### 259: 3Sum Smaller

- Need O(n^2)
- sort the list, loop each number i,
- set j,k to the remaining smallest and largest
- do while j < k
- if good, than we know the count for fix i and k, make j+1 (try bigger)
- if no good, than make k-1 (try smaller)
