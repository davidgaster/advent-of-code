nums = []
with open('input_puzzle1') as f:
    nums = [int(nums.rstrip()) for nums in f]

sums = [a+b+c for a,b,c in zip(nums, nums[1:], nums[2:])]
ans = len( [(i,j) for i,j in zip(sums, sums[1:]) if j > i] )
print(ans)