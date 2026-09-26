import secrets
import string

from sqlalchemy.orm import Session

from models.long_url import Long_URL
from models.short_url import Short_URL
from schemas import URLCreate


def generate_short_code(length: int = 6):

    characters = (
        string.ascii_letters +
        string.digits
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def create_short_url(
    db: Session,
    data: URLCreate,
    user_id: int
):

    if data.custom_alias:

        existing = (
            db.query(Long_URL)
            .filter(
                Long_URL.short_code == data.custom_alias
            )
            .first()
        )

        if existing:
            raise ValueError(
                "Custom alias already exists"
            )

        short_code = data.custom_alias

    else:

        while True:

            short_code = generate_short_code()

            existing = (
                db.query(Short_URL)
                .filter(
                    Short_URL.short_code == short_code
                )
                .first()
            )

            if not existing:
                break

    url = Short_URL(
        long_url=str(data.long_url),
        short_code=short_code,
        custom_alias=data.custom_alias,
        expiry=data.expiry,
        user_id=user_id
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    # # Cache immediately
    # cache_url(
    #     short_code,
    #     url.long_url
    # )

    return url


def get_long_url(
    db: Session,
    short_code: str
):

    # # Redis first
    # cached_url = get_cached_url(short_code)

    # if cached_url:
    #     return cached_url

    # SQLite
    url = (
        db.query(Short_URL)
        .filter(Short_URL.short_code == short_code)
        .first()
    )

    if not url:
        return None

    # # Put into Redis
    # cache_url(
    #     short_code,
    #     url.long_url
    # )

    return url.long_url