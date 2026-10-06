import torch

# списки в программе не менять
lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

tr_1=torch.tensor(lst_1,dtype=torch.int32)
tr_2=torch.tensor(lst_2,dtype=torch.int32)
len1=min(len(tr_1),len(tr_2))
tr_1=tr_1[:len1]**tr_2[:len1]
