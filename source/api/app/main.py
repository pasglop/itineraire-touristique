import os
import dotenv
import uvicorn

dotenv.load_dotenv()

API_HOST = 'localhost'
API_PORT = 8000

if __name__ == "__main__":
    uvicorn.run("source.api.app.app:app", host=API_HOST, port=API_PORT, reload=True)
