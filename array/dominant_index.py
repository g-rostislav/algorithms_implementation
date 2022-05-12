import sys
from typing import List


def get_dominant_index(nums: List[int]) -> int:
    """
    Method returns index of dominant element;
        dominant element - element that larger than others at least twice
    :param nums: list of integers (the largest number occurs only once)
    :return    : index of dominant element, otherwise -1
    """

    max_idx = 0
    max_num = nums[0]
    for idx, num in enumerate(nums[1:], start=1):
        if num > max_num:
            max_idx = idx
            max_num = num

    for idx, num in enumerate(nums):
        if abs(max_num / num) < 2 and idx != max_idx:
            return -1

    return max_idx


if __name__ == '__main__':
    try:
        nums = [int(el) for el in input('Pass ints separated by space (" "):').split(' ')]
    except Exception:
        print('Pass ints separated by space!')
        sys.exit(-1)

    print('result: ', get_dominant_index(nums=nums))

