def count_chars(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


if __name__ == "__main__":
    string = "smiles"
    counts = count_chars(string)
    print(counts)
