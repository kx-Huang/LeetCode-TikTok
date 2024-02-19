# LeetCode-TikTok

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
