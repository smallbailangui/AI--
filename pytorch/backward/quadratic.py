import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import matplotlib.pyplot as plt
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w1=torch.Tensor([1.0])
w1.requires_grad=True

w2=torch.Tensor([1.0])
w2.requires_grad=True

b=torch.Tensor([1.0])
b.requires_grad=True

# 二次函数的forward模型描述
def forward(x):
    return w1**x+w2*x+b

def loss(x,y):
    y_pred=forward(x)
    return (y_pred-y)**2

print("预测（训练前）:",4,forward(4).item())

#设置训练参数
learning_rate=0.1
epochs=1000
history=[]

for epoch in range(epochs):
    for x,y in zip(x_data,y_data):
        l=loss(x,y)
        l.backward()

        w1.data -= learning_rate * w1.grad.data
        w2.data -= learning_rate * w2.grad.data
        b.data -= learning_rate * b.grad.data

        w1.grad.zero_()
        w2.grad.zero_()
        b.grad.zero_()
    history.append(l.item())  # 记录每个epoch的损失



print("预测 (训练后):", 4, forward(4).item())
# 绘制损失曲线
plt.plot(range(epochs), history)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs Epoch (SGD)')
plt.show()