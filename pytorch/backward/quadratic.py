# import os
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# import torch
# import matplotlib.pyplot as plt
# x_data = [1.0, 2.0, 3.0]
# y_data = [2.0, 4.0, 6.0]

# w1=torch.Tensor([1.0])
# w1.requires_grad=True

# w2=torch.Tensor([1.0])
# w2.requires_grad=True

# b=torch.Tensor([1.0])
# b.requires_grad=True

# # 二次函数的forward模型描述
# def forward(x):
#     return w1**x+w2*x+b

# def loss(x,y):
#     y_pred=forward(x)
#     return (y_pred-y)**2

# print("预测（训练前）:",4,forward(4).item())

# #设置训练参数
# learning_rate=0.1
# epochs=1000
# history=[]

# for epoch in range(epochs):
#     for x,y in zip(x_data,y_data):
#         l=loss(x,y)
#         l.backward()

#         w1.data -= learning_rate * w1.grad.data
#         w2.data -= learning_rate * w2.grad.data
#         b.data -= learning_rate * b.grad.data

#         w1.grad.zero_()
#         w2.grad.zero_()
#         b.grad.zero_()
#     history.append(l.item())  # 记录每个epoch的损失



# print("预测 (训练后):", 4, forward(4).item())
# # 绘制损失曲线
# plt.plot(range(epochs), history)
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.title('Loss vs Epoch (SGD)')
# plt.show()





'''
# 回归模型：二次函数拟合
# ai给的示例代码
'''

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import torch
import matplotlib.pyplot as plt

# ------------------- 关键修改：Windows 系统字体配置 -------------------
# 设置中文字体为黑体（SimHei），确保 Windows 系统中存在
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei"]
# 解决负号显示为方块的问题
plt.rcParams["axes.unicode_minus"] = False
# -------------------------------------------------------------------

# 训练数据
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

# 初始化参数
w1 = torch.tensor([1.0], requires_grad=True)  # w₁参数
w2 = torch.tensor([1.0], requires_grad=True)  # w₂参数
b = torch.tensor([1.0], requires_grad=True)   # 偏置项b

# 前向传播函数：y = w₁x² + w₂x + b
def forward(x):
    return w1 * (x ** 2) + w2 * x + b

# 损失函数
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

# 训练前的预测
print("预测 (训练前):", 4, forward(4).item())

# 训练参数
learning_rate = 0.01
epochs = 1000
history = []

# 训练循环
for epoch in range(epochs):
    epoch_loss = 0
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()  # 反向传播计算梯度
        epoch_loss += l.item()

        # 参数更新（梯度下降） with 上下文管理器会禁用计算图的构建
        with torch.no_grad():
            w1.data -= learning_rate * w1.grad
            w2.data -= learning_rate * w2.grad
            b.data -= learning_rate * b.grad
        
        # 梯度清零
        w1.grad.zero_()
        w2.grad.zero_()
        b.grad.zero_()
    
    # 记录每个epoch的平均损失
    avg_loss = epoch_loss / len(x_data)
    history.append(avg_loss)
    
    # 每100个epoch打印一次训练进度
    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], 损失: {avg_loss:.6f}, w1: {w1.item():.4f}, w2: {w2.item():.4f}, b: {b.item():.4f}")

# 训练后的预测
print("预测 (训练后):", 4, forward(4).item())

# 绘制损失曲线
plt.figure(figsize=(10, 5))
plt.plot(range(1, epochs+1), history)
plt.xlabel('迭代次数')
plt.ylabel('损失值')
plt.title('训练过程中的损失变化')
plt.grid(True)
plt.show()

# 绘制原始数据点和拟合的二次函数曲线
plt.figure(figsize=(10, 5))
plt.scatter(x_data, y_data, color='red', label='原始数据') #scatter 属于散点图

# 生成预测曲线的x值
x_pred = torch.linspace(0, 5, 100) # 生成从0到5的100个点
y_pred = w1 * (x_pred ** 2) + w2 * x_pred + b

plt.plot(x_pred.detach().numpy(), y_pred.detach().numpy(), label='拟合曲线')
plt.xlabel('x值')
plt.ylabel('y值')
plt.title('原始数据与二次函数拟合结果')
plt.legend()
plt.grid(True)
plt.show()