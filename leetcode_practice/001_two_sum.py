### SOLUTION 1
class Solution(object):
    def twoSum(self, nums, target):
            nums_index = [(v, index) for index, v in enumerate(nums)]
            nums_index.sort()
            begin = 0
            end = len(nums)-1
            while begin < end:
                current_value = nums_index[begin][0] + nums_index[end][0]
                if current_value == target:
                    return [nums_index[begin][1], nums_index[end][1]]
                elif current_value < target:
                    begin += 1
                else:
                    end -= 1
                    
            
solution = Solution()
print(solution.twoSum([2, 3, 3, 5, 6, 4, 5, 2], 4))


### SOLUTION 2 IMPROVED TIME COMPLEXITY
class Solution(object):
    def twoSum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                required[nums[i]]=i
solution = Solution()
print(solution.twoSum([2, 3, 3, 5, 6, 4, 5, 2], 4))



