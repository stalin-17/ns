import torch
lst = list(map(float, input().split()))
t_box_lst = torch.tensor(lst, dtype=torch.int32).view(-1, 3)

t_mean_vol=torch.mean(torch.prod(t_box_lst,dim=1).float()).item()
t_min_vol=torch.min(t_box_lst[torch.prod(t_box_lst,dim=1)>t_mean_vol]).item()
t_max_vol=torch.max(t_box_lst[torch.prod(t_box_lst,dim=1)<t_mean_vol]).item()
