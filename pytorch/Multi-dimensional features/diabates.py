import torch
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 使用sklearn加载糖尿病数据集
diabetes = load_diabetes()
X = diabetes.data  # 特征，这里包含10个特征
y = diabetes.target  # 目标变量,这里代表的是糖尿病患者一年后疾病进展的定量测量

# 数据预处理
'''
这一步不是很清楚原理，后续需要查阅相关资料
'''
scaler = StandardScaler() # 标准化特征
X = scaler.fit_transform(X) # 特征标准化,先拟合再转换

# 转换为二分类问题（根据血糖水平是否高于中位数）
y_binary = (y > np.median(y)).astype(np.float32).reshape(-1, 1)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# 转换为PyTorch张量
x_train_tensor = torch.from_numpy(X_train).float()
y_train_tensor = torch.from_numpy(y_train).float()
x_test_tensor = torch.from_numpy(X_test).float()
y_test_tensor = torch.from_numpy(y_test).float()

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(10, 6)  
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)  
        self.activate = torch.nn.Sigmoid()
    
    def forward(self, x):
        x = self.activate(self.linear1(x))
        x = self.activate(self.linear2(x))
        x = self.activate(self.linear3(x))
        return x

model = Model()

criterion = torch.nn.BCELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


for epoch in range(100):
    y_pred = model(x_train_tensor)
    loss = criterion(y_pred, y_train_tensor)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 评估模型
with torch.no_grad():
    y_pred_test = model(x_test_tensor)
    y_pred_binary = (y_pred_test > 0.5).float()
    accuracy = (y_pred_binary == y_test_tensor).sum().item() / len(y_test_tensor)
    print(f'测试集准确率: {accuracy:.4f}')    