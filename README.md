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

### 418: Sentence Screen Fitting

- construct 'word1_word2_word3_'
- maintain a pointer
- 3 cases: row ends with space ('_'), row ends with end of a word, row ends in middle of word

### 1530: Number of Goodf Leaf Nodes Pair

- `left/right = dfs(node)`
- `left/right = [1,2,3]`: each item represents their children's path length to them
- update sum with left and right information: if [1,2,3] and [4,5,6], distance = 6, then add 3 pairs (1+4, 2+4, 1+5)
- return [2,3,4]: each children path length+1 for upper level

### 2422: Merge Operations to Turn Array Into a Palindrome

- two pointer from leftmost and rightmost
- if not equal, sum and keep comparing unitl left meet right

#### 1010: Pairs of Songs With Total Durations Divisible by 60

- two pointer (sum 0 or 60) but mod 60 version