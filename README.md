# 🌱 Crop Recommendation System (T5-based NLP Model)

An **AI-powered crop recommendation system** that suggests the most suitable crop based on **soil nutrients and climate conditions**, using a **Transformer (T5) language model** fine-tuned on synthetic agricultural data.

---
#### This project demonstrates how **NLP models can be used instead of traditional tabular ML** for structured decision-making tasks.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Transformers](https://img.shields.io/badge/Transformers-NLP-orange?style=for-the-badge)
![FLAN--T5](https://img.shields.io/badge/FLAN--T5-Text--to--Text-green?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST%20API-02569B?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)


---

## 🚀 Features

- 🧠 **NLP-based reasoning** using T5 (Text-to-Text Transformer)
- 🌾 Crop recommendation from soil & climate parameters
- 🧪 Synthetic dataset generation (domain-controlled)
- 🔥 Fine-tuned on Kaggle (free GPU)
- 🌐 REST API using Flask
- 🎨 Interactive UI using Streamlit
- 🤗 Model hosted on Hugging Face Hub

---


---

## 📊 Dataset Description

The dataset is **NLP-style**, not tabular.

| Column | Description |
|------|------------|
| `text` | Natural language description of soil & climate |
| `label` | Target crop (single token) |

### Example:
```text
Input:
"The soil has 80 ppm nitrogen, 50 ppm phosphorus, and 60 ppm potassium.
Temperature is 30°C, humidity is 75%, pH is 6.5, rainfall is 180 mm."

Target:
"cotton"
