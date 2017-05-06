import matplotlib.pyplot as plt

X = []
Y = []
Z = []

while(1):
	try:
		line = raw_input().split()
		X.append(line[1])
		Y.append(line[3])
		Z.append(line[5])

	except EOFError as e:
		break

plt.plot(X, color="r")
plt.plot(Y, color="g")
plt.plot(Z, color="b")
plt.show()