
import jwt, time, os
from fastapi import HTTPException

SECRET = os.getenv("JWT_SECRET","secret")

def login(data):
    token = jwt.encode(
        {"user": data["username"], "exp": time.time()+86400},
        SECRET,
        algorithm="HS256"
    )
    return {"token": token}

def verify_token(token: str = None):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(401,"Unauthorized")
