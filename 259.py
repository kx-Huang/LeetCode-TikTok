def threeSumSmaller(self, nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    for i in range(len(nums)):
        j, k = i+1, len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] < target:
                count += (k - j)
                j += 1
            else:
                k -= 1
    return count
