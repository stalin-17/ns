import torch
t_rnd = torch.randint(-3, 5, (100, ), dtype=torch.float32)

t_mean=torch.mean(t_rnd).item()
t_max=torch.max(t_rnd[:5]).item()
t_min=torch.min(t_rnd[-3:]).item()
print(t_mean.item())
