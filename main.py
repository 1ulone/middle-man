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
    ref = db.reference("/device_data")
    # Push data to Firebase
    new_ref = ref.push(data)
    return {"ok": True, "firebase_key": new_ref.key}

