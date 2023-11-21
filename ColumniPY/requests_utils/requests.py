from pydantic import BaseModel
import asyncio
import aiohttp
import json
import time
import requests


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
            "url": 'http://ec2-3-217-79-42.compute-1.amazonaws.com:8011/api/userProfile'
        },
        {
            "resource": "posts",
            "url": 'https://icy-tree-030c60010.4.azurestaticapps.net/api/posts'
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

    async def get_resources_async(self):
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


    async def get_resources_sync(self):
        full_result = None
        start_time = time.time()

        full_result = {}

        for r in RequestResource.resources:
            response = requests.get(r["url"])
            full_result[r["resource"]] = response.json()
        end_time = time.time()
        full_result["elapsed_time"] = end_time - start_time

        return full_result
