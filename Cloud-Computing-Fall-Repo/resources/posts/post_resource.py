from resources.abstract_base_resource import BaseResource
from resources.messages.message_models import PostRspModel, PostModel
from resources.rest_models import Link
from typing import List


class PostResource(BaseResource):
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    def __init__(self, config):
        super().__init__()

        self.data_service = config["data_service"]

    self.posts.append(SchoolRspModel(userId="1",
                                       postId="1", postContent="....",dateOfCreation="09/15/23 14:33"))
    self.posts.append(SchoolRspModel(userId="2",
                                       postId="2", postContent="....",dateOfCreation="10/15/23 16:56"))
    self.posts.append(SchoolRspModel(userId="3",
                                       postId="3", postContent="....",dateOfCreation="10/14/23 9:25"))
    self.posts.append(SchoolRspModel(userId="4",
                                       postId="4", postContent="....",dateOfCreation="08/16/23 10:44"))
    self.posts.append(SchoolRspModel(userId="1",
                                       postId="5", postContent="....",dateOfCreation="11/15/23 18:15"))

    for s in self.posts:
        s.links = [
            Link(rel="users", href="/posts/" + s.userId + "/users"),
            Link(rel="self", href="/posts/" + s.userId)
        ]


    def get_posts(self, uni: str = None, last_name: str = None, school_code: str = None, post_id: str = None) -> List[PostRspModel]:

        result = self.data_service.get_posts(uni, first_name, last_name, school_code, post_id)
        final_result = []

        for s in result:
            m = self._generate_links(s)
            final_result.append(m)

        return final_result

