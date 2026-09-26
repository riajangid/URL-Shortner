from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import get_db
from services.url_services import get_long_url


router = APIRouter(
    tags=["Redirect"]
)


@router.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    long_url = get_long_url(
        db,
        short_code
    )

    if not long_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(
        url=long_url,
        status_code=307
    )