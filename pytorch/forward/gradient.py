import numpy as np
import matplotlib.pyplot as plt
x_date = [1.0,2.0,3.0]
y_date = [2.0,4.0,6.0]


w = 1.0
def forward(x):
    return x * w

def cost(xs, ys):
    cost = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x)
        cost += (y_pred - y) ** 2
    return cost / len(xs)  # 修正缩进

def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (x * w - y)
    return grad / len(xs)

print('Predict (before training):', 4, forward(4))

cost_list = []
for epoch in range(100):
    cost_val = cost(x_date, y_date)
    grad_val = gradient(x_date, y_date)
    # 这里的a =0.01
    w -= 0.01 * grad_val
    cost_list.append(cost_val)
    print(f'Epoch {epoch+1}, Cost: {cost_val:.4f}, Gradient: {grad_val:.4f}, Weight: {w:.4f}')

# 绘制 cost 曲线
plt.plot(range(100), cost_list)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.title('Cost vs Epoch')
plt.show()

print('Predict (after training):', 4, forward(4))


