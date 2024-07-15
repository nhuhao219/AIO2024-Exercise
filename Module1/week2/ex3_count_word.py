def count_word(file_path):
    dic = {}
    with open(file_path, "r") as file:
        data = file.read()
    words = data.split()
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


if __name__ == "__main__":
    file_path = "data.txt"
    result = count_word(file_path)
    assert result ["who"] == 3
    print(result["man"])
