import jwt
import json


def decode_jwt(jwt_string:str)->dict:
    token = jwt_string
    # 2. Extract header without verifying signature
    header = jwt.get_unverified_header(token)
    print("Header:")
    print(json.dumps(header, indent=4)) 
    
    # 3. Decode payload without verifying signature
    payload = jwt.decode(token, options={"verify_signature": False})
    result = json.dumps(payload, indent=4)
    # print("\nPayload:")
    # print(result)
    return result

# quick demo
if __name__ == "__main__":
    tk = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjgwNjAyNzIsImlkIjoiM2VmMjIzZGQtYWUwMi00YjY4LWIxMTktMDZlNzdmMTI1N2VlIiwicm9sZSI6InVzZXIifQ.zpUJ2we4XNOQdtN-L-GSUIYdOFEHXBJIRgQbcE6Q124"
    r = decode_jwt(tk)
    print("token_decode:", r)


