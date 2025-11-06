class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n= len(nums)
        res = []
        for i in range(1<<n):
            sub=[]
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            res.append(sub)
        return res
nums=input("enter your numbers:")
print(Solution().subsets(nums))