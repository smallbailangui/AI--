import numpy as np
import matplotlib.pyplot as plt
x_date = [1.0,2.0,3.0]
y_date = [2.0,4.0,6.0]
def forword(x):
    return x*w
def loss(x,y):
    y_pred = forword(x)
    return (y_pred - y)**2
w_list = []
mse_list = [] #代表均方误差
for w in np.arange(0.0,4.0,0.1):
    print("w:",w)
    l_sum = 0.0
    for x,y in zip(x_date,y_date):
        y_pred_val = forword(x)
        loss_val = loss(x,y)
        l_sum += loss_val
        print('\t',x,y,y_pred_val,loss_val)
    print('MSE=',l_sum/len(x_date))
    w_list.append(w)
    mse_list.append(l_sum/len(x_date))


plt.plot(w_list,mse_list)
plt.ylabel('LOSS')
plt.xlabel('Weight')
plt.title('Loss vs Weight')
plt.show()
# 画出损失函数的图像
plt.scatter(w_list, mse_list, color='red')
