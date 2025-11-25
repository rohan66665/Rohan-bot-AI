# app/router_chat.py
import traceback
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag_pipeline import get_context, answer_rag

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(body: ChatRequest) -> ChatResponse:
    try:
        query = body.query.strip()
        if not query:
            return ChatResponse(answer="⚠️ Please enter a valid message.")

        context, sources = get_context(query)

        if not context:
            return ChatResponse(
                answer="📌 No relevant data found in uploaded docs. Pehle PDF / image upload karo."
            )

        response = answer_rag(query, context) or "⚠️ No answer available."
        return ChatResponse(answer=response)

    except Exception:
        print("❌ Chat error:", traceback.format_exc())
        raise HTTPException(status_code=500, detail="Chat failed")
