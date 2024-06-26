# LeetCode Cheat Sheet for TikTok

## Problem List

### 2217. Kth Palindrome

- find pattern in half and build whole

### 666. Path Sum

- from top to bottom using: `dp[current] += dp[parent] + current_val`
- then find nodes with no child and sum them

### 210. Course Schedule II

- topology sort
- build graph and in_degree
- start from in_degree 0
- if queue, pop left queue to ans, loop neighbour, update in_degree (-1), if down to 0, add neighbour to queue
- return ans

### 621. Task Scheduler

- Group by most frequency task

### 694. Number of Distinct Island

- store list with coordinates which are related to the starting point representing an Island
- add island list to set and count

### 259. 3Sum Smaller

- Need O(n^2)
- sort the list, loop each number i,
- set j,k to the remaining smallest and largest
- do while j < k
- if good, than we know the count for fix i and k, make j+1 (try bigger)
- if no good, than make k-1 (try smaller)

### 418. Sentence Screen Fitting

- construct 'word1_word2_word3_'
- maintain a pointer
- 3 cases: row ends with space ('_'), row ends with end of a word, row ends in middle of word

### 1530. Number of Goodf Leaf Nodes Pair

- `left/right = dfs(node)`
- `left/right = [1,2,3]`: each item represents their children's path length to them
- update sum with left and right information: if [1,2,3] and [4,5,6], distance = 6, then add 3 pairs (1+4, 2+4, 1+5)
- return [2,3,4]: each children path length+1 for upper level

### 2422. Merge Operations to Turn Array Into a Palindrome

- two pointer from leftmost and rightmost
- if not equal, sum and keep comparing unitl left meet right

### 1010. Pairs of Songs With Total Durations Divisible by 60

- two pointer (sum 0 or 60) but mod 60 version

### 1541. Minimum Insertions to Balance a Parentheses String

- keep track of left count (to represent a stack)
- if left, just add it to stack
- if right:
  - but no left in stack, add one left to stack and increase count
  - and left in stack, check next one (if exist):
    - if still is a right, pop stack (because one left matches two rights)
    - if not a right, increase one count and pop one left

### 2115. Find All Possible Recipes from Given Supplies

- topology sort but initalize queue to supplies only (not all in_degree 0 nodes)

### 856. Score of Parentheses

- use stack: `['(', 1, '(', 2]`
- match left and right and push score to stack for future compute

### 394. Decode String

- use stack: `['[', 'a', '[', 'c', 'd']`
- use another stack to keep track of number: `[2, 4]`
- expand when encounter a `]`, pop number stack as frequency: `cd` and `4` gives `cdcd`, put back to queue `['[', 'a', 'c', 'd', 'c', 'd']`

### 886. Possible Bipartition

- creat graph using neighbour (dislikes)
- union-find:
  - check self and neighbour have same parent (then invalid)
  - union neighbour with neighbour (random choice, say just neighbour[0])
- bfs:
  - color the graph with 0,1, use a list to keep track of the color (also served as "visited" list)
  - put neighbour in queue until all nodes are colored or encounter invalid (node and neighbour have same color)'

### 799. Champagne Tower

- method 1: `dp[i,j] = (dp[i-1,j-1] - 1) / 2 + (dp[i-1, j] - 1) / 2`
- method 2:
  - `dp[i+1, j] += (dp[i,j] - 1) / 2`
  - `dp[i+1, j+1] += (dp[i,j] - 1) / 2`
