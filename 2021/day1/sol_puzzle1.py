nums = []
with open('input_puzzle1') as f:
    nums = [int(nums.rstrip()) for nums in f]

ans = len([(i,j) for i,j in zip(nums, nums[1:]) if j > i])

print(ans)