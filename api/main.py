from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")

def root():
    return {"the_time": f"Today is {str(datetime.now())}"}
