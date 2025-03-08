# Handwritten Digit Recognition Web Application

📖 **Project Description**

This is a **Handwritten Digit Recognition Web Application** built using **Flask** (Python Web Framework) and trained on the **MNIST dataset**. The app uses a pre-trained Machine Learning model to predict handwritten digits (0-9) from uploaded images.

The model was trained using a **Google Colab** and then integrated into a **Flask Web App**. The primary purpose of this project is to demonstrate the power of **Computer Vision** and **Machine Learning** in recognizing handwritten digits.

---

## 💻 **Technologies Used**

- **Python 3.10+**
- **Flask** (Web Framework)
- **Scikit-learn** (Machine Learning Library)
- **Joblib** (Model Serialization)
- **Pillow** (Image Processing)
- **HTML/CSS** (Frontend)

---

## 💾 **Dataset Used**

- **Dataset**: MNIST (Modified National Institute of Standards and Technology)
- **Size**: 70,000 images (60,000 for training, 10,000 for testing)
- **Resolution**: 28x28 pixels (Grayscale)
- **Classes**: 10 (Digits from 0 to 9)
- **File Used**: `mnist_784.zip` (compressed dataset)

---

## 📊 **Model Accuracy**

The model was trained using **Random Forest** and achieved the following accuracy:

- **Training Accuracy**: **96%**

---

## 💻 **How To Run This Project**

### ✅ **Step 1: Clone This Repository**

Open your terminal or command prompt and run:


git clone https://github.com/V3nugopalKP/Handwritten-Digit-Recognition.git
cd Handwritten-Digit-Recognition

### ✅ Step 2: Install Dependencies
Install the required Python packages using:



pip install -r requirements.txt
### ✅ Step 3: Run The Flask App
Run the following command to start the Flask application:



python app.py
Open your browser and navigate to:


http://localhost:5000
### ✅ Step 4: Upload Image
Upload any image of a handwritten digit (0-9).

Click on Predict.

The model will predict the digit and display the result.

## 💎 Future Enhancements
Add a Drawing Pad: Allow users to draw digits instead of uploading images. 🎨

Deploy Online: Host the app on platforms like Render or Railway. 🌐

Improve Model: Use Convolutional Neural Networks (CNN) for better accuracy. 💻

User Authentication: Add a login system for user-specific features. 🔥
