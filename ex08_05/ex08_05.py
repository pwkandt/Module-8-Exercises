fName = input("Enter file name: ")
count = 0

try:
    fHandle = open(fName)
except:
    print('Invalid file name:', fName)
    quit()

for line in fHandle:
    if line.startswith('From '):
        line = line.split()
        count = count + 1
        print(line[1])

print("There were", count, "lines in the file with From as the first word")
