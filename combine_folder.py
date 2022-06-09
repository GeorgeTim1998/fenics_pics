from operator import concat
import os
from PIL import Image
import numpy as np

folder1 = "Novessel#2"
folder2 = "Vessel#2"
concat_folder= "Concat#2"

# for i in sorted(os.listdir(folder1)):
#     print(i)
# for i in sorted(os.listdir(folder2)):
#     print(i)
    
files1 = sorted(os.listdir(folder1))
files2 = sorted(os.listdir(folder2))
# print(len(os.listdir('Vessel#2')))
# print(len(os.listdir('Novessel#2')))

for i in range(len(files1)):
    im1 = Image.open(os.path.join(folder1, files1[i]))
    im2 = Image.open(os.path.join(folder2, files2[i]))
    
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    
    concat_name = "%d.png" % i
    dst.save(os.path.join(concat_folder, concat_name))