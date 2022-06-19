from operator import concat
import os
from PIL import Image
import numpy as np

def combine_pics_from_folders(NAME, i):
    folder1 = "Pics/%sNovessel#%d"  % (NAME, i)
    folder2 = "Pics/%sVessel#%d"  % (NAME, i)
    concat_folder= "Pics/%sConcat#%d"  % (NAME, i)

    if os.path.exists(concat_folder) == False:
        os.mkdir(concat_folder)

    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))

    print(files1)
    print(files2)

    for i in range(len(files1)):
        print("%d/%d -> %.2f" % (i+1, 
                                len(files1),
                                (i+1)/len(files1)*100))
        
        im1 = Image.open(os.path.join(folder1, files1[i]))
        im2 = Image.open(os.path.join(folder2, files2[i]))
        
        dst = Image.new('RGB', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        
        concat_name = "%d.png" % i
        dst.save(os.path.join(concat_folder, concat_name))