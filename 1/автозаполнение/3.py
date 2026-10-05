import torch

t1=torch.linspace(3,7,2,dtype=torch.float32)
t2=torch.linspace(9,-9,10,dtype=torch.float32)
t3=torch.linspace(5,-5,5,dtype=torch.float32).view(5,1)

print(t1)
print(t2)
print(t3)
