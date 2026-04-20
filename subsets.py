class Solution(object):
    def subsets(self, nums):
        n= len(nums)
        res = []
        for i in range(1<<n):
            sub=[]
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            res.append(sub)
        return res
nums = list(map(int, input("Enter your numbers: ").split()))
solution=Solution()
print(solution.subsets(nums))
