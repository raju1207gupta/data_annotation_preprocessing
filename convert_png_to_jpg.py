from PIL import Image
import os

directory = "Images/"

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        im = Image.open(filename)
        name=filename.split(".")[0]+'.jpg'
        rgb_im = im.convert('RGB')
        rgb_im.save(os.path.join(directory, name))
        continue
    else:
        continue
