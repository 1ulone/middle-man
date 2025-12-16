from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/upload")
async def upload(request: Request):
    data = await request.json()
    print("Received from A9G:", data)
    return {"ok": True}

# import os
# import base64
# import tempfile
# from fastapi import FastAPI, Request
# import firebase_admin
# from firebase_admin import credentials, db
#
# # Decode base64 service account and write to a temporary file
# sa_json_base64 = os.environ["FIREBASE_SA_BASE64"]  # your env var
# sa_json_bytes = base64.b64decode(sa_json_base64)
#
# with tempfile.NamedTemporaryFile(delete=False) as f:
#     f.write(sa_json_bytes)
#     tmp_path = f.name
#
# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(tmp_path)
# firebase_admin.initialize_app(cred, {
#     "databaseURL": os.environ["FIREBASE_DB_URL"]
# })
#
# app = FastAPI()
#
# @app.post("/upload")
# async def upload(req: Request):
#     data = await req.json()
#
#     #ref = db.reference("d01")
#     #ref.push(data)
#
#     return {"ok": True}
