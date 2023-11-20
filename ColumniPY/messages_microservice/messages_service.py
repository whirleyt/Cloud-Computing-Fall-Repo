from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect('https://messages-microservice.ue.r.appspot.com/')
cur = conn.cursor()

PAGE_SIZE = 10

# API Routes
@app.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    page = request.args.get('page', 1, type=int)

    offset = (page - 1) * PAGE_SIZE

    query = """
            SELECT * FROM messages
            WHERE user_id = %s
            ORDER BY timestamp DESC
            LIMIT %s OFFSET %s
        """
    cur.execute(query, (user_id, PAGE_SIZE, offset))
    messages = cur.fetchall()
    return jsonify({"messages": messages})


@app.route('/api/messages/<int:user_id>/newMessage', methods=['POST'])
def new_message(user_id):
    # Implement logic to create a new message for a user
    return jsonify({"message": f"New message created for user {user_id}"})


@app.route('/api/messages/<int:user_id>/<int:thread_id>', methods=['GET'])
def get_thread_messages(user_id, thread_id):
    # Implement logic to retrieve and display messages for a specific thread
    return jsonify({"message": f"Displaying messages for user {user_id} in thread {thread_id}"})


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
