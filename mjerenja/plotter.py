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
			X.append(line[1])
			Y.append(line[3])
			Z.append(line[5])
			C.append(0)

	except EOFError as e:
		break

plt.plot(X, color="r")
plt.plot(Y, color="g")
plt.plot(Z, color="b")
plt.plot(C, color="y")
plt.show()