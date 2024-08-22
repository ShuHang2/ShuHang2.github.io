import torch
import torch.nn as nn
import torch.nn.functional as F

# https://pytorch.org/docs/2.3/generated/torch.nn.Module.html#torch.nn.Module

# https://github.com/vdumoulin/conv_arithmetic


import torchvision.datasets
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# download dataset
dataset = torchvision.datasets.CIFAR10(
    "./data/CIFAR10",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    # download=True,
)

dataloader = DataLoader(
    dataset=dataset, batch_size=64, shuffle=True, num_workers=0, drop_last=False
)


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 3, 1, 0)

    def forward(self, x):
        x = self.conv1(x)
        return x


MyModel = Model()

writer = SummaryWriter("model_logs")
step = 0
for data in dataloader:
    imgs, targets = data
    output = MyModel(imgs)
    print(imgs.shape)
    print(output.shape)
    writer.add_images("input", imgs, step)
    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images("output", output, step)
    step = step + 1
writer.close()

