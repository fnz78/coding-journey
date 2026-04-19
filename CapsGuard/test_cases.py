from detect_capital import detectCapitalUse


def run_tests():
    test_words = {
        "USA": True,
        "hello": True,
        "Google": True,
        "FlaG": False,
        "python": True,
        "PYTHON": True,
        "PyThOn": False
    }

    print("Running Test Cases...\n")

    for word, expected in test_words.items():
        result = detectCapitalUse(word)
        status = "PASS" if result == expected else "FAIL"
        print(f"{word:10} | Expected: {expected} | Got: {result} | {status}")


if __name__ == "__main__":
    run_tests()
