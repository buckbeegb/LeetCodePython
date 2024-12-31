class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[int]:
        sort_nums = sorted(nums)
        output = []
        if len(nums) < 4:
            return output
        for i in reversed(range(4, len(sort_nums))):
            if sort_nums[i] == sort_nums[i-1] and sort_nums[i] == sort_nums[i-2] and sort_nums[i] == sort_nums[i-3] and sort_nums[i] == sort_nums[i-4]:
                sort_nums.pop(i)
        h = 0
        while h < len(sort_nums) - 3:
            i = h + 1
            while i < len(sort_nums) - 2:
                j = i+1
                k = len(sort_nums) - 1
                while j < k:
                    sum = sort_nums[h] + sort_nums[i] + sort_nums[j] + sort_nums[k]
                    if sum < target:
                        j += 1
                    elif sum > target:
                        k -= 1
                    else:
                        output.append([sort_nums[h], sort_nums[i], sort_nums[j], sort_nums[k]])
                        val = sort_nums[j]
                        while j < len(sort_nums) and sort_nums[j] == val:
                            j += 1
                        k = len(sort_nums) - 1
                val = sort_nums[i]
                while i < len(sort_nums) and sort_nums[i] == val:
                    i += 1
            val = sort_nums[h]
            while h < len(sort_nums) and sort_nums[h] == val:
                h += 1
        return output


input1 = [1,0,-1,0,-2,2]
input1a = 0
input2 = [2,2,2,2,2]
input2a = 8
print(Solution().fourSum(input1, input1a))
print(Solution().fourSum(input2, input2a))
