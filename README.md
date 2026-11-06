# CodeAlpha Internship Projects 🚀

A collection of three Python-based projects developed as part of my **CodeAlpha Internship**.

This repository showcases my practical experience in Artificial Intelligence, Machine Learning, Computer Vision, Natural Language Processing, and Flask-based application development.

---

## 📁 Projects Overview

### 1. AI Object Detection & Tracking

**Technologies:** Python, YOLO11n, OpenCV, SORT, Flask, NumPy, SciPy, FilterPy

An AI-powered real-time object detection and multi-object tracking application using the YOLO11n model and SORT tracking algorithm.

**Key Features:**
- Real-time object detection using YOLO11n.
- Multi-object tracking using the SORT algorithm.
- Unique tracking IDs for detected objects.
- Bounding box visualization.
- Kalman Filter-based object tracking.
- Live webcam streaming through Flask.

**Project Structure:**
```text
AI_Object_Detection/
├── templates/
│   └── index.html
├── app.py
├── sort.py
├── tracking.py
├── yolo11n.pt
└── requirements.txt
```

**Run Locally:**
```bash
cd AI_Object_Detection
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open: `http://127.0.0.1:5000`

---

### 2. FAQ Chatbot

**Technologies:** Python, Flask, Scikit-learn, TF-IDF, Cosine Similarity, HTML, CSS, JavaScript

A college FAQ chatbot that understands user questions and retrieves relevant answers from a predefined knowledge base using Natural Language Processing techniques.

**Key Features:**
- Predefined FAQ knowledge base.
- Multiple question patterns for each FAQ.
- TF-IDF text vectorization.
- Cosine similarity-based question matching.
- Similarity threshold for matching responses.
- Interactive web-based chatbot interface.
- Flask REST API integration.

**Project Structure:**
```text
FAQ/
├── app.py
├── faq_bot.py
├── index.html
├── script.js
├── style.css
└── requirements.txt
```

**Run Locally:**
```bash
cd FAQ
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open: `http://127.0.0.1:5000`

---

### 3. AI Language Translator

**Technologies:** Python, Flask, Deep Translator, GoogleTranslator, HTML, CSS, JavaScript

A web-based language translation application that translates text between multiple languages using the Google Translator service through the Deep Translator library.

**Key Features:**
- Automatic source language detection.
- Multiple language support.
- English, Hindi, Kannada, French, German, Spanish, Japanese and more.
- Real-time translation requests.
- Copy translated text functionality.
- Interactive and responsive user interface.

**Project Structure:**
```text
Translation_tool/
├── templates/
│   └── index.html
├── app.py
└── requirements.txt
```

**Run Locally:**
```bash
cd Translation_tool
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open: `http://127.0.0.1:5000`

---

## 🛠️ Technologies & Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Computer Vision | YOLO11n, OpenCV |
| Object Tracking | SORT, Kalman Filter |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF, Cosine Similarity |
| Translation | Deep Translator, GoogleTranslator |
| Frontend | HTML, CSS, JavaScript |
| Numerical Computing | NumPy, SciPy |

---

## ⚙️ Prerequisites

- Python 3.9 or later
- pip package manager
- Git
- Webcam (for AI Object Detection)
- Internet connection (for language translation)

Each project has its own `requirements.txt` file.

---

## 👨‍💻 Author

**Srinivas Gowda**

B.E. – Artificial Intelligence & Data Science  
Mysore University School of Engineering

GitHub: [@srinivasgowdruu](https://github.com/srinivasgowdruu)

---

## 🎯 Internship

**CodeAlpha Internship**

This repository contains three projects completed as part of my CodeAlpha internship, demonstrating practical implementation of Python, AI, Machine Learning, Computer Vision, NLP, and web application development.

---

⭐ If you find these projects interesting, feel free to explore the repositories and star this project!