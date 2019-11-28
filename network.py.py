from keras.models import Sequential
from keras.layers import Dense
import numpy


numpy.random.seed(2)


dataset = numpy.loadtxt("prima-indians-diabetes.csv", delimiter=",") #Данные для обучения 

X, Y = dataset[:,0:1024], dataset[:,1025]


model = Sequential()
model.add(Dense(2048, input_dim=1024, activation='relu')) 
model.add(Dense(15, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1)) 

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])


model.fit(X, Y, epochs = 1000, batch_size=10)


scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))