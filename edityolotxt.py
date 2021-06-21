import fileinput
import os

#filename = "005298_jpg.rf.647d148af5d961d8bbc041f172247170_copy.txt"
filepath = "train_helmet/"
replacements = {'0':'1', '1':'2'}

os.chdir(filepath)
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                word, tail = line.split(" ", 1)
                if word in replacements:
                    word_replace = replacements[word]
                    new_line = word_replace+" " +tail
                    print(line.replace(line, new_line), end='')