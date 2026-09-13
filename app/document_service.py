from io import BytesIO

import pdfplumber


def extract_text(file_bytes: bytes, filename: str) -> str:
    """Extrae el texto de un PDF o un .txt. Devuelve cadena vacía si no se puede procesar."""
    if filename.lower().endswith(".pdf"):
        text_parts = []
        with pdfplumber.open(BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n".join(text_parts)

    if filename.lower().endswith(".txt"):
        return file_bytes.decode("utf-8", errors="ignore")

    return ""
