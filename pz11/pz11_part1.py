from fastapi import FastAPI

#pip install fastapi[all]
#uvicorn pz11\pz11_part1:api --reload

app = FastAPI()
@app.get("/")
def my_study():
    return "I study FastAPI"