import torch
# переменные lst и t_videos в программе не менять
lst = list(map(int, input().split()))
t_videos = torch.tensor(lst, dtype=torch.int32)

t_median=t_videos.median().item()
t_mean=t_videos.float().mean().item()
t_disp=t_videos.float().var().item()
t_low_count=torch.sum[t_videos(t_videos<t_median]).item()
t_hi_count=torch.sum(t_videos[t_videos>t_median]).item()
