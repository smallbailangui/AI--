import torch 
criterion =torch.nn.CrossEntropyLoss()

# TODO:注意，这里一定是LongTensor，约定俗成吗?,后续有待了解
Y=torch.LongTensor([2,0,1])  
Y_pred1 = torch.Tensor([[0.1,0.2,0.9],
                       [1.1,0.1,0.2],
                       [0.2,2.1,0.1]])

Y_pred2 = torch.Tensor([[0.8,0.2,0.3],
                       [0.2,0.3,0.5],
                       [0.2,0.2,0.5]])

l1=criterion(Y_pred1,Y)
l2=criterion(Y_pred2,Y)
print("batch Loss1 = ",l1.data, "\nbatch Loss2 = " ,l2.data)