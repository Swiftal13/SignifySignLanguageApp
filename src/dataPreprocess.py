import os
import tensorflow
keras = tensorflow.keras
preprocessing = keras.preprocessing
image = preprocessing.image
ImageDataGenerator = image.ImageDataGenerator

# Path to the training and test directories
trainDir = r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\.kaggle\asl_alphabet_train'
testDir = r'D:\Programming\Python\All PY files\SignifyNEA\NEA\Datasets\.kaggle\asl_alphabet_test'

# Set up ImageDataGenerator for normalization (rescaling pixel values)
def loadData(trainDir, testDir, targetSize=(64, 64), batchSize=32):
    # Training data generator (rescaling pixel values)
    trainDatagen = ImageDataGenerator(rescale=1.0/255.0)
    trainData = trainDatagen.flow_from_directory(
        directory=trainDir,
        target_size=targetSize,  # Resize images to the target size
        batch_size=batchSize,
        class_mode='categorical',  # Multi-class classification
        shuffle=True  # Shuffle the dataset
    )

    # Test data generator (rescaling pixel values)
    testDatagen = ImageDataGenerator(rescale=1.0/255.0)
    testData = testDatagen.flow_from_directory(
        directory=testDir,
        target_size=targetSize,  # Resize images to the target size
        batch_size=batchSize,
        class_mode='categorical',  # Multi-class classification
        shuffle=False  # Do not shuffle test data
    )

    return trainData, testData

# Load both training and test data
trainData, testData = loadData(trainDir, testDir)

# Display the class labels and number of classes
print("Class labels:", trainData.class_indices)
print("Number of classes:", trainData.num_classes)