from fastapi import FastAPI, Request, HTTPException
import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": os.environ["FIREBASE_DB_URL"]
})

app = FastAPI()

@app.post("/upload")
async def upload(req: Request):
    data = await req.json()

    ref = db.reference("d01")
    ref.push(data)

    return {"output": "masuk"}

