import torch

tr=torch.arange(-10,9,2,dtype=torch.int32).view(5,2)
tr_t=tr.t()

print(tr)
print(tr_t)
