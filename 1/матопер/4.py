import torch

lst = list(map(float, input().split())) # список lst в программе не менять

t_mask=torch.tensor([1,-1]*8)
tr=torch.tensor(lst,dtype=torch.float32)
tr[:16]*=t_mask
print(tr)
