from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    l1 = []
    l1.extend(nums1)
    l1.extend(nums2)
    l1.sort()
    n = len(l1)
    if n % 2 == 0:
        n1 = l1[int(n/2) - 1]
        n2 = l1[int(n/2)]
        if n1 or n2:
            return (n1+n2)/2

        return 0

    else:
        return l1[int(n/2)]


if __name__ == "__main__":
    nums1 = [1, 3, 2]
    nums2 = [7, 6, 5]
    result = find_median_sorted_arrays(nums1, nums2)
    print(result)
