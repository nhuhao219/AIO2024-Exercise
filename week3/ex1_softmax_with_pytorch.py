import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


# test Softmax
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output1 = softmax.forward(data)
print(f"Softmax value: {output1}")

# test softmax stable
soft_stable = StableSoftmax()
output2 = soft_stable.forward(data)
print(f"Softmax stable value: {output2}")
