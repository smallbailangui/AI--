import torch 
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim
import torch.nn as nn


batch_size = 64
transform=transforms.Compose([
    transforms.ToTensor(), # 将PIL图像转变为tensor 归一化
    transforms.Normalize((0.1307, ),(0.3081, )) # 均值和标准差，数据标准化的基本操作 标准化
])

# 加载mnist数据集
train_dataset=datasets.MNIST(root='./dataset/mnist',
                             train=True,
                             download=True,
                             transform=transform)

train_loader=DataLoader(train_dataset,shuffle=True,batch_size=batch_size)
test_dataset=datasets.MNIST(root='./dataset/mnist',
                            train=False,
                            download=True,
                            transform=transform
                            )
test_loader=DataLoader(test_dataset,shuffle=False,batch_size=batch_size)


class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.layers=nn.Sequential(
            nn.Linear(784,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,10)
        )
    
    def forward(self,x):
        x=x.view(-1,784)
        x=self.layers(x)
        return x
    
model = Model()

criterion=torch.nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.01, momentum=0.90) # momentum冲量,会考虑历史梯度的累计影响

def train(epoch):
    running_loss=0.0
    for batch_idx,data in enumerate(train_loader,0):
        inputs,target=data
        optimizer.zero_grad()

        outputs=model(inputs)
        loss=criterion(outputs,target)
        loss.backward()
        optimizer.step()

        running_loss+=loss.item()
        if batch_idx % 300 ==299:
            print('[%d,%5d] loss: %.3f' % (epoch+1,batch_idx+1,running_loss/300))
            running_loss=0.0

def test():
    correct=0
    total=0
    with torch.no_grad():
        for data in test_loader:
            images,labels=data
            outputs=model(images)
            _, pred=torch.max(outputs.data,dim=1)
            total+=labels.size(0)
            correct+=(pred==labels).sum().item()
        print('Accurcy on test set: %d %%' % (100*correct/total))


if __name__=='__main__':
    for epoch in range(10):
        train(epoch)
        test()