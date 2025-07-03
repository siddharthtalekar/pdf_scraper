from fastapi import APIRouter, Request, UploadFile, Form
from fastapi.responses import HTMLResponse
from app.services.pdf_processor import extract_text_from_pdf
from app.services.embedding import embed_and_store
from app.services.query_handler import answer_query
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload/")
async def upload_pdf(file: UploadFile):
    text = await extract_text_from_pdf(file)
    embed_and_store(text, file.filename)
    return {"message": "PDF uploaded and stored successfully"}

@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        answer = answer_query(question)
        return {"answer": answer}
    except Exception as e:
        print("ERROR in answer_query:", e)
        return {"answer": "Error processing your question. Please try again."}
