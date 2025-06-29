import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

batch_size = 64
transform=transforms.Compose([
    transforms.ToTensor(), # 将PIL图像转变为tensor 归一化
    transforms.Normalize((0.1307, ),(0.3081, )) # 均值和标准差，数据标准化的基本操作 标准化
])

# 加载mnist数据集
train_dataset=datasets.MNIST(root='../dataset/mnist',
                             train=True,
                             download=False,
                             transform=transform)

train_loader=DataLoader(train_dataset,shuffle=True,batch_size=batch_size)
test_dataset=datasets.MNIST(root='../dataset/mnist',
                            train=False,
                            download=False,
                            transform=transform
                            )
test_loader=DataLoader(test_dataset,shuffle=False,batch_size=batch_size)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.pooling = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        batch_size = x.size(0)
        x = F.relu(self.pooling(self.conv1(x)))
        x = F.relu(self.pooling(self.conv2(x)))
        x = x.view(batch_size, -1)  # flatten
        x = self.fc(x)
        return x

model = Net()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)


criterion=torch.nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.01, momentum=0.90)

def train(epoch):
    running_loss = 0.0
    for batch_idx, data in enumerate(train_loader, 0):
        inputs, target = data
        inputs, target = inputs.to(device), target.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if batch_idx % 300 == 299:
            print('[%d, %5d] loss: %.3f' % (epoch + 1, batch_idx + 1, running_loss / 300))
            running_loss = 0.0

def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))
    

if __name__ == "__main__":
    for epoch in range(5):  # 训练5个epoch，可根据需要调整
        train(epoch)
        test()


