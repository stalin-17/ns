import torch

lst = list(map(int, input().split())) # список lst в программе не менять

tr=torch.tensor(lst,dtype=torch.int16)
t_res=tr[(tr>=-2) & (tr<=2)]
print(t_res)
