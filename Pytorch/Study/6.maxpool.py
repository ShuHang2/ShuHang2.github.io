import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(
    "./data/CIFAR10",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    # download=True,
)
dataloader = DataLoader(dataset, batch_size=64)

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])

input = torch.reshape(input, (-1, 1, 5, 5))

print("input tenser", input.shape)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output


Model = Model()

writer = SummaryWriter("maxpool_logs")
step = 0

for data in dataloader:
    imgs, target = data
    writer.add_images("input", imgs, step)
    output = Model(imgs)
    writer.add_images("output", output, step)
    step = step + 1

writer.close()
