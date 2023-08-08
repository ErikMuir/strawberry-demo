from datetime import datetime
from uuid import UUID

class User:
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name

class Post:
    def __init__(self, id: UUID, title: str, likes: int, created_by: UUID, created_utc: datetime):
        self.id = id
        self.title = title
        self.likes = likes
        self.created_by = created_by
        self.created_utc = created_utc

