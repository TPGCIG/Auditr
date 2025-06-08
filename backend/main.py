import os
from dotenv import load_dotenv # type: ignore

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=["POST"])
def upload():

    pdf = request.files["file"]
    # if no file given / no name / no file.
    if not pdf or not pdf.filename:
        return jsonify(message="No file found!"), 400

    # obv
    if not pdf.filename.endswith(".pdf"):
        return jsonify(message="Not a pdf"), 400

    # clean and save the file
    filename = secure_filename(pdf.filename)
    pdf.save(os.path.join("uploads", filename))

    # return success
    return jsonify(message="Successfully uploaded pdf!")

@app.route('/api/result', methods=["GET"])
def result():


    return jsonify()


if __name__ == "__main__":
    app.run(debug=True, port=5000)










