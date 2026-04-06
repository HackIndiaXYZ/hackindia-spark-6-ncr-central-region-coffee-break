---
title: ASL Sign Language Detector
emoji: 🤟
colorFrom: cyan
colorTo: purple
sdk: docker
pinned: false
---

# ASL Real-Time Sign Language Detector

Real-time American Sign Language (ASL) detection using MediaPipe hand landmarks and a scikit-learn classifier.

## How to Use
1. Click **Start Camera** to enable your webcam
2. Show your hand sign to the camera
3. The detected letter appears instantly with confidence score
4. Use the **Sign Reference** panel on the right to see all signs
5. Letters are automatically added to history when held for 1.5 seconds

## Tech Stack
- **MediaPipe** — hand landmark extraction (21 keypoints)
- **scikit-learn** — Random Forest / MLP classifier
- **Flask** — web server
- **OpenCV** — image processing
