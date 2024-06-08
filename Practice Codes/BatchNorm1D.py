import torch
import torch.nn as nn

batch_norm = nn.BatchNorm1d(3)
input_tensor = torch.randn(4, 10)
# input_tensor = torch.Tensor([[1,2,3],[4,5,6],[7,8,9]])
output_tensor = batch_norm(input_tensor)
print(input_tensor)
print(output_tensor)
