class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store elements and their indices
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_indices:

                # If it does, then return the indice of the 
                # current element and it's complement
                return [num_indices[complement], i]

            # If the complement doesn't exist, then add
            # the current element and it's index to the dictionary
            num_indices[num] = i

        # If no solution found return empty list
        return []
