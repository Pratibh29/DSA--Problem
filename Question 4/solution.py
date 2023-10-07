def max_subarray_sum(nums):
    """

    :param nums:

    """
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Take user input for the integer array
input_str = input("Enter the elements of the array separated by spaces: ")
nums = [int(x) for x in input_str.split()]

result = max_subarray_sum(nums)
print("Maximum subarray sum:", result)
