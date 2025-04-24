from fastapi import Depends, HTTPException
from auth.auth_bearer import oauth2_scheme
from auth.auth_handler import decode_access_token
from database import get_user_by_phone

def admin_required(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    user = get_user_by_phone(payload["sub"])
    if not user or user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user
