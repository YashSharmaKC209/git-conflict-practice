from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Backend",
        "status": "staging"
    }


@app.get("/users")
def get_users():
    return {
        "users": ["Yash", "Aman", "Naman"]
    }


@app.get("/health")
def health_check():
    return {
        "health": "ok"
    }
