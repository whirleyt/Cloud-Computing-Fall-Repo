from flask import Flask, jsonify, request
import requests
from pydantic import BaseModel
import jwt
import datetime
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


MESSAGES_URL = 'https://76t5n28kf3.execute-api.us-east-1.amazonaws.com/develop/messages-microservice'

PAGE_SIZE = 10

secret_key = 'cc-columni-23'

payload = {
    'sub': 'user1',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
}




class MessageModel(BaseModel):
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "userMessageID": 1,
          "userID": 1,
          "messageThreadID": 1,
          "messageContents": "Hi! (Potentially Encrypted).",
          "creationDT": "10/3/23 16:25"
        }
      ]
    }
  }

def __init__(self, user_message_id: int, user_id: int, message_id: int, message_contents: str, creation_dt: str):
    self.user_message_id = user_message_id
    self.user_id = user_id
    self.message_id = message_id
    self.message_contents = message_contents
    self.creation_dt = creation_dt

@app.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    print(f"Request URL: {MESSAGES_URL}/api/messages/1")
    try:
        payload = {
            'sub': 'user1',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }

        jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')

        headers = {'Authorization': f'Bearer {jwt_token}'}
        response = requests.get(
            f"{MESSAGES_URL}/api/messages/1",
            headers=headers
        )
        response.raise_for_status()
        print("Response from microservice:", response.json())
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        print("Request Exception:", e)
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/api/messages/newMessage/<int:user_id>', methods=['POST'])
def new_message(user_id):
    request_data = request.json
    request_data["user_id"] = user_id
    response = requests.post(f"{MESSAGES_URL}api/messages/newMessage", json=request_data)

    return jsonify(response.json()), response.status_code

@app.route('/api/messages/<int:user_id>/<int:thread_id>', methods=['GET'])
def get_thread_messages(user_id, thread_id):
  # Implement logic to retrieve and display messages for a specific thread
  page = request.args.get('page', 1, type=int)
  offset = (page - 1) * PAGE_SIZE

  response = requests.get(
    MESSAGES_URL + f'api/messages?userID={user_id}&messageThreadID={thread_id}&offset={offset}&limit={PAGE_SIZE}"'
  )

  return response.json()


# Run the application
if __name__ == '__main__':
  app.run(debug=True)
