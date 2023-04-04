fName = input("Enter file name: ")
lst = []

try:
   fHandle = open(fName)
except:
   print('Invalid file name:', fName)
   quit()

for line in fHandle:
   for word in line.split():
      if word not in lst:
         lst.append(word)

lst.sort()
print(lst)
