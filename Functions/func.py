from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, joinedload

from keras.preprocessing.image import ImageDataGenerator
import os
import requests
import numpy as np
from PIL import Image
from io import BytesIO
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
import configparser
from Functions.db import Flower
from Functions.db import User
from Functions.db import UsersFlowers

config = configparser.ConfigParser()
config.read('config.ini')

uname = config.get('database', 'uname')
passwd = config.get('database', 'passwd')
host = config.get('database', 'host')
dbname = config.get('database', 'dbname')
web_client_id = config.get('google', 'web_client_id')
path_to_model = config.get('model', 'model_path')
dir_with_flowers = config.get('model', 'dir_with_flowers')


engine = create_engine(f'postgresql://{uname}:{passwd}@{host}/{dbname}')


Base = declarative_base()
Base.metadata.create_all(engine)


def get_users_flowers_by_token_id(session: Session, user_token: str, email: str):
    account_status = verify_user(user_token, web_client_id, email)

    if account_status:
        user = session.query(User).filter_by(email=email).first()

        flowers = (
                session.query(UsersFlowers)
                .options(joinedload(UsersFlowers.flower))
                .filter(UsersFlowers.user_id == user.id)
                .all()
            )

        flower_list = []

        for user_flower in flowers:
            flower_json = {
                'flowerName': user_flower.flower.name,
                'prediction': float(f'{user_flower.accuracy * 100:.2f}'),
                'imagePath': user_flower.photo_url,
                'description': user_flower.flower.description,
                'growing': user_flower.flower.growing,
                'usage': user_flower.flower.usage,
                'flowering': user_flower.flower.flowering,
                'winterizing': user_flower.flower.winterizing,
                'notes': user_flower.flower.notes
            }
            flower_list.append(flower_json)
        return flower_list
    else:
        return None


def login_user(session: Session, name: str, email: str, token_id: str):
    account_status = verify_user(token_id, web_client_id, email)

    if account_status:
        existing_user = session.query(User).filter_by(email=email).first()

        if existing_user is None:
            new_user = User(name=name, email=email)
            session.add(new_user)
            session.commit()
            return True
        else:
            return True
    else:
        return False


def get_classification(session: Session, image_base64: str, image_url: str, user_token: str, email: str):

    account_status = verify_user(user_token, web_client_id, email)

    if account_status:
        test_datagen = ImageDataGenerator(rescale=1.0/255)
        test_generator = test_datagen.flow_from_directory(
            dir_with_flowers,
            target_size=(250, 250),
            class_mode='categorical'
        )

        model_path = path_to_model
        model = load_model(model_path)


        image = Image.open(BytesIO(image_base64))
        img = image.convert('RGB')
        img = img.resize((250, 250))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        predicted_value = prediction[0][np.argmax(prediction)]
        class_label = test_generator.class_indices

        predicted_label = None

        for key, value in class_label.items():
            if value == predicted_class:
                predicted_label = key
                break
        
        flower = session.query(Flower).filter_by(name=predicted_label).first()
        user = session.query(User).filter_by(email=email).first()

        new_user_flower = UsersFlowers(
            flower_id=int(flower.id),
            user_id=int(user.id),
            accuracy=str(predicted_value),
            photo_url=str(image_url)
        )

        result = {
            'flowerName': predicted_label,
            'prediction': float(f'{predicted_value * 100:.2f}'),
            'imagePath': image_url,
            'description': flower.description,
            'growing': flower.growing,
            'usage': flower.usage,
            'flowering': flower.flowering,
            'winterizing': flower.winterizing,
            'notes': flower.notes
        }

        session.add(new_user_flower)
        session.commit()
        return result
    else:
        return None


def verify_user(token_id: str, client_id: str, email: str):
    verification_url = f'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token_id}&client_id={client_id}'
    response = requests.get(verification_url)
    data = response.json()

    if 'error_description' in data:
        return False
    else:
        if 'email' in data:
            if email == data['email']:
                return True
            else:
                return False