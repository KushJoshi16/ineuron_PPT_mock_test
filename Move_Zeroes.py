'''
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

'''


def moveZeroes(nums: list[int]) -> None:
    """
    Function to move all zero elements to the end while maintaining relative order
    """
    step = 0    # step will keep track of non zero elements encourntered so far

    for num in nums:
        if num != 0:    # if the element is non zero it will be sent to last known 0 position or to the start
            nums[step] = num
            step += 1   # once a non zero element is added we move on to next step

    while step < len(nums): # fills all the left positions with 0
        nums[step] = 0
        step += 1
    return None     

if __name__ == "__main__":

    array1 = [0,1,0,3,12]
    moveZeroes(array1)
    print(array1)

    array2 = [0]
    moveZeroes(array2)
    print(array2)