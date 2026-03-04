from flask import Flask, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

MODEL_ID = "IgYahiko/crop-recommendation-t5"

app = Flask(__name__)

# Load once at startup
tokenizer = T5Tokenizer.from_pretrained(MODEL_ID)
model = T5ForConditionalGeneration.from_pretrained(MODEL_ID)
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No input text provided"}), 400

    input_text = f"recommend crop: {text}"

    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=16
        )

    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({
        "crop": prediction
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)