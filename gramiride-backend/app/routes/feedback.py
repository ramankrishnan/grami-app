from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth.auth_bearer import oauth2_scheme
from auth.auth_handler import decode_access_token
from models.feedback import FeedbackCreate, FeedbackResponse
from controllers.feedback_controller import submit_feedback

router = APIRouter()

@router.post("/feedback", response_model=FeedbackResponse)
def give_feedback(
    feedback: FeedbackCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)
    user_id = payload.get("sub")

    result = submit_feedback(db, user_id, feedback)
    if not result:
        raise HTTPException(status_code=404, detail="Ride not found")

    return result
