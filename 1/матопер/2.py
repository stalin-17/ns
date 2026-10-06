import torch

lst = list(map(int, input().split())) # список lst в программе не менять

tr=torch.tensor(lst,dtype=torch.float32)
tr_res=tr[tr>5]%2
print(tr)
print(tr_res)
