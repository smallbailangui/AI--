import torchvision

'''
CIFAR-10也是一个常用的图像数据集,包含60000张32x32的彩色图像,分为10个类别。
MNIST是一个手写数字数据集,包含60000张28x28的灰度图像,分为10个类别。
'''

trans_set=torchvision.datasets.MNIST(root='./dataset/minist',train=True,download=True)
test_set=torchvision.datasets.MNIST(root='./dataset/minist',train=False,download=True)