import torch

lst = list(map(int, input().split())) # список lst в программе не менять

tr3d=torch.tensor(lst,dtype=torch.int16).view(3,3,4)

t_res=tr3d[...,1].permute(dims=(1,0))
print(t_res)
