class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sort_nums = sorted(nums)
        output = []
        if len(nums) < 3:
            return output
        for i in reversed(range(3, len(sort_nums))):
            if sort_nums[i] == sort_nums[i-1] and sort_nums[i] == sort_nums[i-2] and sort_nums[i] == sort_nums[i-3]:
                sort_nums.pop(i)
        i = 0
        while i < len(sort_nums) - 2:
            j = i+1
            k = len(sort_nums) - 1
            while j < k:
                sum = sort_nums[i] + sort_nums[j] + sort_nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    output.append([sort_nums[i], sort_nums[j], sort_nums[k]])
                    val = sort_nums[j]
                    while j < len(sort_nums) and sort_nums[j] == val:
                        j += 1
                    k = len(sort_nums) - 1
            val = sort_nums[i]
            while i < len(sort_nums) and sort_nums[i] == val:
                i += 1
        return output


input1 = [-1,0,1,2,-1,-4]
input2 = [0,1,1]
input3 = [0,0,0]
print(Solution().threeSum(input1))
print(Solution().threeSum(input2))
print(Solution().threeSum(input3))
