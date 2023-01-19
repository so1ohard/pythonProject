import random

from keras.datasets import mnist
from matplotlib import pyplot

(train_X, train_y), (test_X, test_y) = mnist.load_data()


#print('X_train: ' + str(train_X.shape))
#print('Y_train: ' + str(train_y.shape))
#print('X_test:  '  + str(test_X.shape))
#print('Y_test:  '  + str(test_y.shape))

for i in range(12):
    pyplot.subplot(3,5,i+1)

    rand=random.randrange(0,100,1)
    pyplot.imshow(train_X[rand], cmap=pyplot.get_cmap('Greens'))
pyplot.show()
