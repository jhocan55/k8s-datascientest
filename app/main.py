from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/users")
def get_users():
    # Example: Replace with actual database query logic
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.get("/users/count")
def count_users():
    # Example: Replace with actual database query logic
    return {"count": 2}
