import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

x_data=torch.Tensor([[1.0],[2.0],[3.0]])
y_data=torch.Tensor([[0],[0],[1]]) # 这里的y_data是二分类标签，0和1

class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel,self).__init__()
        self.linear=torch.nn.Linear(1,1)
    
    def forward(self,x):
        y_pred=F.sigmoid(self.linear(x))
        return y_pred
model=LogisticRegressionModel() 


criterion=torch.nn.BCELoss(reduction='sum')
optimizer=torch.optim.SGD(model.parameters(),lr=0.01)


for epoch in range(100):
    y_pred=model(x_data)
    loss=criterion(y_pred,y_data)
    print(epoch,loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()



x=np.linspace(0,10,200)
x_t=torch.Tensor(x).view((200,1))
y_t=model(x_t)
y=y_t.data.numpy()
plt.plot(x,y)
plt.plot([0,10],[0.5,0.5])
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()
plt.show()

