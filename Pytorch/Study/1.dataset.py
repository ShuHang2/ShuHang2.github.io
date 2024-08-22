# import lib
from torch.utils.data import Dataset
from PIL import Image
import os


class MyDataSet(Dataset):
    def __init__(self, root_dir, lable_dir):
        self.root_dir = root_dir
        self.lable_dir = lable_dir
        self.path = os.path.join(self.root_dir, self.lable_dir)

        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_name_path = os.path.join(self.root_dir, self.lable_dir, img_name)

        img = Image.open(img_name_path)
        lable = self.lable_dir

        return img, lable

    def __len__(self):
        return len(self.img_path)


root_dir = "./data"

ant_lable_dir = "ants"
ants_dataset = MyDataSet(root_dir, ant_lable_dir)

bees_lable_dir = "bees"
bees_dataset = MyDataSet(root_dir, bees_lable_dir)

train_dataset = ants_dataset + bees_dataset

img, lable = train_dataset[0]

train_dataset.__len__()
