import fileinput
import os


filepath = "Images/"
for filename in os.listdir(filepath):
    if filename.endswith(".txt"):
        try:
            with fileinput.FileInput(filename, inplace=True) as file:
                for line in file:
                    word, tail = line.split(" ", 1)
                    if word=='1':
                        new_line = ''
                        print(line.replace(line, new_line), end='')
        except Exception as exp:
            print("file not found" + str(exp))