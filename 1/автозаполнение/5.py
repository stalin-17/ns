import torch

t1=torch.rand(3,10,2,dtype=torch.float32)*12-2
t2=torch.randint(13,19,(123,),dtype=torch.int32)
t3=torch.normal(size=(8,1024),mean=23,std=50,dtype=torch.float32)

print(t1)
print(t2)
print(t3)
