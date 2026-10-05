import torch

t1 = torch.empty(3, 2, 10).fill_(5)
t2 = torch.empty(1, 10, 1, 7, 1).fill_(-1)

t1.unsqueeze_(dim=0)
t2=torch.squeeze(t2)

print(t1.size())
print(t2.size())
