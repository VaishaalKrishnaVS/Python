class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []


ans = Solution()
lis = ans.twoSum(input(),int(input()))
print(lis)