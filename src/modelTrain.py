from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from dataPreprocess import loadData 
import time



# Load the data
trainData, testData = loadData(r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\train', 
                                  r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\test')


sampleBatch, sampleLabels = next(trainData)  # Get a sample batch from the training data generator
print("Shape of first batch of images:", sampleBatch.shape)  # Should print (batch_size, height, width, channels)
print("Shape of first batch of labels:", sampleLabels.shape)  # Should print (batch_size, num_classes)

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
model = buildModel(inputShape=(64, 64, 3), numClasses=trainData.num_classes)


start = time.time() # Start time for training

model.fit(trainData, epochs=10, validation_data=testData) # Train the model

end = time.time() # Calculate the time taken to train the model

print(f"Training completed in {(end - start):.2f} seconds.") # Print the time taken to train the model

# Save the trained model
model.save('asl_model.h5')