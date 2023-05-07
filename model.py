import tensorflow as tf
import numpy as np
import cv2


def train_model(decision):
    if decision is True:
        print("Training model...")
        mnist = tf.keras.datasets.mnist
        (trainx, trainy), (testx, testy) = mnist.load_data()
        trainx = tf.keras.utils.normalize(trainx, axis=1)
        testx = tf.keras.utils.normalize(testx, axis=1)
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(trainx, trainy, epochs=3)
        val_loss, val_acc = model.evaluate(testx, testy)
        print(val_loss)
        print(val_acc)
        model.save('rozpoznanie_pisma.model')


def load_model():
    print("Using model")
    model = tf.keras.models.load_model('rozpoznanie_pisma.model')
    return model


def use_model(filepath):
    model = load_model()
    image_file = cv2.imread(filepath)[:, :, 0]
    dsize = (28, 28)
    image_file_resized = cv2.resize(image_file, dsize)
    image_file_resized = np.invert(np.array([image_file_resized]))
    number_prediction = model.predict(image_file_resized)
    return "Numer widoczny na obrazku to prawdopodobnie {}"\
        .format(np.argmax(number_prediction))
