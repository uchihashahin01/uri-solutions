nums = [2,7,11,15]
target = 9

for nums_i in range(len(nums)):
    for nums_j in range(nums_i+1, len(nums)):
        if nums[nums_i] + nums[nums_j] == target:
            print([nums_i, nums_j])
            break
    else:
        continue
    break