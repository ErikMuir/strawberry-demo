from datetime import datetime, timezone
from typing import List
from uuid import UUID
from db_models import Post, User

bart_simpson = User(
        id=UUID("bb276fdd-0f96-430c-a8e1-8b7a77d5e178"),
        name="Bart Simpson",
    )

kurt_vonnegut = User(
        id=UUID("edb6c4a6-3960-4063-a056-948f4ca1e247"),
        name="Kurt Vonnegut",
    )

king_arthur = User(
        id=UUID("ab7e9005-669a-467d-88d2-a27b9cf25233"),
        name="King Arthur",
    )

barrak_obama = User(
        id=UUID("af6df0cc-8e79-47d3-9bfa-0e5fc15b22bc"),
        name="Barrak Obama",
    )

trey_anastasio = User(
        id=UUID("c0a5be09-d7b2-421e-9a91-591016280bd5"),
        name="Trey Anastasio",
    )

line_or_curve = Post(
        id=UUID("40d496a9-9759-455c-b48b-2e81d2ec615b"),
        title="Is it a Line or is it a Curve?",
        likes=2,
        created_by=trey_anastasio.id,
        created_utc=datetime(2023, 7, 4, 14, 42, 29, 443936, tzinfo=timezone.utc),
    )

antimeridian_chaos = Post(
        id=UUID("5e391293-ba04-4ff5-a4c3-f7439dfb0203"),
        title="Antimeridian Chaos",
        likes=7,
        created_by=trey_anastasio.id,
        created_utc=datetime(2023, 7, 18, 10, 4, 51, 832947, tzinfo=timezone.utc),
    )

class Db:
    def __init__(self, users: List[User], posts: List[Post]):
        self.users = users
        self.posts = posts

db = Db(
    users=[
        bart_simpson,
        kurt_vonnegut,
        king_arthur,
        barrak_obama,
        trey_anastasio,
    ],
    posts=[
        line_or_curve,
        antimeridian_chaos,
    ],
)
