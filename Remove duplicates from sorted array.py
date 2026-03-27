class Solution(object):
    def removeDuplicates(self, nums):

        index = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                index+=1
        return index
nums = list(map(int, input("Enter your numbers: ").split(",")))

solution = Solution()
k = solution.removeDuplicates(nums)
print( nums[:k])