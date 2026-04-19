def count_substrings(s: str) -> int:
    """
    Count number of substrings containing only '1's.

    :param s: Binary string
    :return: Number of valid substrings
    """
    count = 0
    current = 0

    for char in s:
        if char == '1':
            current += 1
            count += current
        else:
            current = 0

    return count


# Run manually
if __name__ == "__main__":
    s = "0110111"
    print("Input:", s)
    print("Output:", count_substrings(s))
