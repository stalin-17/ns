import torch

lst = list(map(int, input().split())) # список lst в программе не менять

tr=torch.tensor(lst,dtype=torch.int16)
t_indx=tr[[1,1,2,1,0]]
print(t_indx)
