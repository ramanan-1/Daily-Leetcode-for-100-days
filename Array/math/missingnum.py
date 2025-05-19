class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        #Calculate the expected Sum
        expectedSum = n * (n+1)//2

        #intialize actualSum to 0
        actualSum = 0

        for num in nums :
            actualSum += num #calculate actualSUm

        return expectedSum-actualSum    


        