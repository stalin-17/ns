import torch

tr=torch.empty(32,dtype=torch.int32)
tr[0]=-1;tr[-1]=-1
print(tr)
