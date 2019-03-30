'''

Given an array nums of n integers, are there elements a, b, c 
in nums such that a + b + c = 0? Find all unique triplets in 
the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''

def ThreeSum(nums):
	result = []
  	nums.sort() 
    arr_size = len(nums)
    
    for i in range(0, arr_size-2): 
        if i > 0 and nums[i] == nums[i-1]: continue
        l = i + 1 
        r = arr_size-1 
        while (l < r): 
            temp = nums[i] + nums[l] + nums[r]
            temp_result = [nums[i], nums[l], nums[r]]
            if (temp == 0): 
                result.append(temp_result)
                while l < r and nums[l] == nums[l+1]: l = l + 1
                while l < r and nums[r] == nums[r-1]: r = r - 1
                l = l + 1
                r = r - 1
            elif (temp < 0): 
                l += 1
            else:
                r -= 1
    return [list(x) for x in set(tuple(x) for x in result)]  

