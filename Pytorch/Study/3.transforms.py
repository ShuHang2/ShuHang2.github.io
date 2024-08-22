# import lib
from torchvision import transforms
from PIL import Image

# to tensor
img_path = (
    "./data/val/ants/800px-Meat_eater_ant_qeen_excavating_hole.jpg"  # ants first img
)
img = Image.open(img_path)
print("type", type(img))

trans_totensor = transforms.ToTensor()  # introduce class to create one tool
img_tensor = trans_totensor(img)  # use this tool

print(type(img_tensor))

from torch.utils.tensorboard import SummaryWriter

write = SummaryWriter("logs")

write.add_image("Tensor Img", img_tensor, 0)

# Normalize
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])

write.add_image("Tensor Img", img_tensor, 1)

# resize
print(img.size)
trans_resize = transforms.Resize((64, 64))
img_resize = trans_resize(img)
img_resize = trans_totensor(img)

write.add_image("Resize", img_tensor, 2)

# print(img_resize)
# compose - resize -  2
trans_resize_2 = transforms.Resize(512)
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])

img_resize_2 = trans_compose(img)

write.add_image("Resize2", img_tensor, 3)

# print(img_resize)

# random crop
trans_rcrop = transforms.RandomCrop(512)
trans_compose_2 = transforms.Compose([trans_resize_2, trans_totensor])

for i in range(10):
    img_crop = trans_compose_2(img)
    write.add_image("random crop", img_crop, i)
    
write.close()
