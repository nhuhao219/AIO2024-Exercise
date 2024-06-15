def compute_levenshtein(source, target):
    m = len(source) + 1
    n = len(target) + 1
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + (1 if source[i - 1] != target[j - 1] else 0))
                
    result = matrix[m - 1][n - 1]
    return result

if __name__ == "__main__":
    source = "kitten"
    target = "sitting"
    result = compute_levenshtein(source, target)
    print(result)