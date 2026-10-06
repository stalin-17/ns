import torch

lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

t1 = torch.tensor(lst_1, dtype=torch.int32)
t2 = torch.tensor(lst_2, dtype=torch.int32)

t1[1:len(lst_2)+1]=t2[:]
print(t1)
