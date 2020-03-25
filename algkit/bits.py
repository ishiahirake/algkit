def hamming_weight(n: int) -> int:
    """Calculate the number of '1' bit in the given it.

    :param int n:
    :return: number of '1' bit in the int
    """
    weight = 0
    while n != 0:
        weight += 1
        n &= n - 1
    return weight
