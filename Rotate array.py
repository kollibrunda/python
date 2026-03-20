class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def rev(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1) 
nums = list(map(int, input("Enter your numbers: ").split(",")))
k = int(input("Enter your k: "))

solution = Solution()
solution.rotate(nums, k)
print(nums)