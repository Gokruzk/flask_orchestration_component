from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
API_USER = 'http://127.0.0.1:5001'
API_EMAIL = 'http://127.0.0.1:5002'


@app.route('/', methods=['POST'])
def register_user():
    # retreiving user data
    user_data = request.json

    # call user register service
    registration_response = requests.post(
        f'{API_USER}/user', json=user_data)

    # verify registration service response
    if registration_response.status_code == 200:
        # user email
        email_data = {'email': user_data['email']}
        # call email service
        email_response = requests.post(
            f'{API_EMAIL}/email', json=email_data)

        # # verify email service response
        if email_response.status_code == 200:
            return jsonify({'message': 'User registered and welcome email sent'}), 200
        else:
            return jsonify({'error': 'Failed to send welcome email'}), 500
    else:
        return jsonify({'error': 'Failed to register user'}), 500


if __name__ == '__main__':
    app.run(debug=True)
