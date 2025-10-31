class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start^goal
        res = bin(ans).count("1")
        return res
start = int(input("Enter a number: "))
goal = int(input("Enter your goal:"))
solution = Solution()
print(solution.minBitFlips(start,goal))
