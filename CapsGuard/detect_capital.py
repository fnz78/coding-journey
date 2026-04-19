def detectCapitalUse(word: str) -> bool:
    """
    Returns True if capital usage in the word is correct.
    Rules:
    1. All letters uppercase
    2. All letters lowercase
    3. Only first letter uppercase
    """
    return word.isupper() or word.islower() or word.istitle()


def main():
    print("🛡️ CapsGuard - Capital Usage Validator\n")
    
    word = input("Enter a word: ")
    
    if detectCapitalUse(word):
        print(" Valid capital usage!")
    else:
        print(" Invalid capital usage!")


if __name__ == "__main__":
    main()
