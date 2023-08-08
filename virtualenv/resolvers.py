from typing import List
from uuid import UUID
from db import db
from db_models import Post as dbPost, User as dbUser
from graphql_models import Post as gqlPost, User as gqlUser, UserWithPosts as gqlUserWithPosts

def get_users():
    return map(lambda user: __map_user(user), db.users)

def get_posts():
    return map(lambda post: __map_post(post), db.posts)

def get_user(id: str):
    for _, item in enumerate(db.users):
        if item.id == UUID(id):
            return __map_user(item)
    return None

def get_post(id: str):
    for _, item in enumerate(db.posts):
        if item.id == UUID(id):
            return __map_post(item)
    return None

def get_posts_by_author(id: str) -> List[gqlPost]:
    posts: List[gqlPost] = []
    for _, item in enumerate(db.posts):
        if item.created_by == UUID(id):
            posts.append(__map_post(item))
    return posts

def get_user_with_posts(id: str) -> gqlUserWithPosts:
    user = get_user(id)
    posts = get_posts_by_author(id)
    return gqlUserWithPosts(
        id=user.id,
        name=user.name,
        avatar_url=user.avatar_url,
        posts=posts
    )

def __map_user(dbu: dbUser) -> gqlUser:
    return gqlUser(
        id=dbu.id,
        name=dbu.name,
        avatar_url=f"https://ui-avatars.com/api/?name={dbu.name.replace(' ', '+')}",
    )

def __map_post(dbp: dbPost) -> gqlPost:
    return gqlPost(
        id=dbp.id,
        title=dbp.title,
        likes=dbp.likes,
        created_by=get_user(str(dbp.created_by)),
        created_utc=dbp.created_utc
    )
