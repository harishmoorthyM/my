from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']

    # Check if the file is a PDF
    if file.filename.endswith('.pdf'):
        try:
            # Read PDF content
            pdf_reader = PdfReader(file)
            extracted_text = ''
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()
            
            return render_template('index.html', extracted_text=extracted_text)
        
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    else:
        return "Uploaded file is not a PDF", 400

if __name__ == '__main__':
    app.run(debug=True)
