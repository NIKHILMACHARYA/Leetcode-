class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxAvg = total/k
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i+k]
            maxAvg = max(maxAvg, total/k)
        return maxAvg