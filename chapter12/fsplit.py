infile = open("C:\PYTHON CODE 2025\chapter12\proverbs.txt", "r")

for line in infile:
    line = line.strip()
    word_list = line.strip()
    for word in word_list:
        print(word)
infile.close()