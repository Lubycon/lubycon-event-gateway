from typing import Any

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/")
def collect_event() -> Any:
    """
    Retrieve items.
    """

    return {"message": "success"}
