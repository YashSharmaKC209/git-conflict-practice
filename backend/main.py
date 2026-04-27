from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Backend",
        "status": "running"
    }


@app.get("/users")
def get_users():
    return {
        "users": ["Yash", "Aman", "Naman"]
    }