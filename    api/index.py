from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import os, shutil, traceback

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"status": "ok", "message": "API is running"}

    @app.post("/")
    async def convert(file: UploadFile = File(...)):
        try:
                from pdf2docx import Converter
                        in_path = "/tmp/input.pdf"
                                out_path = "/tmp/output.docx"
                                        with open(in_path, "wb") as f:
                                                    shutil.copyfileobj(file.file, f)
                                                            cv = Converter(in_path)
                                                                    cv.convert(out_path)
                                                                            cv.close()
                                                                                    return FileResponse(out_path, filename=file.filename.replace(".pdf",".docx"))
                                                                                        except Exception as e:
                                                                                                return JSONResponse(status_code=500, content={"error": str(e), "trace": traceback.format_exc()})