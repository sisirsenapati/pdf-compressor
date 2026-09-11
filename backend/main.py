from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import pikepdf
import tempfile
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/compress")
async def compress_pdf(file: UploadFile = File(...)):

    input_path = tempfile.mktemp(".pdf")
    output_path = tempfile.mktemp(".pdf")

    with open(input_path, "wb") as f:
        f.write(await file.read())

    pdf = pikepdf.Pdf.open(input_path)

    pdf.save(
        output_path,
        compress_streams=True,
        object_stream_mode=pikepdf.ObjectStreamMode.generate
    )

    pdf.close()

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="compressed.pdf"
    )


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)