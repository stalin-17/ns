import torch

t1=torch.zeros(4,8,2, dtype=torch.int8)
t2=torch.ones(1,9, dtype=torch.int8)
t3=torch.eye(5,4, dtype=torch.int8)
t4=torch.full((2,7,1,5),5, dtype=torch.int8)
print(t1)
print(t2)
print(t3)
print(t4)
