import os
import imageio
import time

def mysort(string):
    return int(string.split(".png")[0])

t0 = time.time()

NAME = 'ITER'
i = 1

folder = "Pics/%sConcat#%d" % (NAME, i)
files = sorted(os.listdir(folder), key=mysort)
images = []

print(len(os.listdir(folder)))
print(time.time() - t0)

for i in range(len(files)):
    print("%d/%d -> %.2f" % (i+1, 
                             len(files),
                             (i+1)/len(files)*100))
    images.append(imageio.imread(os.path.join(folder, files[i])))

print(time.time() - t0)

savepath = "Pics/Gifs/%s.gif" % NAME
imageio.mimsave(savepath, images, fps = 18)
print("Gid saved to: %s" % savepath)

print(time.time() - t0)