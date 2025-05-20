class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0 #position where the next non-zero value should be placed

        for idx in range(len(nums)):

            if nums[idx] != 0 :
                nums[l],nums[idx] = nums[idx],nums[l]
                l += 1


        #Tc = o(n)
        #Sc = o(1)        
                




        