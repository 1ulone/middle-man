import os
import base64
import json
from fastapi import FastAPI, Request
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Initialize Firebase
if not firebase_admin._apps:
    sa_json = base64.b64decode(os.environ["FIREBASE_SA_BASE64"])
    cred = credentials.Certificate(json.loads(sa_json))
    firebase_admin.initialize_app(cred, {
        "databaseURL": os.environ["FIREBASE_DB_URL"]
    })

@app.post("/upload")
async def upload(request: Request):
    data = await request.json()
    ref = db.reference("/latest_data")
    ref.set(data)
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )
