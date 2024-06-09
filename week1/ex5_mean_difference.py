# MD_nRE 
def md_nre_single_sample(y, y_hat, n, p):
    Loss = (y**(1/n) - y_hat**(1/n))**p
    return Loss

if __name__ == "__main__":
    y = 100
    y_hat = 99.5
    n = 2
    p = 1
    Loss = md_nre_single_sample(y, y_hat, n, p)
    print("md_nre_single_sample: ", Loss)