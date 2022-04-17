# Problem 53:
#     Combinatoric Selections
#
# Description:
#     There are exactly ten ways of selecting three from five, 12345:
#         123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#     In combinatorics, we use the notation, (5 choose 3) = 10.
#
#     In general, (n choose r) = n! / (r! * (n-r)!), where r ≤ n, n! = n × (n-1) × ... × 3 × 2 × 1, and 0! = 1.
#
#     It is not until n = 23, that a value exceeds one-million: (23 choose 10) = 1,144,066.
#
#     How many, not necessarily distinct, values of (n choose r) for 1 ≤ n ≤ 100, are greater than one-million?

from math import inf


def main():
    """
    Returns the number of non-distinct values of (n choose r) which are greater than one million.

    Returns:
        (int): Count of instances of (n choose r) greater than 1,000,000.
    """
    # Idea:
    #     Iterate through the increasing rows of Pascal's triangle.
    #     Can simply use values in current row to get next row.
    #     Also don't need the exact numbers once they exceed 10^6,
    #       so just replace with `inf` at that point.

    n = 0
    pascal_row = [1]  # Row for n = 0
    big_count = 0
    while n < 100:
        pascal_row = list(map(sum, zip([0]+pascal_row, pascal_row+[0])))
        for i in range(len(pascal_row)):
            x = pascal_row[i]
            if x == inf:
                big_count += 1
            elif x > 1000000:
                pascal_row[i] = inf
                big_count += 1
            else:
                continue
        n += 1
    return big_count


if __name__ == '__main__':
    big_combs_count = main()
    print('For 1 ≤ n ≤ 100 ...')
    print('Number of non-distinct values of (n choose r) which are greater than 1,000,000:')
    print('  {}'.format(big_combs_count))
