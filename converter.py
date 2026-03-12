from docx import Document

def convert_docx_to_html(file_path):

    doc = Document(file_path)
    html = ""

    for para in doc.paragraphs:

        text = para.text.strip()

        if not text:
            continue

        style = para.style.name

        if "Heading 1" in style:
            html += f"<h1>{text}</h1>\n"

        elif "Heading 2" in style:
            html += f"<h2>{text}</h2>\n"

        elif "Heading 3" in style:
            html += f"<h3>{text}</h3>\n"

        elif "List Bullet" in style:
            html += f"<ul><li>{text}</li></ul>\n"

        elif "List Number" in style:
            html += f"<ol><li>{text}</li></ol>\n"

        else:
            html += f"<p>{text}</p>\n"

    return html