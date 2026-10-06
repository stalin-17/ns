import torch
lst = list(map(int, input().split()))

targets = torch.tensor(lst, dtype=torch.int64)
t_onehot = torch.eye(targets.max()+1)[targets]

t_bags=t_onehot.sum(dim=0)
pred=torch.argmax(t_bags).item()
print(t_bags)
print(pred)
