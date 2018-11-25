#!/usr/bin/env python3
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy

data = numpy.loadtxt("shows.csv", delimiter=",",skiprows=1)
X = data[:,0:3]
Y = data[:,3]
print('oto data: \n', data)
print(X)
print(Y)
# przeksztalcenie do postaci one hot notation
categories = np_utils.to_categorical(Y)
print(categories)
model = Sequential()
model.add(Dense(10, input_dim=3, activation = 'relu'))
model.add(Dense(3, activation = 'relu'))
model.add(Dense(3, activation = 'sigmoid'))

model.compile(loss='binary_crossentropy',optimizer = 'adam')
model.fit(X, categories, epochs = 100, batch_size=100, verbose = 0)
test_data = numpy.array([[0,1,2],[0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]])
print('test data', test_data)
pred = model.predict(test_data)
print(type(pred))
for (idx, row) in enumerate(test_data):
	print(row, row[2])