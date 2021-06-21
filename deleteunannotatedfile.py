import os

filepath = "train_helmet_mask/"
os.chdir(filepath)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        if os.path.exists(filename.split('.')[0]+".txt"):
            continue
        else:
            os.remove(filename)

            