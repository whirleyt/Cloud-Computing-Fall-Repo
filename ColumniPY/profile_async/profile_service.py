from flask import Flask, jsonify, request
import requests
from pydantic import BaseModel
import jwt
import datetime
from flask_cors import CORS
import asyncio
import aiohttp
import time

app = Flask(__name__)

CORS(app)


MESSAGES_URL = 'https://76t5n28kf3.execute-api.us-east-1.amazonaws.com/develop/messages-microservice'

PAGE_SIZE = 10

secret_key = 'cc-columni-23'

payload = {
    'sub': 'user1',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
}


class Request(BaseModel):
  name: str


class RequestResource:
  #
  # These endpoints are on Prof. Ferguson's SwaggerHub mock APIs
  #
  resources = [
      {
          "resource": "messages",
          "url": 'https://messages-microservice.ue.r.appspot.com/api/messages'
      },
      {
          "resource": "users",
          "url": 'https://messages-microservice.ue.r.appspot.com/api/users'
      },
      {
          "resource": "posts",
          "url": 'https://ecbm4040-spr2139.uc.r.appspot.com/api/posts'
      }
  ]

  @classmethod
  async def fetch(cls, session, resource):
      url = resource["url"]
      print("Calling URL = ", url)
      async with session.get(url) as response:
          t = await response.json()
          print("URL ", url, "returned", str(t))
          result = {
              "resource": resource["resource"],
              "data": t
          }
      return result

async def get_resources_async():
    full_result = None
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(
            RequestResource.fetch(session, res)) for res in RequestResource.resources]
        responses = await asyncio.gather(*tasks)
        full_result = {}
        for response in responses:
            full_result[response["resource"]] = response["data"]
        end_time = time.time()
        full_result["elapsed_time"] = end_time - start_time

        return full_result


async def get_resources_sync():
    full_result = None
    start_time = time.time()

    full_result = {}

    for r in RequestResource.resources:
        response = requests.get(r["url"])
        print("Received: " + r["resource"])
        full_result[r["resource"]] = response.json()
    end_time = time.time()
    full_result["elapsed_time"] = end_time - start_time

    return full_result



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

@app.route('/api/profile_sync', methods=['GET'])
def get_profile_messages_sync():
  # Implement logic to retrieve and display messages for a specific thread

  response = asyncio.run(get_resources_sync())

  return response

@app.route('/api/profile_async', methods=['GET'])
def get_profile_messages_async():
  # Implement logic to retrieve and display messages for a specific thread

  response = asyncio.run(get_resources_async())

  return response


# Run the application
if __name__ == '__main__':
  app.run(debug=True)
