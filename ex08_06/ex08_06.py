lst = []

while True:
    num = input('Enter a number: ')
    if num == 'Done':
        break
    try:
        fNum = float(num)
        lst.append(fNum)
    except:
        print('Invalid input')
        continue

print('Maximum is', max(lst))
print('Minimum is', min(lst))
