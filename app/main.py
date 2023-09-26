from fastapi import FastAPI
from time import sleep

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/stress/{seconds}")
def stress_cpu(seconds: int):
    start_time = time.time()
    # Simulate CPU intensive computation
    while True:
        # Some computation
        _ = [x * x for x in range(1000)]
        elapsed_time = time.time() - start_time
        if elapsed_time > seconds:
            break
    return {"status": "done"}
