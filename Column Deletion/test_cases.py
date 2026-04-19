from solution import minDeletionSize


def run_tests():
    test_cases = [
        (["abc", "bce", "cae"], 1),
        (["a", "b"], 0),
        (["zyx", "wvu", "tsr"], 3),
        (["aaa", "aaa", "aaa"], 0),
        (["cba", "daf", "ghi"], 1)
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = minDeletionSize(input_data)
        assert result == expected, f"Test {i+1} Failed: Expected {expected}, got {result}"
        print(f"Test {i+1} Passed ")


if __name__ == "__main__":
    run_tests()
