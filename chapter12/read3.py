infile = open("phones.txt", "r")
line = infile.readline()
while line !="":
    print(line)
    line = infile.readline()
infile.close