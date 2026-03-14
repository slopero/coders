import fitz

def read_pdf(filename: str):
    try:
        doc = fitz.open(filename)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.lower()
    except Exception as e:
        print(f"Ошибка при чтении файла {e}")
        return None
    

