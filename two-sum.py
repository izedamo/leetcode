def twoSum(nums, target):
        
        compliments = {}
        
        for idx in range(len(nums)):
            num = nums[idx]
            if(compliments.get(num) is not None):
                return [idx, compliments[num]]
            else:
                compliments[target - num] = idx

print(twoSum([2,7,11,15], 9))