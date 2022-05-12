import sys
from typing import List


def plus_one(nums: List[int]) -> List[int]:
    """
    Method returns array represented integer as arr_to_int(nums) + 1
    :param nums: int represented by array
        ex. nums=[1,2,3] represents integer=123
    :return    : represented by (int from array + 1) as array
        ex. integer = 123+1 = 124 -> return [1,2,4]
    """

    str_int = ''
    for digit in nums:
        str_int += str(digit)

    acc = 1
    plus_one_nums = []

    for digit in nums[-1::-1]:
        if digit + acc >= 10:
            plus_one_nums.insert(0, 0)
        else:
            plus_one_nums.insert(0, digit + acc)
            acc = 0

    if acc != 0:
        plus_one_nums.insert(0, 1)

    return plus_one_nums


if __name__ == '__main__':
    try:
        nums = [int(el) for el in input('Pass ints separated by space (" "):').split(' ')]
    except Exception:
        print('Pass ints separated by space!')
        sys.exit(-1)

    print('result: ', plus_one(nums=nums))

