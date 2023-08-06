from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def print_hello():
    return {"data": "Hellow Worldo.."}



def run():
    run_myapp = uvicorn.run(app)
    return run_myapp


if __name__ == "__main__":
    run()