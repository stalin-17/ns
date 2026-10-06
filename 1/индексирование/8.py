import torch

lst = list(map(int, input().split())) # список lst в программе не менять

tr=torch.tensor(lst,dtype=torch.int16)

t_pos=tr[tr>0]
print(t_pos)
