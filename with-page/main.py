from flask import Flask, request, jsonify
import pyttsx3
import PyPDF2
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return "No file uploaded", 400

    pdf_file = request.files['pdf']
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Initialize text-to-speech
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()

        return "Success", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)