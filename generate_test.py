import os

image_files = []
os.chdir(os.path.join("data", "test_images"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        image_files.append("data/test_images/" + + filename.split('.')[0]+".jpg")
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")