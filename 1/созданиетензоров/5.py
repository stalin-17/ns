import torch

lst = list(map(int, input().split())) # список в программе не менять

t_indx=torch.tensor(lst,dtype=torch.int64).reshape(2,3)

print(t_indx)
