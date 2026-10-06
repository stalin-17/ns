import torch

value = int(input()) # переменную value в программе не менять

tr=torch.zeros(10,dtype=torch.int32)
tr[1::2]=value
print(tr)
