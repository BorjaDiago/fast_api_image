from fastapi import FastAPI

# Run the app executing this command --> uvicorn main:app --reload
app = FastAPI()


@app.get("/hello")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello_name(name: int) -> dict:
    return {"message": f"Hello {name}"}
