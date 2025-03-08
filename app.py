from flask import Flask, request, render_template
import joblib
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = joblib.load('digit_recognition_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    if file.filename == '':
        return "No file selected"

    if file:
        # Process the image
        image = Image.open(file).convert('L')
        image = image.resize((28, 28))
        image = np.array(image).reshape(1, -1) / 255.0

        # Predict the digit
        prediction = model.predict(image)
        return render_template('index.html', prediction=int(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)