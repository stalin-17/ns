import torch

lst = list(map(int, input().split())) # список lst в программе не менять

targets=torch.tensor(lst,dtype=torch.int32)
t_onehot=torch.zeros(len(targets),max(targets)+1,dtype=torch.int8)
for i in range(len(targets)):
    t_onehot[i,targets[i]]=1
print(t_onehot)
