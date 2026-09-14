from google import genai
from google.genai import types

from app.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

# Límite de caracteres para no disparar el tamaño de la petición en el demo
MAX_CHARS = 12000

SYSTEM_PROMPT = (
    "Eres un asistente que resume documentos de forma clara y concisa en español. "
    "Devuelve siempre: 1) un resumen de 3-4 frases, y 2) una lista de 3-5 puntos clave. "
    "Sé directo, sin relleno."
)


def summarize_document(text: str) -> str:
    if not text.strip():
        return "No he podido extraer texto de ese documento. ¿Puedes probar con otro archivo?"

    truncated = text[:MAX_CHARS]

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Resume este documento:\n\n{truncated}",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            max_output_tokens=2048,
        ),
    )
    return response.text
