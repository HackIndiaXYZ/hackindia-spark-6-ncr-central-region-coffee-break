# 🤟 SignBridge – Real-Time ASL Communication System

🏆 Built for HackIndia Spark 6 @ NIT Delhi

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/jayantjain052005/asl-detector

---

## 🚨 Problem

Millions of people with hearing and speech impairments face difficulty communicating in real-time, especially in public spaces, education, and workplaces.

---

## 💡 Solution

SignBridge is an AI-powered real-time sign language detection system that converts hand gestures into readable text using computer vision and machine learning.

It acts as a **communication bridge** between sign language users and non-signers.

---

## ⚙️ Features

* 🎥 Real-time hand tracking using MediaPipe
* 🤖 Machine learning-based ASL alphabet detection
* 💬 Instant gesture-to-text conversion
* 📊 Confidence score for predictions
* 🧠 Smart letter capture (1.5s hold detection)
* 📝 Letter history tracking for word formation
* 📚 Built-in sign reference panel

---

## 🛠️ Tech Stack

* **MediaPipe** — hand landmark extraction (21 keypoints)
* **scikit-learn** — classification (Random Forest / MLP)
* **Flask** — backend server
* **OpenCV** — image processing
* **Hugging Face Spaces (Docker)** — deployment

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

---

## 🎮 How to Use

1. Click **Start Camera**
2. Show hand signs in front of webcam
3. Detected letter appears with confidence score
4. Hold gesture for ~1.5 seconds to capture
5. Build words using detected letters

---

## 📸 Demo Preview

(Add screenshots or demo video here)

---

## 🚀 Future Scope

* 🔊 Text-to-Speech output
* 🧠 Full word/sentence prediction
* 📱 Mobile app integration
* 🌍 Multi-language sign support

---

## 👨‍💻 Team

Coffee Break – HackIndia

---
