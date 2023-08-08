from typing import List
import strawberry
import resolvers
from graphql_models import User, Post, UserWithPosts

@strawberry.type
class Query:
    users: List[User] = strawberry.field(resolver=resolvers.get_users)
    posts: List[Post] = strawberry.field(resolver=resolvers.get_posts)
    user: User = strawberry.field(resolver=resolvers.get_user)
    post: Post = strawberry.field(resolver=resolvers.get_post)
    user_with_posts: UserWithPosts = strawberry.field(resolver=resolvers.get_user_with_posts)

schema = strawberry.Schema(query=Query)
