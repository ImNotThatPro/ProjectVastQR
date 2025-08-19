from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def root():
    return {'message': 'Hello from VastQR backend'}

@app.post('/api/qr')
async def generate_qr(request: Request):
    data = await request.json()
    print("Received on backend:", data, flush=True)
    return {'result': f'Received: {data}'}

@app.post('/api/upload')
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {'filename': file.filename, 'size': len(contents)}