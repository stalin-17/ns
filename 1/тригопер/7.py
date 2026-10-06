import torch
lst = list(map(float, input().split()))
t_rect_lst = torch.tensor(lst, dtype=torch.int32).view(-1, 2)

t_sum_sq=(torch.sum(t_rect_lst[:,0])*torch.sum(t_rect_lst[:,1])).item()
t_min_per=(torch.min(torch.sum(t_rect_lst,axis=1))*2).item()
t_max_per=(torch.max(torch.sum(t_rect_lst,axis=1))*2).item()
print(t_rect_lst)
print(t_sum_sq)
print(t_min_per)
print(t_max_per)
