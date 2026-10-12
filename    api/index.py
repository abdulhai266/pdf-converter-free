from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pdf2docx import Converter
import shutil

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/index")
@app.post("/")
async def convert(file: UploadFile):
    inp = f"/tmp/{file.filename}"
        out = inp.replace(".pdf",".docx")
            with open(inp,"wb") as f: shutil.copyfileobj(file.file,f)
                cv = Converter(inp)
                    cv.convert(out)
                        cv.close()
                            return FileResponse(out, filename=file.filename.replace(".pdf",".docx"))

                            @app.get("/")
                            def home():
                                return {"status": "API is Running"}