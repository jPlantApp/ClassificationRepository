from flask import Flask, jsonify, request
from flask_cors import CORS  
import base64
import Functions.func as ff
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

uname = config.get('database', 'uname')
passwd = config.get('database', 'passwd')
host = config.get('database', 'host')
dbname = config.get('database', 'dbname')

engine = create_engine(f'postgresql://{uname}:{passwd}@{host}/{dbname}')

app = Flask(__name__)
CORS(app)

@app.route('/api/get_photo_classification', methods=['POST'])
def get_photo_classification():
    try:
        image_base = request.json.get('imageData', '')
        image_url = request.json.get('photoPath', '')
        user_token = request.json.get('userToken', '')
        user_email = request.json.get('userEmail', '')

        Session = sessionmaker(bind=engine)
        session = Session()
        image_data = base64.b64decode(image_base)
        classification_result = ff.get_classification(session, image_data, image_url, user_token, user_email)
        if classification_result is None:
            return jsonify({'error'}), 401
        else:
            return jsonify(classification_result), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/api/login_user', methods=['POST'])
def login_user():
    try:
        email = request.json.get('userEmail', '')
        token_id = request.json.get('userToken', '')
        name = request.json.get('userName', '')
        Session = sessionmaker(bind=engine)
        session = Session()

        ff.login_user(session, name, email, token_id)

        return jsonify({
            'user_id': token_id,
            'name': name,
            'email': email,
        }), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/get_flower_list', methods=['GET'])
def get_flower_list():
    try:
        user_token = request.args.get('userToken')
        user_email = request.args.get('userEmail')
        Session = sessionmaker(bind=engine)
        session = Session()
        user_flowers = ff.get_users_flowers_by_token_id(session, user_token, user_email)
        session.close()
        if user_flowers is None:
            return jsonify({'error'}), 401
        else:
            return jsonify(user_flowers), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
