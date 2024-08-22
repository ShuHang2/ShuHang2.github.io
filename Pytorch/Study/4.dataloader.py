import torchvision.datasets
from torch.utils.tensorboard import SummaryWriter

from torch.utils.data import DataLoader

# download dataset
test_data = torchvision.datasets.CIFAR10(
    "./data/CIFAR10",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    # download=True,
)

test_loader = DataLoader(
    dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False
)

img, target = test_data[0]

print(img.shape)
print(target)

wirter = SummaryWriter("dataloader_logs")

for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        # print(imgs.shape)
        # print(targets)
        wirter.add_images("Epoch:{}".format(epoch), imgs, step)
        step = step + 1
wirter.close()
