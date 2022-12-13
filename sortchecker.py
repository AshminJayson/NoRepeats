
f = open('testdata.txt', 'r')

lines = f.readlines()

data = []
for line in lines:
    data.append(line)

x = sorted(data)

if data == x:
    print('fair')

