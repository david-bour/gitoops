from fastapi import FastAPI
from datetime import datetime
from opentelemetry import trace

tracer = trace.get_tracer("app.api")

app = FastAPI()

@app.get("/")

def root():
    with tracer.start_as_current_span("root") as span:
        the_time = str(datetime.now())
        span.set_attribute("the_time", the_time)
        return {"the_time": f"Today is {the_time}"}
