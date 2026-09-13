from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Interaction
from app import telegram_service, document_service, ai_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DocuBot")


@app.get("/")
def health_check():
    return {"status": "ok", "service": "DocuBot"}


@app.post("/webhook/telegram")
async def telegram_webhook(update: dict, db: Session = Depends(get_db)):
    message = update.get("message")
    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    document = message.get("document")

    if not document:
        await telegram_service.send_message(
            chat_id, "Envíame un PDF o un .txt y te devuelvo un resumen con los puntos clave."
        )
        return {"ok": True}

    filename = document.get("file_name", "documento")
    file_path = await telegram_service.get_file_path(document["file_id"])
    file_bytes = await telegram_service.download_file(file_path)

    text = document_service.extract_text(file_bytes, filename)
    summary = ai_service.summarize_document(text)

    await telegram_service.send_message(chat_id, summary)

    db.add(Interaction(telegram_user_id=chat_id, document_name=filename, summary=summary))
    db.commit()

    return {"ok": True}
