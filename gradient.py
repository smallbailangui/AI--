import numpy as np
import matplotlib.pyplot as plt
x_date = [1.0,2.0,3.0]
y_date = [2.0,4.0,6.0]


w=1.0
def forword(x):
    return x*w
def cost(xs,ys):
    cost=0
    for x,y in zip(xs,ys):
        y_pred=forword(x)
        cost+=(y_pred-y)**2
        return cost/len(xs)
def gradient(xs,ys):
    grad=0
    for x,y in zip(xs,ys):
        grad +=2*x*(x*w-y)
    return grad/len(xs)

'''
记录模型训练前的预测效果（即还没学习之前，模型的表现）。 
方便和训练后的预测结果进行对比，观察模型训练的改进效果。
'''
print('Predict (before training):',4, forword(4)) # Initial prediction before training

for epoch in range(100):
    cost_val = cost(x_date, y_date)
    grad_val = gradient(x_date, y_date)
    w -= 0.01 * grad_val  # Update weight with learning rate 0.01
    print(f'Epoch {epoch+1}, Cost: {cost_val:.4f}, Gradient: {grad_val:.4f}, Weight: {w:.4f}')
    print('Predict (after training):', 4, forword(4))
