from typing import List


def mpp(n: int, arr: List[int]) -> int:

    """
    Method calculates the max pairwise product of arr x arr (complexity -> O(n))
    ! skipping itself multiplication (i != j)
    :param   n: len of array
    :param arr: list of positive integers
    :return   : max pairwise product
    """

    first_max = -1
    second_max = -1
    skip_idx = None

    for idx in range(n):
        if arr[idx] >= first_max:
            skip_idx = idx
            first_max = arr[idx]

    for idx in range(n):
        if arr[idx] >= second_max and idx != skip_idx:
            second_max = arr[idx]

    print(f'f -> {first_max}')
    print(f's -> {second_max}')

    return first_max * second_max


if __name__ == '__main__':
    n = int(input())
    arr = [int(el) for el in input().split(' ')]

    print(mpp(n, arr))

