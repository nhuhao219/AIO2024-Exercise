# regression loss function
import random

def loss_function(num_samples, loss_name):
    if loss_name == "MAE":
        sum = 0
        for i in range(num_samples):
            target, pred = module_random()
            loss = abs(pred - target)
            print("loss name : {}, sample : {}, pred : {}, target : {}, loss : {}".format(loss_name, i, pred, target, loss))
            sum =+ loss
        Loss_MAE = sum / num_samples
        return f"final {loss_name}: {Loss_MAE}"
    
    if loss_name == "MSE":
        sum = 0
        for i in range(num_samples):
            target, pred = module_random()
            loss = (pred - target) * (pred - target)
            print("loss name : {}, sample : {}, pred : {}, target : {}, loss : {}".format(loss_name, i, pred, target, loss))
            sum =+ loss
        Loss_MSE = sum / num_samples
        return f"final {loss_name}: {Loss_MSE}"
        
def module_random():
    y_target = random.uniform(0, 10)
    y_predict = random.uniform(0, 10)
    return y_target, y_predict

if __name__ == "__main__":
    num_samples = input("Input number of samples (integer number) which are generated: ")
    
    if num_samples.isnumeric():
        if not "." in num_samples:
            num_samples = int(num_samples)
            loss_name = input("Input loss name(MAE or MSE):")
            L = loss_function(num_samples, loss_name)
            print(L)
        else:
            raise ValueError("number of samples must be an integer number")
    else:
        raise ValueError("number of samples must be an integer number")
