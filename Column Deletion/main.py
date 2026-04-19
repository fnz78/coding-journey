from solution import minDeletionSize

if __name__ == "__main__":
    strs = ["abc", "bce", "cae"]
    result = minDeletionSize(strs)
    
    print("Input:", strs)
    print("Columns to delete:", result)
