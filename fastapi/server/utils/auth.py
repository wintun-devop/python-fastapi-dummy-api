import os
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from typing import Union,Any
from jose import jwt

from server_config import (
    JWT_REFRESH_SECRET_KEY,
    JWT_SECRET_KEY,
    refresh_token_expire_minutes,
    access_token_expire_minutes,
    token_hash_algorithm
)


password_context = CryptContext(
    schemes=["argon2"],
    default="argon2",
    # tuning params — adjust to your environment after benchmarking
    # number of iterations
    argon2__time_cost=2, 
    # memory in KiB (100 MiB)      
    argon2__memory_cost=102400, 
    argon2__parallelism=8
)

access_token_expire = access_token_expire_minutes
refresh_token_expire = refresh_token_expire_minutes
jwt_secret_key = JWT_SECRET_KEY
jwt_refresh_secret_key = JWT_REFRESH_SECRET_KEY
algorithm = token_hash_algorithm

""" 
password_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
) 
 """

def hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(payload: dict, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire)
    to_encode = {"exp": expires_delta, **payload}
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm)
    return encoded_jwt


def create_refresh_token(payload: dict, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=refresh_token_expire)
    to_encode = {"exp": expires_delta, **payload}
    encoded_jwt = jwt.encode(to_encode, jwt_refresh_secret_key, algorithm)
    return encoded_jwt


def test_function()->dict:
    return {"a_key":jwt_secret_key,"r_key":jwt_refresh_secret_key,
            "r":refresh_token_expire,"a":access_token_expire,
            "l":algorithm
            }



# quick demo
if __name__ == "__main__":
    p = "s3cret!"
    h = hashed_password(p)
    print("hash:", h)
    print("verify ok:", verify_password(p, h))