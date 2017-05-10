import matplotlib.pyplot as plt

def lpf(axis_data):
	aux = []
	old_x = axis_data[0]
	alpha = 0.2


	for x in axis_data:

		curr_data = (1 - alpha) * x + alpha * old_x
		aux.append(curr_data)
		old_x = curr_data


	return aux


X = []
Y = []
Z = []
C = []

while(1):
	try:
		line = input().split()
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

X_lpf = lpf(X)

plt.subplot(211)
x = plt.plot(X, color="r", label="X axis")
plt.subplot(212)
x_lpf = plt.plot(X_lpf, color="b", label="Filtered X axis")
#plt.subplot(211)

# y = plt.plot(Y, color="g", label="Y axis")
# z = plt.plot(Z, color="b", label="Z axis")
# c = plt.plot(C, color="k", label="Click detection")

plt.ylabel("Relative acceleration")
plt.xlabel("Time")
#plt.legend(["X","Y","Z","Click detection"],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
