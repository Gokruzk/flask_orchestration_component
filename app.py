from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register_user():
    # retreiving user data
    user_data = request.json  

    # call user register service
    registration_response = requests.post(
        'http://127.0.0.1:5001/user', json=user_data)

    # verify registration service response
    if registration_response.status_code == 200:
        # user email
        email_data = {'email': user_data['email']}
        # call email service
        email_response = requests.post(
            'http://127.0.0.1:5002/email', json=email_data)

        # # verify email service response
        if email_response.status_code == 200:
            return jsonify({'message': 'User registered and welcome email sent'}), 200
        else:
            return jsonify({'error': 'Failed to send welcome email'}), 500
    else:
        return jsonify({'error': 'Failed to register user'}), 500


if __name__ == '__main__':
    app.run(debug=True)
