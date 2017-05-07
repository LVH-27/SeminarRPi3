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


plt.plot(X, color="r", label="X axis")
plt.plot(Y, color="g", label="Y axis")
plt.plot(Z, color="b", label="Z axis")
plt.plot(C, color="k", label="Click detection")
plt.ylabel("Relative acceleration")
plt.xlabel("Time")
plt.show()


"""plt.figure(1)
plt.subplot(411, title="X axis")
plt.plot(X, color="r")

plt.subplot(412, title="Y axis")
plt.plot(Y, color="g")

plt.subplot(413, title="Z axis")
plt.plot(Z, color="b")

plt.subplot(414, title="Click detection")
plt.plot(C, color="y")"""