def minDeletionSize(strs):
    n = len(strs)        # number of rows
    m = len(strs[0])     # number of columns
    
    delete_count = 0
    
    for col in range(m):
        for row in range(n - 1):
            if strs[row][col] > strs[row + 1][col]:
                delete_count += 1
                break
    
    return delete_count
