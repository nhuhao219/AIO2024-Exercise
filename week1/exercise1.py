# evalue model by f1-score
def calculator_values(tp, fp, fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    return precision, recall, f1_score

# nhap vao cac gia tri tp, fp, fn
# tp, fp, fn = input("Nhap vao 3 gia tri tp, fp, fn cach nhau dau cach:").split()
tp, fp, fn = map(int, input("Nhập vào 3 giá trị tp, fp, fn cách nhau bởi dấu cách: ").split())
if not type(tp)==int:
    ValueError("tp must be int")
if not type(fp)==int:
    ValueError("fp must be int")
if not type(fn)==int:
    ValueError("fn must be int")

if not (tp>0 and fp>0 and fn>0):
    ValueError("tp and fp and fn must be greater than zero")

precision, recall, f1_score = calculator_values(tp, fp, fn)
print("precision is: ", precision)
print("recall is: ", recall)
print("f1_score is: ", f1_score)