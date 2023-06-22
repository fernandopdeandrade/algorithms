# nums1 = [1, 3, 4, 2, 2]
# nums2 = [3, 1, 3, 4, 2]
# nums3 = [1, 1]
# nums4 = [1, 1, 2]
# nuns5 = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# nums_test_error = [1, 2]


def find_duplicate(nums: list[int]) -> int or bool:
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] >= 0:
            return nums[i]

    return False


# print(find_duplicate(nums1))
# print(find_duplicate(nums2))
# print(find_duplicate(nums3))
# print(find_duplicate(nums4))
# print(find_duplicate(nuns5))
# print(find_duplicate(nums_test_error))
