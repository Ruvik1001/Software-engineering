from datetime import datetime, timedelta, timezone
import jwt

SECRET = "lab2-super-secret-key-for-jwt-signing-2026"
ALGO = "HS256"

def encode_token(payload: dict, expires_minutes: int) -> str:
    data = payload.copy()
    data["exp"] = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    return jwt.encode(data, SECRET, algorithm=ALGO)

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=[ALGO])
