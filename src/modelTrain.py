from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from dataPreprocess import load_data 

# Load the data
trainData, testData = load_data(r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\train', 
                                  r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\test')


# CNN model architecture
def buildModel(inputShape, numClasses):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', inputShape=inputShape),  # Conv layer
        MaxPooling2D(2, 2),  # Pooling layer
        Flatten(),  # Flatten layer
        Dense(128, activation='relu'),  # Dense fully connected layer
        Dense(numClasses, activation='softmax')  # Output layer
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# model architecture
model = buildModel(inputShape=(64, 64, 3), numClasses=trainData.numClasses)

# Train the model
model.fit(trainData, epochs=10, validation_data=testData)

# Save the trained model
model.save('asl_model.h5')
