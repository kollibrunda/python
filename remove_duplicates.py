class Solution(object):
    def removeDuplicates(self, nums):
        """
""        :type nums: List[int]
        :rtype: int
        """""
        

        insert_pos = 1  # Start from index 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos
nums = [1,1,2]
k = Solution().removeDuplicates(nums)
print(k)          # Output: 2
print(nums[:k])   # Output: [1, 2]

