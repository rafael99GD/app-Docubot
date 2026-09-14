# 🤖 DocuBot

Bot de Telegram que recibe un documento (PDF o .txt), lo resume con IA y guarda el histórico de interacciones en PostgreSQL.

Proyecto hecho para practicar exactamente el tipo de herramienta que construyen los equipos de IA aplicada a procesos internos: **extracción de documentos + asistente conversacional + IA generativa**, con backend en FastAPI en vez de Spring Boot, para ampliar stack más allá de Java.

## Cómo funciona

1. El usuario envía un PDF o .txt al bot por Telegram.
2. FastAPI recibe la actualización vía webhook (`POST /webhook/telegram`).
3. Se descarga el archivo desde la API de Telegram y se extrae el texto (`pdfplumber` para PDFs).
4. El texto se envía a la API de Gemini (Google) pidiendo un resumen + puntos clave.
5. El resumen se devuelve al usuario por Telegram.
6. Cada interacción (usuario, documento, resumen) se guarda en PostgreSQL.

## Stack

- **FastAPI** — framework backend, expone el webhook de Telegram
- **PostgreSQL** (vía Docker) — persistencia del histórico
- **SQLAlchemy** — ORM
- **Google Gemini API** (gratis) — generación del resumen
- **pdfplumber** — extracción de texto de PDFs
- **httpx** — cliente HTTP para hablar con la API de Telegram

## Cómo ejecutarlo

### 1. Configura las variables de entorno

```bash
cp .env.example .env
```

Rellena `TELEGRAM_BOT_TOKEN` (créalo hablando con [@BotFather](https://t.me/BotFather) en Telegram) y `GEMINI_API_KEY` (gratis, sin tarjeta, desde [aistudio.google.com/apikey](https://aistudio.google.com/apikey)).

### 2. Levanta todo con Docker

```bash
docker compose up --build
```

Esto levanta PostgreSQL y la API en `http://localhost:8000`.

### 3. Conecta el webhook de Telegram

Necesitas una URL pública (con `ngrok` en local, por ejemplo):

```bash
ngrok http 8000
curl "https://api.telegram.org/bot<TU_TOKEN>/setWebhook?url=https://<tu-url-ngrok>/webhook/telegram"
```

### 4. Pruébalo

Mándale un PDF a tu bot por Telegram y en unos segundos te responde con el resumen.

## Sin Docker (desarrollo local)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

(Necesitas una instancia de PostgreSQL accesible en la `DATABASE_URL` que configures).

## Próximas mejoras

- Soportar más formatos (`.docx`, imágenes con OCR)
- Endpoint para consultar el histórico de un usuario
- Botones interactivos de Telegram para pedir "más detalle" o "solo los puntos clave"
- Tests con `pytest`

---
Proyecto personal de Rafael, para explorar Python/FastAPI + IA aplicada más allá de su stack principal (Java/Spring Boot).
