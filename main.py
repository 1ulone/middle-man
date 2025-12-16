from fastapi import FastAPI, Request
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://your-project.firebaseio.com"
})

app = FastAPI()

@app.post("/upload")
async def upload(req: Request):
    data = await req.json()

    ref = db.reference("devices/a9g_01")
    ref.push(data)

    return {"status": "ok"}

