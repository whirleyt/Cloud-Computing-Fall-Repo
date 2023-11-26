from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

POSTS_URL = 'https://posts-microservice.ue.r.appspot.com/'

PAGE_SIZE = 10

class PostModel(BaseModel):
    userPostID: int
    userID: int
    postID: int
    postThreadID: int
    postContent: str
    dateOfCreation: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
           
                    "userPostID":1,
                    "userID": 1,
                    "postID": 1,
                    "postThreadID": 1,
                    "postContent": "Hey, so excited to connect after so long!",
                    "dateOfCreation": "09/15/23 14:33"
                }
            ]
        }
    }

# API Routes
@app.route('/api/posts/<int:user_id>', methods=['GET'])
def get_posts(user_id):
    offset = (page - 1) * PAGE_SIZE
    return requests.get(POSTS_URL+'api/posts?userID='+str(user_id)+'&offset='+str(offset)+'&limit=10').json


@app.route('/api/posts/newPost', methods=['POST'])
def new_post(request: postModel, user_id):
    # Icreate a new post for a user
    return requests.post(POSTS_URL+'api/posts/newPost', json = request)


@app.route('/api/posts/<int:user_id>/<int:thread_id>', methods=['GET'])
def get_thread_posts(user_id, thread_id):
    # etrieve and display post for a specific thread
    return requests.get(POSTS_URL+'api/posts?userID='+str(user_id)+'&postThreadID='+str(thread_id)+'&offset='+str(offset)+'&limit=10').json


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
