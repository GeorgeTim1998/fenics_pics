import os
import imageio
import time
import combine_folder

def mysort(string):
    return int(string.split(".png")[0])

t0 = time.time()

NAME = 'ITER'
attempt = 2
FPS = 12

print("\nCombining pics from folders...")
combine_folder.combine_pics_from_folders(NAME, attempt)

folder = "Pics/%sConcat#%d" % (NAME, attempt)
files = sorted(os.listdir(folder), key=mysort)
images = []

print(len(os.listdir(folder)))
print(time.time() - t0)

print("\nCreating gif...")
for i in range(len(files)):
    print("%d/%d -> %.2f" % (i+1, 
                             len(files),
                             (i+1)/len(files)*100))
    images.append(imageio.imread(os.path.join(folder, files[i])))

print(time.time() - t0)

savepath = "Pics/Gifs/%sConcat#%d.gif" % (NAME, attempt)
imageio.mimsave(savepath, images, fps = FPS)
print("Gif saved to: %s" % savepath)

print(time.time() - t0)