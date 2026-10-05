import torch

t1=torch.arange(2,11, dtype=torch.float32)
t2=torch.arange(21,25,0.5,dtype=torch.float32).view(1,8)
t3=torch.arange(0,-2,-0.2,dtype=torch.float32).view(5,2)

print(t1)
print(t2)
print(t3)
