import matplotlib.pyplot as plt

# Open our file
file1 = open('output1.txt', 'r')
lines1 = file1.readlines()

file2 = open('output2.txt', 'r')
lines2 = file2.readlines()

file3 = open('output3.txt', 'r')
lines3 = file3.readlines()

# Capture the output from fortran
x1 = []
y1 = []
for line in lines1:
    row = line.strip().split()
    x1.append(float(row[0]))
    y1.append(float(row[1]))

x2 = []
y2 = []
for line in lines2:
    row = line.strip().split()
    x2.append(float(row[0]))
    y2.append(float(row[1]))

x3 = []
y3 = []
for line in lines3:
    row = line.strip().split()
    x3.append(float(row[0]))
    y3.append(float(row[1]))

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(15,10))

# Plot the derivative
plt.plot(x1, y1, color='blue')
plt.plot(x2, y2, color='grey')
plt.plot(x3, y3, color='green')

plt.xlim((0, 3.5))
plt.ylim((0, 3))

# Plot the original function
plt.title('Plot of Eulers Method')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('display')