# evalue model by f1-score
def calculator_values(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return precision, recall, f1_score

if __name__ == "__main__":
    tp, fp, fn = 2, 3, 4.5

    if not isinstance(tp, int):
        raise ValueError("tp must be an int")
    
    if not isinstance(fp, int):
        raise ValueError("fp must be an int")
    
    if not isinstance(fn, int):
        raise ValueError("fn must be an int")

    if not (tp > 0 and fp > 0 and fn > 0):
        raise ValueError("tp and fp and fn must be greater than zero")

    precision, recall, f1_score = calculator_values(tp, fp, fn)

    print("precision is: ", precision)
    print("recall is: ", recall)
    print("f1_score is: ", f1_score)