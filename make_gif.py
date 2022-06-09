import os
import imageio
import time

t0 = time.time()


folder = "AbsoluteVessel#1"

# for i in sorted(os.listdir(folder1)):
#     print(i)
# for i in sorted(os.listdir(folder2)):
#     print(i)
    
files = sorted(os.listdir(folder))
images = []
print(len(os.listdir(folder)))

for i in range(len(files)):
    images.append(imageio.imread(os.path.join(folder, files[i])))
    imageio.mimsave('mygif.gif', images, fps = 24)
    
print(time.time() - t0)