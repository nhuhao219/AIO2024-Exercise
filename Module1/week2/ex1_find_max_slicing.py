def find_max(num_list, k):
    length = len(num_list)
    result = []
    for i in range(length + 1 - k):
        slicing = num_list[i:i+k]
        result.append(max(slicing))
    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    result = find_max(num_list, k)
    print(result)
