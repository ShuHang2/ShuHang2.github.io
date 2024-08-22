# 根据LeNet模型图`.study step\Net\img.png`构建神经网络模型
import torch
from torch import nn


# 搭建神经网络
# input：batch size为64、通道为3、全为1、32*32的张量
# output：batch size为64、特征结果为10
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10),
        )

    def forward(self, x):
        x = self.model(x)
        return x


if __name__ == "__main__":
    model = Model()
    input = torch.ones((64, 3, 32, 32))
    output = model(input)
    print(output.shape)
