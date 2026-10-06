import torch

t_out = torch.randn(10, dtype=torch.float32) * 10 - 5 # тензор t_out в программе не менять

def softmax(t):
    return torch.exp(t)/torch.sum(torch.exp(t))

t_pred=softmax(t_out)
t_indx_min=torch.argmin(t_pred).item()

