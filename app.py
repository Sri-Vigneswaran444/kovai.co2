from flask import Flask, render_template
from converter import convert_docx_to_html
from uploader import upload_to_document360

app = Flask(__name__)

@app.route("/")
def index():

    # Updated file name
    file_path = "vickytest.docx"

    # Convert Word → HTML body
    html_body = convert_docx_to_html(file_path)

    # Create full HTML skeleton
    html_file = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Migration Preview</title>
</head>

<body>

{html_body}

</body>
</html>
"""

    # Save preview locally
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_file)

    # Read saved file
    with open("output.html", "r", encoding="utf-8") as f:
        saved_html = f.read()

    # Upload saved HTML
    response = upload_to_document360(saved_html)

    return render_template(
        "index.html",
        html_content=html_body,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)