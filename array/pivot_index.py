import sys
from typing import List


def get_pivot_index(nums: List[int]) -> int:
    """
    Method returns pivot index;
        pivot_index - id of element where sum of elements on the left side
                      equals to sum on the right side
    :param nums: list of integers
    :return    : pivot index, otherwise -1
    """

    l_sum = 0
    r_sum = sum(nums[1:])

    if l_sum == r_sum:
        return 0

    for idx in range(1, len(nums)):
        l_sum += nums[idx - 1]
        r_sum -= nums[idx]

        if l_sum == r_sum:
            return idx

    return -1


if __name__ == '__main__':
    try:
        nums = [int(el) for el in input('Pass ints separated by space (" "):').split(' ')]
    except Exception:
        print('Pass ints separated by space!')
        sys.exit(-1)

    print('result: ', get_pivot_index(nums=nums))
