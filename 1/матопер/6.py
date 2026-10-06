import torch

current_tm = int(input()) # переменную current_tm в программе не менять

lst=[current_tm,current_tm//60//60,current_tm//60%60,current_tm%60]
t_time=torch.tensor(lst,dtype=torch.int32)

