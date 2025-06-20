import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
# 这么设置是因为出现了虚拟环境的问题，导致 PyTorch 在使用多线程时出现了重复的库加载错误。
# 这行代码允许 PyTorch 在多线程环境中加载重复的库，从而避免错误。
import torch
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad = True

def forward(x):
    return x * w

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print("predict (before training):", 4, forward(4).item())
l_list = []
for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        # 调用 backward() 计算梯度
        l.backward()
        print("\tgrad: ", x, y, w.grad.item())
        w.data = w.data - 0.01 * w.grad.data
        # 清除梯度
        w.grad.zero_()
    # 打印当前的损失值
    # 注意：这里的 l 是一个标量，所以可以直接使用 item() 方法获取
    print("progress:", epoch, l.item())
    l_list.append(l.item())

print("predict (after training):", 4, forward(4).item())
# 绘制 cost 曲线
plt.plot(range(100), l_list)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.title('Cost vs Epoch (SGD)')
plt.show()