from typing import List
import strawberry
from datetime import datetime
from uuid import UUID

@strawberry.type
class User:
    id: UUID
    name: str
    avatar_url: str

@strawberry.type
class Post:
    id: UUID
    title: str
    likes: int
    created_by: User
    created_utc: datetime

@strawberry.type
class UserWithPosts(User):
    posts: List[Post]
