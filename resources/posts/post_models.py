from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class PostModel(BaseModel):

    userID: str
    postID: str
    postContent: str
    dateOfCreation: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "userID": "1",
                    "postID": "1",
                    "postContent": "Hey, so excited to connect after so long!",
                    "dateOfCreation": "09/15/23 14:33"
                }
            ]
        }
    }


class PostRspModel(PostModel):
    links: List[Link] = None



