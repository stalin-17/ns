import torch

tr3d=torch.tensor(list(range(1,13))+list(range(10,130,10))+list(range(-1,-13,-1)),dtype=torch.int16).view(3,3,4)
print(tr3d)
tm=tr3d[1]
print(tm)

