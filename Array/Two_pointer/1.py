class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Initialize a hash map to store value:index pairs
        seen = {}

        # # Iterate through the list with index and value
        for idx, num in enumerate(nums):
            # # Calculate the complement that would sum up to the target
            complement = target - num

            # # Check if the complement has already been seen
            if complement in seen:
                # # If found, return the indices of the complement and current number
                return [seen[complement], idx]

            # # Store the current number and its index in the hash map
            seen[num] = idx