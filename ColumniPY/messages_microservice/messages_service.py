from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

MESSAGES_URL = 'https://messages-microservice.ue.r.appspot.com/'

PAGE_SIZE = 10

class MessageModel(BaseModel):
    userMessageID: int
    userID: int
    messageID: int
    messageContents: str
    creationDT: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "userMessageID": 1,
                    "userID": 1,
                    "messageID": 1,
                    "messageContents": "Hi! (Potentially Encrypted).",
                    "creationDT": "10/3/23 16:25"
                }
            ]
        }
    }

# API Routes
@app.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    offset = (page - 1) * PAGE_SIZE
    return requests.get(MESSAGES_URL+'api/messages?userID='+str(user_id)+'&offset='+str(offset)+'&limit=10').json


@app.route('/api/messages/newMessage', methods=['POST'])
def new_message(request: MessageModel, user_id):
    # Implement logic to create a new message for a user
    return requests.post(MESSAGES_URL+'api/messages/newMessage', json = request)


@app.route('/api/messages/<int:user_id>/<int:thread_id>', methods=['GET'])
def get_thread_messages(user_id, thread_id):
    # Implement logic to retrieve and display messages for a specific thread
    return requests.get(MESSAGES_URL+'api/messages?userID='+str(user_id)+'&messageThreadID='+str(thread_id)+'&offset='+str(offset)+'&limit=10').json


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
