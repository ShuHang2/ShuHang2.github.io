# using SummaryWriter to write a chart
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("./tensorborad_logs")

# y = 2x
for i in range(100):
    writer.add_scalar("y=x", 2 * i, i)

# using SummaryWriter to add a picture
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("./tensorborad_logs")

# process img to numpy
img_path = (
    "./data/ants/800px-Meat_eater_ant_qeen_excavating_hole.jpg"  # ants first img
)
img = Image.open(img_path)
print(type(img))  # not meet the type

img_array = np.array(img)
print("type", type(img_array), "shape", img_array.shape)  # not meet the shape

# add img to tensorboard
writer.add_image("test", img_array, 1, dataformats="HWC")

writer.close
