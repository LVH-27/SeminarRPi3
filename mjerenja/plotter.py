import matplotlib.pyplot as plt

X = []
Y = []
Z = []
C = []

while(1):
	try:
		line = raw_input().split()
		if "detected" in line:
			continue
		elif "click" in line:
			C.append(1)
		else:
			X.append(float(line[1]))
			Y.append(float(line[3]))
			Z.append(float(line[5]))
			C.append(0)
	except EOFError as e:
		break

x = plt.plot(X, color="r", label="X axis")
y = plt.plot(Y, color="g", label="Y axis")
z = plt.plot(Z, color="b", label="Z axis")
c = plt.plot(C, color="k", label="Click detection")
plt.ylabel("Relative acceleration")
plt.xlabel("Time")
#plt.legend(["X","Y","Z","Click detection"],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()