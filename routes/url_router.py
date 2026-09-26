from models.long_url import Long_URL
from models.short_url import Short_URL
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from database import get_db
from schemas import URLCreate
from services.url_services import (
    create_short_url,
    get_long_url
)
from core.dependencies import get_current_user


router = APIRouter(
    prefix="/urls",
    tags=["URLs"]
)


@router.post("/")
def create_url(
    data: URLCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        url = create_short_url(
            db,
            data,
            current_user.id
        )

        return {
            "short_code": url.short_code,
            "short_url": (
                f"http://localhost:8000/"
                f"{url.short_code}"
            ),
            "long_url": url.long_url
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )