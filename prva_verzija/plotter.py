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

plt.plot(X, color="r", label="X axis")
plt.plot(Y, color="g", label="Y axis")
plt.plot(Z, color="b", label="Z axis")
plt.plot(C, color="k", label="Click detection")
plt.ylabel("Relative acceleration")
plt.xlabel("Time")
plt.show()