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

### running app
```
uvicorn app:app --reload
```
