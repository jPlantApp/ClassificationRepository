from sklearn.model_selection import train_test_split
import os
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import tensorflow as tf
from keras.callbacks import ModelCheckpoint
from keras.callbacks import ModelCheckpoint
from torchvision.transforms import ColorJitter
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from keras.callbacks import CSVLogger
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
import configparser

config = configparser.ConfigParser()
config.read('train.ini')

b_size = int(config.get('configuration', 'batch_size'))
d_dir = config.get('configuration', 'data_dir') 
n_classes = int(config.get('configuration', 'num_classes'))
tst_size = float(config.get('configuration', 'test_size'))
r_state = int(config.get('configuration', 'random_state'))
dropout = float(config.get('configuration', 'dropout'))
epsilon = float(config.get('configuration', 'epsilon'))
momentum = float(config.get('configuration', 'momentum'))
l_rate = float(config.get('configuration', 'learning_rate'))
epch = int(config.get('configuration', 'epochs'))



def improved_vgg16(num_classes, d, e, m):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(250, 250, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization(momentum=m, epsilon=e))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization(momentum=m, epsilon=e))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization(momentum=m, epsilon=e))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(d))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    optimizer = Adam(learning_rate=l_rate)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    model.summary()

    return model

class ImageJitter(object):
    def __init__(self, saturation_range=(0.8, 1.2), contrast_range=(0.8, 1.2), hue_range=(-0.1, 0.1)):
        self.saturation_range = saturation_range
        self.contrast_range = contrast_range
        self.hue_range = hue_range

    def __call__(self, x):
        color_jitter = ColorJitter(
            contrast=self.contrast_range,
            saturation=self.saturation_range,
            hue=self.hue_range
        )
        x = color_jitter(np.array(x))
        return x

gpus = tf.config.experimental.list_physical_devices('GPU')
batch_size = b_size
target_size = (250, 250)
data_dir = d_dir
data = []
num_classes = n_classes 

for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if os.path.isdir(class_dir):
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            data.append((img_path, class_name))
            
train_data, test_data = train_test_split(data, test_size=tst_size, random_state=r_state)

train_df = pd.DataFrame(train_data, columns=['filename', 'label'])
test_df = pd.DataFrame(test_data, columns=['filename', 'label'])

print(train_df)
print(test_df)

train_boosted_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,           # Zakres obracania obrazu (w stopniach)
    width_shift_range=0.2,       # Zakres przesunięcia obrazu w poziomie
    height_shift_range=0.2,      # Zakres przesunięcia obrazu w pionie
    shear_range=0.2,             # Zakres przekształcenia sferycznego
    zoom_range=0.2,              # Zakres przybliżenia/oddalenia obrazu
    horizontal_flip=True,        # Losowe odbicie w poziomie
    brightness_range=(0.8, 1.2), # Zakres zmiany jasności
    channel_shift_range=10
    )

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_boosted_generator = train_boosted_datagen.flow_from_dataframe(
    train_df,
    x_col='filename',
    y_col='label',
    batch_size=batch_size,
    target_size=target_size,
    class_mode='categorical',
    preprocessing_function=ImageJitter()
)

test_generator = test_datagen.flow_from_dataframe(
    test_df,
    x_col='filename',
    y_col='label',
    batch_size=batch_size,
    target_size=target_size,
    class_mode='categorical'
)

model = improved_vgg16(num_classes, dropout, epsilon, momentum)

csv_logger = CSVLogger("history_other_500.csv")

model_checkpoint_loss = ModelCheckpoint('model_best_loss.h5', monitor='val_loss', save_best_only=True, verbose=1)
model_checkpoint_acc = ModelCheckpoint('model_best_acc.h5', monitor='val_accuracy', save_best_only=True, verbose=1)

model.fit(train_boosted_generator, epochs=epch, validation_data=test_generator, callbacks=[model_checkpoint_loss, model_checkpoint_acc, csv_logger])