from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

PDF_DIRECTORY = 'pdfs'

os.makedirs(PDF_DIRECTORY, exist_ok=True)

@app.route('/')
def index():
    # List PDF files in the directory
    pdf_files = os.listdir(PDF_DIRECTORY)
    pdf_links = [f"<li><a href='/pdf/{file}'>{file}</a></li>" for file in pdf_files if file.endswith('.pdf')]
    return render_template_string("""
    <!doctype html>
    <title>PDF File Server</title>
    <h1>PDF Files</h1>
    <ul>
        {{ pdf_links|safe }}
    </ul>
    """, pdf_links=''.join(pdf_links))

@app.route('/pdf/<path:filename>')
def serve_pdf(filename):
    return send_from_directory(PDF_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(debug=True)
