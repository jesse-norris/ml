import os, sys, time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

### "ex3data1.csv" contains 5,000 samples of 401 element arrays
### These correspond to 20x20 pixel images (400 elements) and 1 classification
### The images are written numbers and the classifications are the number (0-9)
X = np.loadtxt(os.path.join("..", "data", "ex3data1.csv"), delimiter=",", skiprows=1)
[m,n] = X.shape
# Assign 'y' as the classification array
y = X[:,[-1]]
# Remove 'y' from X
X = np.delete(X, -1, axis=1)

### View one of the images (0 to 4999)
# image = 0
# plt.imshow(X[image].reshape(20,20), origin='lower', cmap=plt.cm.binary)
# plt.title("Image of {}".format(int(y[image])))
# plt.show()
###################

# Add the bias array to 'X'
X = np.column_stack((np.ones(m), X))

def sigmoid(z):
	return 1/(1+np.exp(-z))

# Define the number of classes
classes = 10

### Verify the dimensions and type of 'X', 'y', and 'theta'
### Note: X includes the bias vector already
print("X:", X.shape, type(X))
print("y:", y.shape, type(y))

### Load the weight vectors of Neural Network
theta1 = np.loadtxt("ex3weights1.csv", delimiter=",")
theta2 = np.loadtxt("ex3weights2.csv", delimiter=",")
### Verify the dimensions and type of 'theta1' and 'theta2'
print("theta1:", theta1.shape, type(theta1))
print("theta2:", theta2.shape, type(theta2))

### Determine the second activation function
a2 = sigmoid(np.dot(X,theta1.T))
### Verify 'a2'
print("a2:", a2.shape, type(a2))
### Add the bias vector to 'a2'
a2 = np.insert(a2, 0, np.ones((1,m)), axis=1)
### Re-verify 'a2' and check that the bias vector is in the first column
print("a2:", a2.shape, type(a2))
print("a2[0]:", a2[0])
### Determine the their activiation function (the hypothesis)
a3 = sigmoid(np.dot(a2,theta2.T))
### Verify 'a3'
print("a3:", a3.shape, type(a3))
print("a3[0]:", a3[0])

### 'a3' now contain the 5000x10 hypothesis matrix
### Each row corresponds to an image
### Each column corresponds to the hypothesis for each image
### Checking the accuracy
correct = 0
for i, hyp, img in zip(range(len(y)), a3, y):
	if (int(img)%10 == int(str(np.argmax(hyp)+1)[-1])):
		# print("Success!")
		correct += 1
	else:
		print("#{} (guess: {}, actual: {})".format(i, int(str(np.argmax(hyp))[-1]), int(img)%10))

### Display the final results!
print("{} right out of 5000 ({}%)".format(correct, '%0.1f'%(correct/5000*100)))