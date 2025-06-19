import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0

def forward(x):
    return x * w

def loss (x,y):
    y_pred=forward(x)
    return (y_pred - y) ** 2

def gradient(x, y):
    return 2 * x * (x * w - y)

print('Predict (before training):', 4, forward(4))

cost_list = []
for epoch in range(100):
    for x, y in zip(x_data, y_data):
        grad = gradient(x, y)
        w -= 0.01 * grad
        print("\tgrad: ",x, y, grad)
        l=loss(x, y)
        cost_list.append(l)

    print("progress: ", epoch, "loss: ", l, "weight: ", w)

# 绘制 cost 曲线
plt.plot(range(100), cost_list)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.title('Cost vs Epoch (SGD)')
plt.show()

print('Predict (after training):', 4, forward(4))