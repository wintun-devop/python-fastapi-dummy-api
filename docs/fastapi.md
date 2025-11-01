### virtual env setup
```
python -m venv fastapi_env
```
```
fastapi_env\Scripts\activate
```

### Installing Necessary Pacakges
- installs FastAPI plus a curated set of optional, commonly‑used dependencies so a development/production experience works out of the box.
```
pip install "fastapi[standard]"
```
### installing database packages
```
pip install sqlalchemy[asyncio] asyncpg
```


### Auth Modules
```
pip install python-jose[cryptography] passlib[argon2] python-multipart
```

### running app
```
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Openssl Command for generate secret key
```
openssl rand -base64 32
```
