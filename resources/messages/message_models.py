from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class MessageModel(BaseModel):
    userMessageID: str
    userID: str
    messageID: str
    messageContent: str
    timestamp: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "userMessageID": "1",
                    "userID": "1",
                    "messageID": "1",
                    "messageContent": "Hi! (Potentially Encrypted).",
                    "timestamp": "10/3/23 16:25"
                }
            ]
        }
    }


class MessageRspModel(MessageModel):
    links: List[Link] = None



