'''
1.准备数据集
2.定义模型
3.定义损失函数与优化器--->调用pytorch的api
4.训练模型
'''
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


import torch
import matplotlib.pyplot as plt
x_data=torch.Tensor([[1.0],[2.0],[3.0],[4.0],[5.0]]) # 输入数据
y_data=torch.Tensor([[2.0],[4.0],[6.0],[8.0],[10.0]]) # 输出数据

# nn 代表神经网络（Neural Network）# nn.Linear 是一个线性层，通常用于线性回归或线性变换
# nn.Linear 的输入参数是输入特征的维度和输出特征的维度
# 在这里，我们定义了一个线性模型，它有一个输入特征和一个输出特征
# 这里的特征维度指的是每个样本的特征数量
class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear=torch.nn.Linear(1,1) # class nn.Linear 包含两个参数：输入特征的维度和输出特征的维度
        
        '''
        阅读linear的文档 了解weight和bias在实际使用的大小和操作
        
        Examples::
        >>> m = nn.Linear(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
        '''

    def forward(self,x):
        y_pred=self.linear(x)
        return y_pred
    
model=LinearModel()


criterion=torch.nn.MSELoss(reduction='sum') # 定义损失函数，这里使用均方误差损失函数（Mean Squared Error Loss），reduction='sum'表示对所有样本的损失求和
# 这里使用的优化器是随机梯度下降（SGD），学习率为0.01
# 使用其他的优化器定向输出至文本中查看结果
optimizer=torch.optim.SGD(model.parameters(),lr=0.01) # 使用随机梯度下降优化器，学习率为0.01

history = [] # 用于存储每个epoch的损失值
for epoch in range(100):
    y_pred=model(x_data)
    loss=criterion(y_pred,y_data) # 计算损失函数，这里使用均方误差损失函数
    print(epoch,loss.item())

    optimizer.zero_grad()
    loss.backward() # 反向传播，计算梯度
    optimizer.step() # 更新参数

    history.append(loss.item()) # 记录损失值

print('w=',model.linear.weight.item())
print('b=',model.linear.bias.item())

x_test=torch.Tensor([[4.0]])
y_test=model(x_test)
print('y_pred = ',y_test.data)

plt.plot(range(100),history)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Loss vs Epoch")
plt.grid()
plt.show()