import torch

lst = list(map(float, input().split())) # список в программе не менять

tr=torch.tensor(lst,dtype=torch.float32)
tr_2=tr[::2]

print(tr)
print(tr_2)
