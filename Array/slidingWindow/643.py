
def findMaxAverage(nums,k) :

    #preCalculation
    window_sum = sum(nums[:k])

    max_sum = window_sum 

    for i in range(k,len(nums)):

        window_sum += nums[i] - nums[i-k] 

        #evaluate
        max_sum = max(window_sum,max_sum)

    return max_sum/k



        