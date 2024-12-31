class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = 0
        initialized = False
        closest_return = 0
        sort_nums = sorted(nums)
        if len(nums) < 4:
            sum = 0
            for i in range(len(nums)):
                sum += nums[i]
            return sum
        i = 0
        while i < len(sort_nums) - 2:
            j = i + 1
            k = len(sort_nums) - 1
            while j < k:
                sum = sort_nums[i] + sort_nums[j] + sort_nums[k]
                if not(initialized) or abs(sum - target) < closest:
                    initialized = True
                    closest = abs(sum - target)
                    closest_return = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    break
            i += 1
        return closest_return


input1 = [-1,2,1,-4]
input2 = [0,0,0]
input3 = [0,1,2]
input4 = [4,0,5,-5,3,3,0,-4,-5]
print(Solution().threeSumClosest(input1, 1))
print(Solution().threeSumClosest(input2, 1))
print(Solution().threeSumClosest(input3, 3))
print(Solution().threeSumClosest(input4, -2))
