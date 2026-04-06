import os
import cv2
import numpy as np
import joblib
import mediapipe as mp
import base64
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Load model ───────────────────────────────────────────────────
MODEL_PATH = "sign_model.pkl"
bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
le = bundle["label_encoder"]
CLASSES = list(le.classes_)
print(f"✅ Model loaded. Classes: {CLASSES}")

# ── MediaPipe setup ──────────────────────────────────────────────
mp_hands = mp.solutions.hands

def get_landmark_features(hand_landmarks):
    lm = hand_landmarks.landmark
    wrist = lm[0]
    points = []
    for point in lm:
        points.append([
            point.x - wrist.x,
            point.y - wrist.y,
            point.z - wrist.z
        ])
    points = np.array(points)
    scale = np.max(np.linalg.norm(points, axis=1))
    if scale > 0:
        points = points / scale
    return points.flatten().reshape(1, -1)

@app.route("/")
def index():
    return render_template("index.html", classes=CLASSES)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        img_data = data["image"].split(",")[1]
        img_bytes = base64.b64decode(img_data)
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"error": "Could not decode image"}), 400

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.5
        ) as hands:
            result = hands.process(img_rgb)

            if not result.multi_hand_landmarks:
                return jsonify({"detected": False, "label": None, "confidence": 0, "all_probs": []})

            hand_lm = result.multi_hand_landmarks[0]
            features = get_landmark_features(hand_lm)
            pred_idx = model.predict(features)[0]
            probas = model.predict_proba(features)[0]
            confidence = float(probas[pred_idx])
            label = le.inverse_transform([pred_idx])[0]

            all_probs = [
                {"label": le.classes_[i], "prob": float(probas[i])}
                for i in np.argsort(probas)[::-1][:5]
            ]

            return jsonify({
                "detected": True,
                "label": label,
                "confidence": confidence,
                "all_probs": all_probs
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=False)
