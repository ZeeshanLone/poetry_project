from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "You have reached root"}


@app.get("/user")
async def user():
    return {"message", "Hello user2..."}
